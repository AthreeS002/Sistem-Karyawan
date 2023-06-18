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

#kelas utama (tampilan awal)
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.btn_login.clicked.connect(self.login_karyawan)
        self.ui.btn_login_admin.clicked.connect(self.admin_page)

    #login sebagai karyawan
    def login_karyawan(self):
        username = self.ui.edit_username.text()
        password = self.ui.edit_password.text()

        db = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="karyawan"
            )
        cursor = db.cursor()

        query = "SELECT * FROM data WHERE username = %s AND password = %s"
        values = (username, password)
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result is not None:
            self.close()
            self.dashboard_karyawan(username)

        else:
            QMessageBox.warning(self, "Login error", "Invalid username or password")

    #tampil dashboard karyawan
    def dashboard_karyawan(self, username):
        self.create_new_user_window = Ui_dashboard_karyawan(self)
        self.create_new_user_window.username = username
        self.create_new_user_window.show()
        self.close()

    #tampil login page untuk admin
    def admin_page(self):
        self.create_new_user_window = Ui_admin()
        self.close()
        self.create_new_user_window.show()

#class dashboard karyawan
class Ui_dashboard_karyawan(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("dashboard_karyawan.ui")
        self.setCentralWidget(self.ui)
#        self.username = username

        self.ui.btn_show.clicked.connect(self.show_data)

    def show_data(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="karyawan"
            )
            mycursor = mydb.cursor()

            username = self.username
            sql = "SELECT username, nama, gaji, alamat, status FROM data WHERE username = %s"
            val = (self.username,)
            mycursor.execute(sql, val)

            result = mycursor.fetchall()
            num_rows = len(result)
            num_columns = len(result[0])

            self.ui.tableWidget.setRowCount(num_rows)
            self.ui.tableWidget.setColumnCount(num_columns)
            self.ui.tableWidget.setHorizontalHeaderLabels(['Username', 'Nama', 'Gaji', 'Alamat', 'Status'])
            for row_number, row_data in enumerate(result):
               for column_number, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    self.ui.tableWidget.setItem(row_number, column_number, item)

        except mc.Error as e:
            print("Error")


#class tampilan login admin
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

#class tampilan dashboard dari admin
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
            self.ui.btn_update.clicked.connect(self.edit_karyawan)

    def add_karyawan(self):
        username = self.ui.edit_username.text()
        password = self.ui.edit_password.text()
        nama = self.ui.edit_nama.text()
        gaji = self.ui.edit_gaji.text()
        alamat = self.ui.edit_alamat.text()
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
            sql = "INSERT INTO data (username, password, nama, gaji, alamat, status) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (username, password, nama, gaji, alamat, status)

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

    def edit_karyawan(self):
        username = self.ui.edit_username.text()
        password = self.ui.edit_password.text()
        nama = self.ui.edit_nama.text()
        gaji = self.ui.edit_gaji.text()
        alamat = self.ui.edit_alamat.text()
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
            sql = """UPDATE data SET username = %s, password = %s, nama = %s, gaji = %s, alamat = %s, status = %s WHERE username = %s"""
            val = (username, password, nama, gaji, alamat, status, username)

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
