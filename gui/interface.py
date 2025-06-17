# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windows.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(847, 616)
        MainWindow.setMinimumSize(QSize(750, 600))
        MainWindow.setStyleSheet(u"")
        self.actionutilisateur = QAction(MainWindow)
        self.actionutilisateur.setObjectName(u"actionutilisateur")
        self.actionajouter_une_personne = QAction(MainWindow)
        self.actionajouter_une_personne.setObjectName(u"actionajouter_une_personne")
        self.actionr_seau = QAction(MainWindow)
        self.actionr_seau.setObjectName(u"actionr_seau")
        self.actionJournal_d_authentification = QAction(MainWindow)
        self.actionJournal_d_authentification.setObjectName(u"actionJournal_d_authentification")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(100, 50))
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0,150);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMaximumSize(QSize(5000, 10280))
        self.widget.setStyleSheet(u"background-color: rgb(76, 52, 255);")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(400, 200))
        self.widget_3.setMaximumSize(QSize(5000, 5000))
        self.widget_3.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 0, 5)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(500, 500))
        self.verticalLayout_10 = QVBoxLayout(self.widget_5)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, -1, 0)
        self.label_camera = QLabel(self.widget_5)
        self.label_camera.setObjectName(u"label_camera")
        self.label_camera.setMaximumSize(QSize(300, 300))
        self.label_camera.setStyleSheet(u"background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1c1c1c, stop:1 #2c3e50);\n"
"border: 2px solid #3498db;\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"color: white;")

        self.verticalLayout_10.addWidget(self.label_camera)

        self.label_infos_camera = QLabel(self.widget_5)
        self.label_infos_camera.setObjectName(u"label_infos_camera")
        self.label_infos_camera.setMinimumSize(QSize(0, 5))
        self.label_infos_camera.setMaximumSize(QSize(500, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_infos_camera.setFont(font1)
        self.label_infos_camera.setStyleSheet(u"")
        self.label_infos_camera.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_infos_camera)


        self.horizontalLayout_2.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(100, 0))
        self.widget_6.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(145, 100))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_photo_trouver = QLabel(self.widget_9)
        self.label_photo_trouver.setObjectName(u"label_photo_trouver")
        self.label_photo_trouver.setMinimumSize(QSize(154, 154))
        self.label_photo_trouver.setMaximumSize(QSize(180, 200))
        self.label_photo_trouver.setStyleSheet(u"\n"
"QLabel {\n"
"    border: 2px dashed #0078D7;\n"
"    border-radius: 6px;\n"
"    background-color: #f9f9f9;\n"
"    min-width: 150px;\n"
"    min-height: 150px;\n"
"background-color: rgb(107, 107, 107);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.label_photo_trouver)

        self.label_infos = QLabel(self.widget_9)
        self.label_infos.setObjectName(u"label_infos")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_infos.setFont(font2)
        self.label_infos.setStyleSheet(u"")
        self.label_infos.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_infos)


        self.verticalLayout_5.addWidget(self.widget_9)

        self.widget_13 = QWidget(self.widget_6)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget_13)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_3.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.label_5 = QLabel(self.widget_13)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(False)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(255, 48, 11);")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)


        self.verticalLayout_5.addWidget(self.widget_13)


        self.horizontalLayout_2.addWidget(self.widget_6)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.widget_4.setMaximumSize(QSize(500, 5000))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_4 = QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_14 = QWidget(self.widget_7)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_6 = QVBoxLayout(self.widget_14)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.widget_14)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"QLabel {\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
" \n"
"    border-radius: 7px; /* Coins arrondis */\n"
"    /*background-color: #f0f0f0; /* Couleur de fond si l'image est transparente */\n"
"}\n"
"")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_4)


        self.verticalLayout_4.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_7)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.widget_15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_15)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	\n"
"	background-color: rgb(34, 34, 34);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    border: 2px solid #000; /* Bordure noire */\n"
"    border-radius: 10px; /* Coins arrondis */\n"
"    /*background-color: #f0f0f0; /* Couleur de fond si l'image est transparente */\n"
"}\n"
"")

        self.verticalLayout_7.addWidget(self.label_2)


        self.verticalLayout_4.addWidget(self.widget_15)


        self.horizontalLayout_6.addWidget(self.widget_7)


        self.verticalLayout_3.addWidget(self.widget_4)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.frame_2)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.widget_2.setMaximumSize(QSize(700, 600))
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.widget_2)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 50))
        self.widget_10.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_8.addWidget(self.widget_10, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_11 = QWidget(self.widget_2)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy3)
        self.verticalLayout_9 = QVBoxLayout(self.widget_11)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.widget_11)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"/* Style g\u00e9n\u00e9ral pour le QTableWidget */\n"
"QTableWidget {\n"
"    /*background-color: #f8f9fa; /* Fond clair pour une apparence professionnelle */\n"
"    border: 1px solid #ced4da; /* Bordure l\u00e9g\u00e8re et neutre */\n"
"    gridline-color: #dee2e6; /* Couleur des lignes de la grille */\n"
"    font-size: 14px; /* Taille de police standard */\n"
"    font-family: Arial, sans-serif; /* Police professionnelle */\n"
"    selection-background-color: #007bff; /* Couleur de fond pour la s\u00e9lection */\n"
"    selection-color: #ffffff; /* Texte de la s\u00e9lection en blanc */\n"
"}\n"
"\n"
"/* Style des en-t\u00eates horizontaux */\n"
"QHeaderView::section {\n"
"    background-color: #343a40; /* Fond sombre pour les en-t\u00eates */\n"
"    color: #ffffff; /* Texte blanc pour le contraste */\n"
"    font-weight: bold; /* Texte en gras */\n"
"    border: 1px solid #495057; /* Lignes autour des en-t\u00eates */\n"
"    padding: 4px; /* Espacement interne */\n"
"}\n"
"\n"
"/* Style des en-t\u00eate"
                        "s verticaux */\n"
"QHeaderView::section:vertical {\n"
"    background-color: #e9ecef; /* Fond clair pour les en-t\u00eates verticaux */\n"
"    color: #495057; /* Texte gris fonc\u00e9 */\n"
"    border: 1px solid #dee2e6; /* Lignes autour des en-t\u00eates verticaux */\n"
"    padding: 4px;\n"
"}\n"
"\n"
"/* Style pour les lignes altern\u00e9es */\n"
"QTableWidget::item {\n"
"    padding: 6px; /* Espacement interne des cellules */\n"
"}\n"
"\n"
"QTableWidget::item:alternate {\n"
"    background-color: #f1f3f5; /* Fond gris clair pour les lignes altern\u00e9es */\n"
"}\n"
"\n"
"/* Survol des \u00e9l\u00e9ments */\n"
"QTableWidget::item:hover {\n"
"    background-color: #e2e6ea; /* Couleur de survol */\n"
"}\n"
"\n"
"/* Style pour les bordures pendant la s\u00e9lection */\n"
"QTableWidget::item:selected {\n"
"    border: 1px solid #0056b3;\n"
"}\n"
"\n"
"/* Barre de d\u00e9filement */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f8f9fa;\n"
"    width: 12px;\n"
"    margin: 0px;\n"
"}\n"
""
                        "\n"
"QScrollBar::handle:vertical {\n"
"    background: #6c757d;\n"
"    border-radius: 6px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"    background: none;\n"
"}\n"
"")

        self.verticalLayout_9.addWidget(self.tableWidget)


        self.verticalLayout_8.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_2)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(300, 35))
        self.widget_12.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.boutton_afficher = QPushButton(self.widget_12)
        self.boutton_afficher.setObjectName(u"boutton_afficher")
        self.boutton_afficher.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/display-arrow-down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boutton_afficher.setIcon(icon)
        self.boutton_afficher.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.boutton_afficher)

        self.boutton_supprimer = QPushButton(self.widget_12)
        self.boutton_supprimer.setObjectName(u"boutton_supprimer")
        icon1 = QIcon()
        icon1.addFile(u":/icons/delete-off.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boutton_supprimer.setIcon(icon1)
        self.boutton_supprimer.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.boutton_supprimer)

        self.boutton_modifier = QPushButton(self.widget_12)
        self.boutton_modifier.setObjectName(u"boutton_modifier")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-edit-24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boutton_modifier.setIcon(icon2)
        self.boutton_modifier.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.boutton_modifier)

        self.boutton_refresh = QPushButton(self.widget_12)
        self.boutton_refresh.setObjectName(u"boutton_refresh")
        icon3 = QIcon()
        icon3.addFile(u":/icons/back-up (1).svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.boutton_refresh.setIcon(icon3)
        self.boutton_refresh.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.boutton_refresh)


        self.verticalLayout_8.addWidget(self.widget_12, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 847, 33))
        self.menuparam_tre = QMenu(self.menubar)
        self.menuparam_tre.setObjectName(u"menuparam_tre")
        self.menuBase_de_donn_e = QMenu(self.menubar)
        self.menuBase_de_donn_e.setObjectName(u"menuBase_de_donn_e")
        self.menuHistoriques = QMenu(self.menubar)
        self.menuHistoriques.setObjectName(u"menuHistoriques")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuparam_tre.menuAction())
        self.menubar.addAction(self.menuBase_de_donn_e.menuAction())
        self.menubar.addAction(self.menuHistoriques.menuAction())
        self.menuparam_tre.addAction(self.actionutilisateur)
        self.menuparam_tre.addAction(self.actionr_seau)
        self.menuBase_de_donn_e.addAction(self.actionajouter_une_personne)
        self.menuHistoriques.addAction(self.actionJournal_d_authentification)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"fenetre principale", None))
        self.actionutilisateur.setText(QCoreApplication.translate("MainWindow", u"utilisateur", None))
        self.actionajouter_une_personne.setText(QCoreApplication.translate("MainWindow", u"ajouter une personne", None))
        self.actionr_seau.setText(QCoreApplication.translate("MainWindow", u"r\u00e9seau", None))
        self.actionJournal_d_authentification.setText(QCoreApplication.translate("MainWindow", u"Journal d'authentification", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SECURITY - ESP32_CAM", None))
        self.label_camera.setText("")
        self.label_infos_camera.setText("")
        self.label_photo_trouver.setText("")
        self.label_infos.setText(QCoreApplication.translate("MainWindow", u"Infos de la personne", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nombre de salle connect\u00e9e:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Journal des evenements", None))
        self.label_2.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Badge", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Salle", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Photos", None));
        self.boutton_afficher.setText("")
        self.boutton_supprimer.setText("")
        self.boutton_modifier.setText("")
        self.boutton_refresh.setText("")
        self.menuparam_tre.setTitle(QCoreApplication.translate("MainWindow", u"param\u00e8tre", None))
        self.menuBase_de_donn_e.setTitle(QCoreApplication.translate("MainWindow", u"Base de donn\u00e9e", None))
        self.menuHistoriques.setTitle(QCoreApplication.translate("MainWindow", u"Historiques", None))
    # retranslateUi

