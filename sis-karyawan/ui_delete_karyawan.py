# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete_karyawan.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(652, 143)
        Form.setMinimumSize(QSize(652, 143))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 20, 311, 31))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(50, 70, 561, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.edit_id = QLineEdit(self.horizontalLayoutWidget)
        self.edit_id.setObjectName(u"edit_id")

        self.horizontalLayout.addWidget(self.edit_id)

        self.btn_delete = QPushButton(self.horizontalLayoutWidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setMaximumSize(QSize(70, 40))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_delete.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_delete)

        self.btn_cancel = QPushButton(self.horizontalLayoutWidget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMaximumSize(QSize(60, 40))
        self.btn_cancel.setFont(font1)

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Input Karyawan ID to Delete", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"ID Karyawan:", None))
        self.btn_delete.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.btn_cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi

