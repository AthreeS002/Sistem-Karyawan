# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editpage_admin2.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(660, 398)
        MainWindow.setMinimumSize(QSize(660, 398))
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 30, 221, 41))
        font = QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(480, 130, 160, 171))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_update = QPushButton(self.verticalLayoutWidget_2)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_update.setFont(font1)

        self.verticalLayout_2.addWidget(self.btn_update)

        self.btn_cancel = QPushButton(self.verticalLayoutWidget_2)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMaximumSize(QSize(16777215, 50))
        self.btn_cancel.setFont(font1)

        self.verticalLayout_2.addWidget(self.btn_cancel)

        self.btn_exit = QPushButton(self.verticalLayoutWidget_2)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMaximumSize(QSize(16777215, 50))
        self.btn_exit.setFont(font1)

        self.verticalLayout_2.addWidget(self.btn_exit)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 110, 411, 191))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.edit_username = QLineEdit(self.verticalLayoutWidget)
        self.edit_username.setObjectName(u"edit_username")
        self.edit_username.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.edit_username)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.edit_nama = QLineEdit(self.verticalLayoutWidget)
        self.edit_nama.setObjectName(u"edit_nama")
        self.edit_nama.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.edit_nama)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.edit_password = QLineEdit(self.verticalLayoutWidget)
        self.edit_password.setObjectName(u"edit_password")
        self.edit_password.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.edit_password)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 660, 21))
        self.menuAction = QMenu(self.menubar)
        self.menuAction.setObjectName(u"menuAction")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAction.menuAction())
        self.menuAction.addAction(self.actionLogout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Halaman Edit Admin", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"Edit Data", None))
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nama Admin", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.menuAction.setTitle(QCoreApplication.translate("MainWindow", u"Action", None))
    # retranslateUi

