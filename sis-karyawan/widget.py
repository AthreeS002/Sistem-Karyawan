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
        self.ui.btn_edit.clicked.connect(self.edit_page)
        self.ui.btn_exit.clicked.connect(self.close)

        self.ui.actionLogout.triggered.connect(self.logout)

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
            val = (username,)
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

    def edit_page(self, username):
        username = self.username
        self.create_new_user_window = Ui_edit_karyawan(self, username)
#        self.create_new_user_window.username = username
        self.create_new_user_window.show()
        self.close()

    def logout(self):
        self.create_new_user_window = Widget()
        self.close()
        self.create_new_user_window.show()

#class edit karyawan
class Ui_edit_karyawan(QtWidgets.QMainWindow):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
#        super(self.__class__, self).__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("edit_karyawan.ui")
        self.setCentralWidget(self.ui)

        self.ui.btn_update.clicked.connect(self.update_data)
        self.ui.btn_cancel.clicked.connect(self.cancel)
        self.ui.btn_exit.clicked.connect(self.close)
        self.username = username

        self.ui.actionLogout.triggered.connect(self.logout)

    def update_data(self, username):
        username = self.username
        password = self.ui.edit_password.text()
        nama = self.ui.edit_nama.text()
        alamat= self.ui.edit_alamat.text()

        try:
            mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="karyawan"
            )
            mycursor = mydb.cursor()
            sql = """UPDATE data SET password = %s, nama = %s, alamat = %s WHERE username = %s"""
            val = (password, nama, alamat, username)

            mycursor.execute(sql, val)

            mydb.commit()
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Sukses")
            dlg.setText("Update Data sukses")
            button = dlg.exec()

            if button == QMessageBox.StandardButton.Ok:
                print("OK!")

        except mc.Error as err:
            print("mysql exception: {}".format(err))

    def logout(self):
        self.create_new_user_window = Widget()
        self.close()
        self.create_new_user_window.show()

    def cancel(self):
#        username = self.username
        self.create_new_user_window = Ui_dashboard_karyawan(self)
        self.create_new_user_window.username = self.username
        self.create_new_user_window.show()
        self.close()

#class tampilan login admin
class Ui_admin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("admin.ui")
        self.setCentralWidget(self.ui)
        self.ui.btn_login.clicked.connect(self.login_admin)
        self.ui.btn_cancel.clicked.connect(self.cancel)
        self.ui.btn_exit.clicked.connect(self.close)


    def dashboard_admin(self):
        self.create_new_user_window = Ui_dashboard_admin()
        self.create_new_user_window.show()
        self.close()

    def cancel(self):
        self.create_new_user_window = Widget()
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
            self.ui.btn_admin.clicked.connect(self.admin)
            self.ui.btn_karyawan.clicked.connect(self.karyawan)
            self.ui.actionLogout.triggered.connect(self.logout)


    def admin(self):
        self.create_new_user_window = Ui_data_admin()
        self.create_new_user_window.show()
        self.close()

    def karyawan(self):
        self.create_new_user_window = Ui_data_karyawan()
        self.create_new_user_window.show()
        self.close()

    def logout(self):
        self.create_new_user_window = Widget()
        self.close()
        self.create_new_user_window.show()

class Ui_data_admin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("data_admin.ui")
        self.setCentralWidget(self.ui)
        self.ui.btn_add.clicked.connect(self.add_admin)
        self.ui.btn_show.clicked.connect(self.table_view)

    def add_admin(self):
        self.create_new_user_window = Ui_add_admin()
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
            mycursor.execute("SELECT * FROM admin")

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

class Ui_data_karyawan(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
            super(self.__class__, self).__init__(parent)
            loader = QUiLoader()
            self.ui = loader.load("data_karyawan.ui")
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

class Ui_add_admin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("add_admin.ui")
        self.setCentralWidget(self.ui)

        self.ui.btn_add.clicked.connect(self.add_karyawan)

    def add_karyawan(self):
        username = self.ui.edit_username.text()
        nama = self.ui.edit_nama.text()
        password = self.ui.edit_password.text()

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="karyawan"
                )
            mycursor = mydb.cursor()
            sql = "INSERT INTO admin (username, nama, password) VALUES (%s, %s, %s)"
            val = (username, nama, password)

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
