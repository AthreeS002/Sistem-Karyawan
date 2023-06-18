# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'karyawan.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 30, 201, 41))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(80, 120, 321, 281))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.verticalLayoutWidget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(1)

        self.verticalLayout.addWidget(self.tableWidget)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(560, 140, 181, 201))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_show = QPushButton(self.verticalLayoutWidget_2)
        self.btn_show.setObjectName(u"btn_show")
        self.btn_show.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_show.setFont(font1)

        self.verticalLayout_2.addWidget(self.btn_show)

        self.btn_edit = QPushButton(self.verticalLayoutWidget_2)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setMaximumSize(QSize(16777215, 50))
        self.btn_edit.setFont(font1)

        self.verticalLayout_2.addWidget(self.btn_edit)

        self.pushButton = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(16777215, 50))
        self.pushButton.setFont(font1)

        self.verticalLayout_2.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuAction = QMenu(self.menubar)
        self.menuAction.setObjectName(u"menuAction")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAction.menuAction())
        self.menuAction.addAction(self.actionLogout)
        self.menuAction.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Information Data", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem1 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nama", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Gaji", None));
        self.btn_show.setText(QCoreApplication.translate("MainWindow", u"Show Data", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Edit Data", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menuAction.setTitle(QCoreApplication.translate("MainWindow", u"Action", None))
    # retranslateUi

