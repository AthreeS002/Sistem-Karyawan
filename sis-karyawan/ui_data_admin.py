# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'data_admin.ui'
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
        MainWindow.resize(800, 488)
        MainWindow.setMinimumSize(QSize(800, 488))
        self.actionImport = QAction(MainWindow)
        self.actionImport.setObjectName(u"actionImport")
        self.actionExport_to_Excel = QAction(MainWindow)
        self.actionExport_to_Excel.setObjectName(u"actionExport_to_Excel")
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 110, 541, 281))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.verticalLayoutWidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)

        self.verticalLayout.addWidget(self.tableWidget)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 10, 331, 81))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(600, 160, 181, 171))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_add = QPushButton(self.verticalLayoutWidget_2)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_add.setFont(font1)

        self.verticalLayout_2.addWidget(self.btn_add)

        self.btn_show = QPushButton(self.verticalLayoutWidget_2)
        self.btn_show.setObjectName(u"btn_show")
        self.btn_show.setMaximumSize(QSize(16777215, 50))
        self.btn_show.setFont(font1)

        self.verticalLayout_2.addWidget(self.btn_show)

        self.btn_exit = QPushButton(self.verticalLayoutWidget_2)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setMaximumSize(QSize(16777215, 50))
        self.btn_exit.setFont(font1)

        self.verticalLayout_2.addWidget(self.btn_exit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuExport = QMenu(self.menuFile)
        self.menuExport.setObjectName(u"menuExport")
        self.menuAction = QMenu(self.menubar)
        self.menuAction.setObjectName(u"menuAction")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAction.menuAction())
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addAction(self.actionImport)
        self.menuExport.addAction(self.actionExport_to_Excel)
        self.menuAction.addAction(self.actionLogout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.actionExport_to_Excel.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"username", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"nama", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"password", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Information Data Admin", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Add or Edit\n"
"Data", None))
        self.btn_show.setText(QCoreApplication.translate("MainWindow", u"Show Data", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuExport.setTitle(QCoreApplication.translate("MainWindow", u"Export", None))
        self.menuAction.setTitle(QCoreApplication.translate("MainWindow", u"Action", None))
    # retranslateUi

