# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(710, 371)
        MainWindow.setMinimumSize(QSize(700, 300))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(100, 120, 351, 61))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.edit_username = QLineEdit(self.verticalLayoutWidget)
        self.edit_username.setObjectName(u"edit_username")
        self.edit_username.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.edit_username)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(100, 201, 351, 61))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.edit_password = QLineEdit(self.verticalLayoutWidget_2)
        self.edit_password.setObjectName(u"edit_password")
        self.edit_password.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_2.addWidget(self.edit_password)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 30, 271, 41))
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        self.label.setFont(font)
        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(490, 120, 160, 151))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_login = QPushButton(self.verticalLayoutWidget_3)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_login.setFont(font1)

        self.verticalLayout_3.addWidget(self.btn_login)

        self.btn_cancel = QPushButton(self.verticalLayoutWidget_3)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMaximumSize(QSize(16777215, 50))
        self.btn_cancel.setFont(font1)

        self.verticalLayout_3.addWidget(self.btn_cancel)

        self.btn_exit = QPushButton(self.verticalLayoutWidget_3)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMaximumSize(QSize(16777215, 50))
        self.btn_exit.setFont(font1)

        self.verticalLayout_3.addWidget(self.btn_exit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 710, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login as Administrator", None))
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

