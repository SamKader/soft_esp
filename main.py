import sys
import queue
import time  # Ajouté pour le délai dans closeEvent
from datetime import datetime
from PySide6.QtCore import QTimer, Signal, QObject
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PySide6.QtGui import QTextCursor, QFont
from gui.interface import Ui_MainWindow
from gui.ressources import icons_rc


class LogManager(QObject):
    """Separate log management class for better organization"""
    log_received = Signal(str)

    def __init__(self):
        super().__init__()
        self.log_queue = queue.Queue()  # Thread-safe queue

    def add_log(self, message):
        """Add a message to the log queue"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {message}"
        self.log_queue.put(formatted_message)

    def get_pending_logs(self):
        """Get all pending log messages"""
        messages = []
        try:
            while True:
                message = self.log_queue.get_nowait()
                messages.append(message)
        except queue.Empty:
            pass
        return messages


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize components
        self.log_manager = LogManager()
        self.reseau_dialog = None  # Keep reference to avoid garbage collection

        # Setup logging system
        self.setup_logging()

        # Setup UI
        self.setup_ui()

        # Connect actions
        self.connect_actions()

        # Initial log message
        self.log_message("Application started successfully")

    def setup_logging(self):
        """Configure the logging system"""
        self.log_timer = QTimer()
        self.log_timer.timeout.connect(self.update_logs)
        self.log_timer.start(50)  # Check for new logs every 50ms (more responsive)

        # Configure log display if it exists
        if hasattr(self.ui, 'log_text'):
            # Set monospace font for better log readability
            font = QFont("Consolas", 9)
            if not font.exactMatch():
                font = QFont("Courier New", 9)
            self.ui.log_text.setFont(font)

            # Set maximum lines to prevent memory issues
            self.ui.log_text.document().setMaximumBlockCount(1000)

    def setup_ui(self):
        """Setup additional UI configurations"""
        # Set window title with version info
        self.setWindowTitle("Network Server Manager v1.0")

        # Setup status bar if it exists
        if hasattr(self.ui, 'statusbar'):
            self.ui.statusbar.showMessage("Ready")

    def connect_actions(self):
        """Connect UI actions to their handlers"""
        # Network dialog action
        if hasattr(self.ui, 'actionr_seau'):
            self.ui.actionr_seau.triggered.connect(self.ouvrir_dialog_reseau)

        # Add other action connections here as needed
        # Example: self.ui.actionExit.triggered.connect(self.close)

    def update_logs(self):
        """Update log display with new messages"""
        if not hasattr(self.ui, 'log_text'):
            return

        messages = self.log_manager.get_pending_logs()
        if not messages:
            return

        # Batch update for better performance
        cursor = self.ui.log_text.textCursor()
        cursor.movePosition(QTextCursor.End)

        for message in messages:
            cursor.insertText(message + "\n")

        # Auto-scroll to bottom
        scrollbar = self.ui.log_text.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

        # Update status bar with last message
        if hasattr(self.ui, 'statusbar') and messages:
            last_message = messages[-1].split('] ', 1)[-1]  # Remove timestamp
            self.ui.statusbar.showMessage(f"Last: {last_message}", 3000)

    def log_message(self, message):
        """Add a message to the log queue"""
        self.log_manager.add_log(message)

    def ouvrir_dialog_reseau(self):
        """Ouvrir le dialog de configuration réseau"""
        try:
            self.log_message("Ouverture du dialog réseau...")

            # Import ici pour éviter les imports circulaires
            from reseau import Reseau

            # Vérifier si le dialog existe déjà et n'est pas fermé
            if self.reseau_dialog and not self.reseau_dialog.isHidden():
                # Ramener le dialog au premier plan
                self.reseau_dialog.raise_()
                self.reseau_dialog.activateWindow()
                self.log_message("Dialog réseau déjà ouvert - ramené au premier plan")
                return

            # Créer un nouveau dialog
            self.reseau_dialog = Reseau(self)

            # Connecter les signaux du serveur pour l'intégration
            if hasattr(self.reseau_dialog, 'server_manager'):
                self.reseau_dialog.server_manager.signals.log_message.connect(self.log_message)
                self.reseau_dialog.server_manager.signals.status_changed.connect(self.on_server_status_changed)

            # Afficher le dialog (non modal pour permettre l'interaction avec la fenêtre principale)
            self.reseau_dialog.show()
            self.log_message("Dialog réseau ouvert")

        except ImportError as e:
            error_msg = f"Échec d'import du module réseau: {e}"
            self.log_message(error_msg)
            QMessageBox.critical(self, "Erreur d'Import", error_msg)

        except Exception as e:
            error_msg = f"Erreur lors de l'ouverture du dialog réseau: {e}"
            self.log_message(error_msg)
            QMessageBox.critical(self, "Erreur", error_msg)

    def on_server_status_changed(self, status):
        """Handle server status changes"""
        self.log_message(f"Server status: {status}")
        if hasattr(self.ui, 'statusbar'):
            self.ui.statusbar.showMessage(f"Server: {status}")

    def closeEvent(self, event):
        """Gérer la fermeture de l'application"""
        try:
            self.log_message("Fermeture de l'application...")

            # Vérifier si le serveur est en cours d'exécution
            server_running = False
            if self.reseau_dialog and hasattr(self.reseau_dialog, 'server_manager'):
                server_running = self.reseau_dialog.server_manager.is_running

            # Si le serveur fonctionne, demander confirmation
            if server_running:
                reply = QMessageBox.question(
                    self,
                    "Serveur en cours d'exécution",
                    "Le serveur réseau est actuellement en cours d'exécution.\n"
                    "Voulez-vous l'arrêter et fermer l'application ?",
                    QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                    QMessageBox.Cancel
                )

                if reply == QMessageBox.Yes:
                    # Arrêter le serveur
                    self.log_message("Arrêt du serveur avant fermeture...")
                    self.reseau_dialog.server_manager.stop_server()
                    time.sleep(0.5)  # Petit délai pour permettre l'arrêt propre
                elif reply == QMessageBox.No:
                    # Fermer sans arrêter le serveur (le serveur continuera en arrière-plan)
                    self.log_message("Fermeture de l'application - le serveur continue en arrière-plan")
                else:
                    # Annuler la fermeture
                    event.ignore()
                    return

            # Arrêter le timer de logs
            if hasattr(self, 'log_timer'):
                self.log_timer.stop()

            # Fermer le dialog réseau s'il est ouvert (sans arrêter le serveur)
            if self.reseau_dialog and not self.reseau_dialog.isHidden():
                self.log_message("Fermeture du dialog réseau...")
                self.reseau_dialog.close()

            # Accepter l'événement de fermeture
            event.accept()
            self.log_message("Application fermée avec succès")

        except Exception as e:
            self.log_message(f"Erreur lors de la fermeture: {e}")
            event.accept()  # Fermer quand même

    def show_about(self):
        """Show about dialog"""
        QMessageBox.about(
            self,
            "About Network Server Manager",
            "Network Server Manager v1.0\n\n"
            "A Qt-based network server management application.\n"
            "Built with PySide6 and Python."
        )

    def get_log_history(self):
        """Get current log history as text"""
        if hasattr(self.ui, 'log_text'):
            return self.ui.log_text.toPlainText()
        return ""

    def clear_logs(self):
        """Clear log display"""
        if hasattr(self.ui, 'log_text'):
            self.ui.log_text.clear()
            self.log_message("Log history cleared")

    def export_logs(self):
        """Export logs to file"""
        try:
            from PySide6.QtWidgets import QFileDialog

            filename, _ = QFileDialog.getSaveFileName(
                self,
                "Export Logs",
                f"server_logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                "Text Files (*.txt);;All Files (*)"
            )

            if filename:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(self.get_log_history())
                self.log_message(f"Logs exported to: {filename}")

        except Exception as e:
            error_msg = f"Failed to export logs: {e}"
            self.log_message(error_msg)
            QMessageBox.warning(self, "Export Error", error_msg)


def main():
    """Main application entry point"""
    try:
        # Create application
        app = QApplication(sys.argv)
        app.setApplicationName("Network Server Manager")
        app.setApplicationVersion("1.0")
        app.setOrganizationName("Your Organization")

        # Create and show main window
        window = MainWindow()
        window.show()

        # Start application event loop
        sys.exit(app.exec())

    except Exception as e:
        print(f"Critical error starting application: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()