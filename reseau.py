from PySide6.QtCore import QSize, QObject, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QMessageBox
import socket
import threading
import json
from datetime import datetime
import sqlite3
from functools import lru_cache
import logging
import hashlib
import time

from gui.reseau_interface import Ui_Dialog

MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10 MB max
BUFFER_SIZE = 8192
CONNECTION_TIMEOUT = 30.0
MAX_CONNECTIONS = 50


class ServerSignals(QObject):
    status_changed = Signal(str)
    log_message = Signal(str)
    client_connected = Signal(str, str)
    client_disconnected = Signal(str, str)


class ServerManager:
    """Gestionnaire de serveur persistant - survit à la fermeture du dialog"""
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized'):
            return

        self._initialized = True
        self.signals = ServerSignals()

        # État du serveur
        self.is_running = False
        self.host = '0.0.0.0'
        self.port = 8888
        self.server_socket = None
        self.server_thread = None

        # Gestion des threads
        self.lock = threading.RLock()
        self.connected_rooms = {}
        self.active_connections = 0
        self.db_pool = []

        # Logging
        self.setup_logging()

    def setup_logging(self):
        """Configuration du logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('server.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def log(self, message, level=logging.INFO):
        """Log avec émission du signal"""
        self.logger.log(level, message)
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.signals.log_message.emit(f"[{timestamp}] {message}")

    def get_db_connection(self):
        """Obtenir une connexion à la base de données"""
        try:
            if self.db_pool:
                return self.db_pool.pop()
            return self.init_db()
        except Exception as e:
            self.log(f"Erreur de connexion DB: {e}", logging.ERROR)
            return None

    def return_db_connection(self, conn):
        """Retourner une connexion au pool"""
        if conn and len(self.db_pool) < 5:
            self.db_pool.append(conn)
        elif conn:
            conn.close()

    def init_db(self):
        """Initialiser la base de données"""
        conn = sqlite3.connect('database.db', check_same_thread=False, timeout=10.0)
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=NORMAL")
        conn.execute("PRAGMA cache_size=10000")

        conn.executescript("""
            CREATE TABLE IF NOT EXISTS captures (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                uid TEXT NOT NULL,
                salle TEXT NOT NULL,
                nom TEXT NOT NULL,
                image BLOB NOT NULL,
                image_hash TEXT NOT NULL,
                image_size INTEGER NOT NULL,
                timestamp TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );

            CREATE INDEX IF NOT EXISTS idx_captures_uid_salle ON captures(uid, salle);
            CREATE INDEX IF NOT EXISTS idx_captures_timestamp ON captures(timestamp);
            CREATE INDEX IF NOT EXISTS idx_captures_hash ON captures(image_hash);

            CREATE TABLE IF NOT EXISTS autorisations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                uid TEXT NOT NULL,
                salle TEXT NOT NULL,
                nom TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(uid, salle)
            );

            CREATE INDEX IF NOT EXISTS idx_auth_uid_salle ON autorisations(uid, salle);
        """)

        conn.commit()
        return conn

    @lru_cache(maxsize=1000)
    def is_authorized(self, uid, salle):
        """Vérifier l'autorisation"""
        conn = self.get_db_connection()
        if not conn:
            return None

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT nom FROM autorisations WHERE uid=? AND salle=?", (uid, salle))
            result = cursor.fetchone()
            return result[0] if result else None
        except Exception as e:
            self.log(f"Erreur vérification autorisation: {e}", logging.ERROR)
            return None
        finally:
            self.return_db_connection(conn)

    def save_capture(self, uid, salle, nom, image_data, timestamp):
        """Sauvegarder une capture"""
        conn = self.get_db_connection()
        if not conn:
            return False

        try:
            image_hash = hashlib.sha256(image_data).hexdigest()
            image_size = len(image_data)

            cursor = conn.cursor()
            cursor.execute(
                "SELECT id FROM captures WHERE image_hash=? AND uid=? AND salle=? LIMIT 1",
                (image_hash, uid, salle)
            )

            if cursor.fetchone():
                self.log(f"Image dupliquée détectée pour {nom} dans {salle}")
                return True

            with self.lock:
                conn.execute(
                    """INSERT INTO captures (uid, salle, nom, image, image_hash, image_size, timestamp) 
                       VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    (uid, salle, nom, image_data, image_hash, image_size, timestamp)
                )
                conn.commit()

            self.log(f"Capture sauvegardée: {nom} ({image_size} octets)")
            return True

        except Exception as e:
            self.log(f"Erreur sauvegarde capture: {e}", logging.ERROR)
            return False
        finally:
            self.return_db_connection(conn)

    def receive_data_with_timeout(self, client_sock):
        """Recevoir des données avec timeout"""
        buffer = bytearray()
        start_time = time.time()

        while True:
            if time.time() - start_time > CONNECTION_TIMEOUT:
                raise socket.timeout("Timeout réception données")

            try:
                data = client_sock.recv(BUFFER_SIZE)
                if not data:
                    break

                buffer.extend(data)

                if b"EOF" in data:
                    eof_pos = buffer.find(b"EOF")
                    buffer = buffer[:eof_pos]
                    break

                if len(buffer) > MAX_IMAGE_SIZE:
                    raise ValueError(f"Taille des données dépasse la limite: {len(buffer)} octets")

            except socket.timeout:
                continue

        return bytes(buffer)

    def _send_error_response(self, client_sock, error_msg):
        """Envoyer une réponse d'erreur"""
        try:
            response = {"status": "ERROR", "reason": error_msg}
            client_sock.sendall(json.dumps(response).encode('utf-8'))
        except:
            pass

    def handle_client(self, client_sock, addr):
        """Gérer un client"""
        salle = None
        conn_start = time.time()

        try:
            client_sock.settimeout(CONNECTION_TIMEOUT)

            # Recevoir les données JSON
            json_data = client_sock.recv(1024).decode('utf-8').strip()
            if not json_data:
                raise ValueError("Aucune donnée initiale reçue")

            try:
                client_data = json.loads(json_data)
            except json.JSONDecodeError as e:
                raise ValueError(f"Format JSON invalide: {e}")

            salle = client_data.get("room", "").strip()
            uid = client_data.get("uid", "").strip()

            if not salle or not uid:
                raise ValueError("Champs requis manquants: room et uid")

            # Mise à jour du suivi des connexions
            with self.lock:
                if salle not in self.connected_rooms:
                    self.connected_rooms[salle] = 0
                self.connected_rooms[salle] += 1
                self.active_connections += 1

                if self.active_connections > MAX_CONNECTIONS:
                    raise ValueError("Serveur à capacité maximale")

            self.log(f"Client connecté de {addr} à la salle '{salle}' (Total: {self.active_connections})")

            # Vérification d'autorisation
            nom = self.is_authorized(uid, salle)
            if not nom:
                response = {"status": "DENIED", "reason": "Accès refusé - identifiants invalides"}
                client_sock.sendall(json.dumps(response).encode('utf-8'))
                self.log(f"Accès refusé pour UID {uid} dans la salle {salle}")
                return

            # Envoyer succès d'autorisation
            response = {"status": "OK", "message": "Envoyer les données d'image", "user": nom}
            client_sock.sendall(json.dumps(response).encode('utf-8'))

            # Recevoir les données d'image
            self.log(f"Réception d'image de {nom} dans {salle}")
            image_data = self.receive_data_with_timeout(client_sock)

            if not image_data:
                raise ValueError("Aucune donnée d'image reçue")

            # Sauvegarder la capture
            timestamp = datetime.now().isoformat()
            if self.save_capture(uid, salle, nom, image_data, timestamp):
                response = {
                    "status": "GRANTED",
                    "timestamp": timestamp,
                    "size": len(image_data),
                    "user": nom
                }
                self.log(f"Image sauvegardée avec succès pour {nom} ({len(image_data)} octets)")
            else:
                response = {"status": "ERROR", "reason": "Échec de sauvegarde de l'image"}

            client_sock.sendall(json.dumps(response).encode('utf-8'))

        except socket.timeout:
            self.log(f"Timeout de connexion avec {addr}", logging.WARNING)
            self._send_error_response(client_sock, "Timeout de connexion")

        except ValueError as e:
            self.log(f"Erreur de validation des données de {addr}: {e}", logging.WARNING)
            self._send_error_response(client_sock, str(e))

        except Exception as e:
            self.log(f"Erreur inattendue lors de la gestion du client {addr}: {e}", logging.ERROR)
            self._send_error_response(client_sock, "Erreur interne du serveur")

        finally:
            try:
                client_sock.close()
            except:
                pass

            if salle:
                with self.lock:
                    if salle in self.connected_rooms:
                        self.connected_rooms[salle] -= 1
                        if self.connected_rooms[salle] <= 0:
                            del self.connected_rooms[salle]

                    self.active_connections = max(0, self.active_connections - 1)

                duration = time.time() - conn_start
                self.log(
                    f"Client {addr} déconnecté de la salle '{salle}' (Durée: {duration:.2f}s, Actifs: {self.active_connections})")

    def start_server(self):
        """Démarrer le serveur"""
        if self.is_running:
            self.log("Le serveur est déjà en cours d'exécution")
            return False

        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(10)

            self.is_running = True
            self.log(f"Serveur démarré sur {self.host}:{self.port}")
            self.signals.status_changed.emit(f"Serveur actif sur {self.host}:{self.port}")

            # Démarrer le thread du serveur
            self.server_thread = threading.Thread(
                target=self._server_loop,
                daemon=True,
                name="ServerThread"
            )
            self.server_thread.start()
            return True

        except Exception as e:
            self.log(f"Erreur de démarrage du serveur: {e}", logging.ERROR)
            self.is_running = False
            return False

    def _server_loop(self):
        """Boucle principale du serveur"""
        try:
            while self.is_running:
                try:
                    self.server_socket.settimeout(1.0)
                    client_sock, addr = self.server_socket.accept()

                    client_thread = threading.Thread(
                        target=self.handle_client,
                        args=(client_sock, addr),
                        daemon=True,
                        name=f"Client-{addr[0]}:{addr[1]}"
                    )
                    client_thread.start()

                except socket.timeout:
                    continue
                except OSError:
                    if self.is_running:
                        self.log("Socket serveur fermé", logging.INFO)
                    break

        except Exception as e:
            self.log(f"Erreur serveur: {e}", logging.ERROR)
        finally:
            self._cleanup_server()

    def stop_server(self):
        """Arrêter le serveur"""
        if not self.is_running:
            self.log("Le serveur n'est pas en cours d'exécution")
            return False

        self.log("Arrêt du serveur en cours...")
        self.is_running = False

        if self.server_socket:
            try:
                self.server_socket.close()
            except:
                pass

        return True

    def _cleanup_server(self):
        """Nettoyage après arrêt du serveur"""
        self.server_socket = None

        # Nettoyer les connexions DB
        while self.db_pool:
            conn = self.db_pool.pop()
            try:
                conn.close()
            except:
                pass

        # Nettoyer le suivi des connexions
        with self.lock:
            self.connected_rooms.clear()
            self.active_connections = 0

        self.signals.status_changed.emit("Serveur arrêté")
        self.log("Serveur arrêté et nettoyé")

    def get_status(self):
        """Obtenir le statut actuel du serveur"""
        return {
            "is_running": self.is_running,
            "host": self.host,
            "port": self.port,
            "active_connections": self.active_connections,
            "connected_rooms": dict(self.connected_rooms),
            "total_rooms": len(self.connected_rooms)
        }


class Reseau(QDialog):
    """Dialog réseau qui utilise le gestionnaire de serveur persistant"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = parent

        # Obtenir l'instance du gestionnaire de serveur (singleton)
        self.server_manager = ServerManager()

        # Interface utilisateur
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Connecter les signaux du serveur
        self.connect_server_signals()

        # Mettre à jour l'interface selon l'état actuel
        self.update_ui_from_server_state()

        # Connexion des boutons
        self.ui.bouton_serveur.clicked.connect(self.toggle_server)

    def connect_server_signals(self):
        """Connecter les signaux du gestionnaire de serveur"""
        self.server_manager.signals.status_changed.connect(self.on_status_changed)
        self.server_manager.signals.log_message.connect(self.on_log_message)

    def update_ui_from_server_state(self):
        """Mettre à jour l'interface selon l'état actuel du serveur"""
        status = self.server_manager.get_status()

        if status["is_running"]:
            # Serveur en cours d'exécution
            icon = QIcon(":/icons/icons8-power-on.png")
            self.ui.bouton_serveur.setIcon(icon)
            self.ui.bouton_serveur.setText("Arrêter le serveur")
            self.ui.label_etat_sever.setText(f"Serveur actif sur {status['host']}:{status['port']}")
        else:
            # Serveur arrêté
            icon = QIcon(":/icons/icons8-power-off.png")
            self.ui.bouton_serveur.setIcon(icon)
            self.ui.bouton_serveur.setText("Démarrer le serveur")
            self.ui.label_etat_sever.setText("Serveur arrêté")

    def toggle_server(self):
        """Basculer l'état du serveur"""
        if self.server_manager.is_running:
            success = self.server_manager.stop_server()
            if success:
                self.log("Serveur arrêté par l'utilisateur")
        else:
            success = self.server_manager.start_server()
            if success:
                self.log("Serveur démarré par l'utilisateur")
            else:
                QMessageBox.critical(self, "Erreur", "Impossible de démarrer le serveur")

    def on_status_changed(self, status):
        """Gestionnaire de changement de statut"""
        self.ui.label_etat_sever.setText(status)
        self.update_ui_from_server_state()

    def on_log_message(self, message):
        """Gestionnaire de message de log"""
        self.log(message)

    def log(self, message):
        """Envoyer un message de log à la fenêtre principale"""
        if self.main_window and hasattr(self.main_window, 'log_message'):
            self.main_window.log_message(message)
        print(message)

    def closeEvent(self, event):
        """Gérer la fermeture du dialog - NE PAS arrêter le serveur"""
        # Le serveur continue de fonctionner même si le dialog est fermé
        self.log("Dialog réseau fermé - le serveur continue de fonctionner")
        event.accept()

    def reject(self):
        """Gérer l'annulation du dialog - NE PAS arrêter le serveur"""
        self.log("Dialog réseau fermé via Annuler - le serveur continue de fonctionner")
        super().reject()

    def get_server_info(self):
        """Obtenir les informations du serveur pour affichage"""
        return self.server_manager.get_status()