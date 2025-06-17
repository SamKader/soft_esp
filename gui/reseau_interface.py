# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reseau.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 300)
        Dialog.setMinimumSize(QSize(400, 200))
        Dialog.setMaximumSize(QSize(600, 300))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_etat_reseau = QLabel(self.widget_3)
        self.label_etat_reseau.setObjectName(u"label_etat_reseau")

        self.horizontalLayout_3.addWidget(self.label_etat_reseau)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.champ_port = QLineEdit(self.widget_4)
        self.champ_port.setObjectName(u"champ_port")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.champ_port.sizePolicy().hasHeightForWidth())
        self.champ_port.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.champ_port)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.widget_5)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.champ_ip = QLineEdit(self.widget_5)
        self.champ_ip.setObjectName(u"champ_ip")
        sizePolicy1.setHeightForWidth(self.champ_ip.sizePolicy().hasHeightForWidth())
        self.champ_ip.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.champ_ip)


        self.verticalLayout_3.addWidget(self.widget_5)

        self.widget_8 = QWidget(self.widget)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_5 = QVBoxLayout(self.widget_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.bouton_reseau = QPushButton(self.widget_8)
        self.bouton_reseau.setObjectName(u"bouton_reseau")

        self.verticalLayout_5.addWidget(self.bouton_reseau)


        self.verticalLayout_3.addWidget(self.widget_8)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.frame_2)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_etat_sever = QLabel(self.widget_6)
        self.label_etat_sever.setObjectName(u"label_etat_sever")

        self.horizontalLayout_2.addWidget(self.label_etat_sever)


        self.verticalLayout_4.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.bouton_serveur = QPushButton(self.widget_7)
        self.bouton_serveur.setObjectName(u"bouton_serveur")
        icon = QIcon()
        icon.addFile(u":/icons/icons8-power-off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bouton_serveur.setIcon(icon)
        self.bouton_serveur.setIconSize(QSize(50, 50))

        self.horizontalLayout_6.addWidget(self.bouton_serveur, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_4.addWidget(self.widget_7)


        self.horizontalLayout.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Param\u00e8tre r\u00e9seau", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Etat du r\u00e9seau :", None))
        self.label_etat_reseau.setText(QCoreApplication.translate("Dialog", u"actif", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"port :", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Adress ip :", None))
        self.bouton_reseau.setText(QCoreApplication.translate("Dialog", u"valid\u00e9", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Serveur :", None))
        self.label_etat_sever.setText(QCoreApplication.translate("Dialog", u"eteint", None))
        self.bouton_serveur.setText("")
    # retranslateUi

