# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader


from PySide6 import QtWidgets, QtGui
import mysql.connector as mc
import xlrd
import pandas as pd
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.btn_login_admin.clicked.connect(self.admin_page)

    def admin_page(self):
        self.create_new_user_window = Ui_admin()
        self.close()
        self.create_new_user_window.show()


class Ui_admin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
            super(self.__class__, self).__init__(parent)
            loader = QUiLoader()
            self.ui = loader.load("admin.ui")
            self.setCentralWidget(self.ui)
            self.ui.btn_login.clicked.connect(self.login_admin)
            self.ui.btn_exit.clicked.connect(self.close)


    def dashboard_admin(self):
        self.create_new_user_window = Ui_dashboard_admin()
        self.create_new_user_window.show()
        self.close()


    def login_admin(self):
        username = self.ui.edit_username.text()
        password = self.ui.edit_password.text()

        db = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="karyawan"
            )
        cursor = db.cursor()

        query = "SELECT * FROM admin WHERE username = %s AND password = %s"
        values = (username, password)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result is not None:
            for i in result:
#                QMessageBox.information(self, "Login successful", "Welcome to the dashboard!")
                self.close()
                self.dashboard_admin()
                break
        else:
            QMessageBox.warning(self, "Login error", "Invalid username or password")


class Ui_dashboard_admin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
            super(self.__class__, self).__init__(parent)
            loader = QUiLoader()
            self.ui = loader.load("dashboard_admin.ui")
            self.setCentralWidget(self.ui)
            self.ui.btn_add.clicked.connect(self.add_karyawan)
            self.ui.btn_show.clicked.connect(self.table_view)

    def add_karyawan(self):
        self.create_new_user_window = Ui_add_karyawan()
        self.create_new_user_window.show()
        self.close()

    def table_view(self):
        try:
            mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="karyawan"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM data")

            result = mycursor.fetchall()
            self.ui.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                print(row_number)
                self.ui.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.ui.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print("Error")


class Ui_add_karyawan(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
            super(self.__class__, self).__init__(parent)
            loader = QUiLoader()
            self.ui = loader.load("add_karyawan.ui")
            self.setCentralWidget(self.ui)

#            self.ui.radio_aktif = QRadioButton("Aktif")
#            self.ui.radio_tidakAktif = QRadioButton("Tidak Aktif")

            self.ui.btn_add.clicked.connect(self.add_karyawan)

    def add_karyawan(self):
        username = self.ui.edit_username.text()
        password = self.ui.edit_password.text()
        nama = self.ui.edit_nama.text()
        gaji = self.ui.edit_gaji.text()
        status = ""
        if self.ui.radio_aktif.isChecked():
            status = "Aktif"
        elif self.ui.radio_tidakAktif.isChecked():
            status = "Tidak Aktif"

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="karyawan"
                )
            mycursor = mydb.cursor()
            sql = "INSERT INTO data (username, password, nama, gaji, status) VALUES (%s, %s, %s, %s, %s)"
            val = (username, password, nama, gaji, status)

            mycursor.execute(sql, val)

            mydb.commit()
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Sukses")
            dlg.setText("Data tersimpan")
            button = dlg.exec()

            if button == QMessageBox.StandardButton.Ok:
                print("OK!")

        except mc.Error as err:
            print("mysql exception: {}".format(err))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
