# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(642, 377)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 31, 141, 41))
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        self.label.setFont(font)
        self.verticalLayoutWidget = QWidget(Widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 120, 351, 61))
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

        self.verticalLayoutWidget_2 = QWidget(Widget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(60, 201, 351, 61))
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

        self.verticalLayoutWidget_3 = QWidget(Widget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(450, 120, 160, 141))
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

        self.btn_exit = QPushButton(self.verticalLayoutWidget_3)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMaximumSize(QSize(16777215, 50))
        self.btn_exit.setFont(font1)

        self.verticalLayout_3.addWidget(self.btn_exit)

        self.verticalLayoutWidget_4 = QWidget(Widget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(60, 320, 551, 31))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_login_admin = QPushButton(self.verticalLayoutWidget_4)
        self.btn_login_admin.setObjectName(u"btn_login_admin")

        self.verticalLayout_4.addWidget(self.btn_login_admin)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Login Page", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Username", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Password", None))
        self.btn_login.setText(QCoreApplication.translate("Widget", u"Login", None))
        self.btn_exit.setText(QCoreApplication.translate("Widget", u"Exit", None))
        self.btn_login_admin.setText(QCoreApplication.translate("Widget", u"Login as Administrator", None))
    # retranslateUi

