# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_karyawan.ui'
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
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(70, 150, 411, 191))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.edit_password = QLineEdit(self.verticalLayoutWidget)
        self.edit_password.setObjectName(u"edit_password")
        self.edit_password.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.edit_password)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.edit_nama = QLineEdit(self.verticalLayoutWidget)
        self.edit_nama.setObjectName(u"edit_nama")
        self.edit_nama.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.edit_nama)

        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.edit_alamat = QLineEdit(self.verticalLayoutWidget)
        self.edit_alamat.setObjectName(u"edit_alamat")
        self.edit_alamat.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.edit_alamat)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(530, 180, 160, 171))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_update = QPushButton(self.verticalLayoutWidget_2)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(12)
        self.btn_update.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_update)

        self.btn_cancel = QPushButton(self.verticalLayoutWidget_2)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMaximumSize(QSize(16777215, 50))
        self.btn_cancel.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_cancel)

        self.btn_exit = QPushButton(self.verticalLayoutWidget_2)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMaximumSize(QSize(16777215, 50))
        self.btn_exit.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_exit)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(310, 50, 201, 31))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_3.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nama Karyawan", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Alamat", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"Edit Data", None))
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ubah Data Anda", None))
    # retranslateUi

