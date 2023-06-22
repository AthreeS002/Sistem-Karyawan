# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader

#import package to export PDF
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

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
        self.ui.btn_exit.clicked.connect(self.close)

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

        self.ui.actionExport_to_Excel.triggered.connect(self.export_data)
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

    def export_data(self):
            # Konek ke Basis Data
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="karyawan"
                )
            mycursor = mydb.cursor()
            username = self.username
            sql = "SELECT * FROM data WHERE username = %s"
            val = (username,)
            mycursor.execute(sql, val)
            # Fetch all results
            rows = mycursor.fetchall()

            # Convert the result to a Pandas DataFrame
            df = pd.DataFrame(rows)
            col_names= ["ID", "Username", "Password", "Nama", "Gaji", "Alamat", "Status"]
            df.columns = col_names
            # Write the DataFrame to an Excel file
            df.to_excel('data_anda.xlsx', index=False)

            # Close the cursor and connection
            mycursor.close()
            mydb.close()

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
        self.ui.btn_delete.clicked.connect(self.delete_data)

        self.ui.actionImport.triggered.connect(self.import_data)
        self.ui.actionExport_to_Excel.triggered.connect(self.export_data)
        self.ui.actionExport_to_PDF.triggered.connect(self.export_to_pdf)

        self.ui.actionLogout.triggered.connect(self.logout)
        self.ui.btn_exit.clicked.connect(self.exit)

    def add_admin(self):
        self.create_new_user_window = Ui_add_admin()
        self.create_new_user_window.show()
        self.close()

    #Import dari excel
    def import_data(self):
        book = xlrd.open_workbook("import_admin.xlsx")
        sheet = book.sheet_by_name("admin")

        # Konek ke Basis Data
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="karyawan"
            )
        mycursor = mydb.cursor()
        sql = """INSERT INTO admin (id, username, nama, password) VALUES (NULL, %s, %s, %s)"""
        # Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
        for r in range(1, sheet.nrows):
            username       = sheet.cell(r,1).value
            nama           = sheet.cell(r,2).value
            password       = sheet.cell(r,3).value
            # Assign values from each row
            val = (username, nama, password)

            # Execute sql Query
            mycursor.execute(sql, val,)
            mydb.commit()
        # Close the cursor
        mycursor.close()

        # Commit the transaction
        mydb.commit()

        # Close the database connection
        mydb.close()

    def export_data(self):
        # Konek ke Basis Data
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="karyawan"
            )
        mycursor = mydb.cursor()
                #        nis = self.txt_nis.text()
        sql = "SELECT * FROM admin"
            #        val = (nis,)
        mycursor.execute(sql,)
        # Fetch all results
        rows = mycursor.fetchall()

        # Convert the result to a Pandas DataFrame
        df = pd.DataFrame(rows)
        col_names= ["ID", "Username", "Nama", "Password"]
        df.columns = col_names
        # Write the DataFrame to an Excel file
        df.to_excel('data_admin.xlsx', index=False)

        # Close the cursor and connection
        mycursor.close()
        mydb.close()

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

    def export_to_pdf(self):
            try:
                # Menghubungkan ke database
                mydb = mc.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="karyawan"
                )
                mycursor = mydb.cursor()

                # Mengambil data dari database
                query = "SELECT id, username, nama FROM admin"
                mycursor.execute(query)
                result = mycursor.fetchall()

                # Membuat dokumen PDF baru
                doc = SimpleDocTemplate("data_admin.pdf", pagesize=letter)

                # Menginisialisasi tabel
                table_data = [["ID", "Username", "Nama"]]
                table_data.extend(result)

                # Mengatur gaya tabel
                table = Table(table_data)
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 12),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                    ('FONTSIZE', (0, 1), (-1, -1), 10),
                    ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
                ]))

                # Menambahkan tabel ke dokumen PDF
                elements = []
                elements.append(table)

                # Membuat dokumen PDF
                doc.build(elements)

                print("Export to PDF berhasil")

            except mc.Error as e:
                print("mysql exception: {}".format(e))

    def delete_data(self):
        self.create_new_user_window = Ui_delete_admin()
        self.create_new_user_window.show()

    def exit(self):
        self.create_new_user_window = Ui_dashboard_admin()
        self.create_new_user_window.show()
        self.close()

    def logout(self):
        self.create_new_user_window = Widget()
        self.close()
        self.create_new_user_window.show()

class Ui_data_karyawan(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
            super(self.__class__, self).__init__(parent)
            loader = QUiLoader()
            self.ui = loader.load("data_karyawan.ui")
            self.setCentralWidget(self.ui)

            self.ui.btn_add.clicked.connect(self.add_karyawan)
            self.ui.btn_show.clicked.connect(self.table_view)
            self.ui.btn_delete.clicked.connect(self.delete_karyawan)
            self.ui.btn_exit.clicked.connect(self.exit)

            self.ui.actionLogout_2.triggered.connect(self.logout)
            self.ui.actionImport.triggered.connect(self.import_data)
            self.ui.actionExport_to_Excel.triggered.connect(self.export_data)
            self.ui.actionExport_to_PDF.triggered.connect(self.export_to_pdf)

    def exit(self):
        self.create_new_user_window = Ui_dashboard_admin()
        self.create_new_user_window.show()
        self.close()

    def add_karyawan(self):
        self.create_new_user_window = Ui_add_karyawan()
        self.create_new_user_window.show()
        self.close()

    def delete_karyawan(self):
        self.create_new_user_window = Ui_delete_karyawan()
        self.create_new_user_window.show()

    def logout(self):
        self.create_new_user_window = Widget()
        self.close()
        self.create_new_user_window.show()

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

    #Import dari excel
    def import_data(self):
        book = xlrd.open_workbook("import_karyawan.xlsx")
        sheet = book.sheet_by_name("karyawan")

        # Konek ke Basis Data
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="karyawan"
            )
        mycursor = mydb.cursor()
        sql = """INSERT INTO data (id, username, password, nama, gaji, alamat, status) VALUES (NULL, %s, %s, %s, %s, %s, %s)"""
        # Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
        for r in range(1, sheet.nrows):
            username       = sheet.cell(r,1).value
            password       = sheet.cell(r,2).value
            nama           = sheet.cell(r,3).value
            gaji           = sheet.cell(r,4).value
            alamat         = sheet.cell(r,5).value
            status         = sheet.cell(r,6).value

            # Assign values from each row
            val = (username, password, nama, gaji, alamat, status)

            # Execute sql Query
            mycursor.execute(sql, val,)
            mydb.commit()
        # Close the cursor
        mycursor.close()

        # Commit the transaction
        mydb.commit()

        # Close the database connection
        mydb.close()

    def export_data(self):
        # Konek ke Basis Data
        mydb = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="karyawan"
            )
        mycursor = mydb.cursor()
#        nis = self.txt_nis.text()
        sql = "SELECT * FROM data"
#        val = (nis,)
        mycursor.execute(sql,)
        # Fetch all results
        rows = mycursor.fetchall()

        # Convert the result to a Pandas DataFrame
        df = pd.DataFrame(rows)
        col_names= ["ID", "Username", "Password", "Nama", "Gaji", "Alamat", "Status"]
        df.columns = col_names
        # Write the DataFrame to an Excel file
        df.to_excel('data_karyawan.xlsx', index=False)

        # Close the cursor and connection
        mycursor.close()
        mydb.close()

    def export_to_pdf(self):
        try:
            # Menghubungkan ke database
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="karyawan"
            )
            mycursor = mydb.cursor()

            # Mengambil data dari database
            query = "SELECT id, username, nama, gaji, alamat, status FROM data"
            mycursor.execute(query)
            result = mycursor.fetchall()

            # Membuat dokumen PDF baru
            doc = SimpleDocTemplate("data_karyawan.pdf", pagesize=letter)

            # Menginisialisasi tabel
            table_data = [["ID", "Username", "Nama", "Gaji", "Alamat", "Status"]]
            table_data.extend(result)

            # Mengatur gaya tabel
            table = Table(table_data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 10),
                ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
            ]))

            # Menambahkan tabel ke dokumen PDF
            elements = []
            elements.append(table)

            # Membuat dokumen PDF
            doc.build(elements)

            print("Export to PDF berhasil")

        except mc.Error as e:
            print("mysql exception: {}".format(e))


class Ui_add_admin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("add_admin.ui")
        self.setCentralWidget(self.ui)

        self.ui.btn_edit.clicked.connect(self.edit_admin)
        self.ui.btn_cancel.clicked.connect(self.cancel)
        self.ui.actionLogout.triggered.connect(self.logout)
        self.ui.btn_add.clicked.connect(self.add_admin)

    def add_admin(self):
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

    def edit_admin(self):
        self.create_new_user_window = Ui_edit_admin1()
        self.create_new_user_window.show()
        self.close()

    def cancel(self):
        self.create_new_user_window = Ui_data_admin()
        self.create_new_user_window.show()
        self.close()

    def logout(self):
        self.create_new_user_window = Widget()
        self.close()
        self.create_new_user_window.show()


class Ui_add_karyawan(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
            super(self.__class__, self).__init__(parent)
            loader = QUiLoader()
            self.ui = loader.load("add_karyawan.ui")
            self.setCentralWidget(self.ui)

#            self.ui.radio_aktif = QRadioButton("Aktif")
#            self.ui.radio_tidakAktif = QRadioButton("Tidak Aktif")

            self.ui.btn_add.clicked.connect(self.add_karyawan)
            self.ui.btn_update.clicked.connect(self.edit_page1)

            self.ui.actionLogout.triggered.connect(self.logout)
            self.ui.btn_exit.clicked.connect(self.close)

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
            sql = "INSERT INTO data (id, username, password, nama, gaji, alamat, status) VALUES (NULL, %s, %s, %s, %s, %s, %s)"
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

#    def edit_karyawan(self):
#        username = self.ui.edit_username.text()
#        password = self.ui.edit_password.text()
#        nama = self.ui.edit_nama.text()
#        gaji = self.ui.edit_gaji.text()
#        alamat = self.ui.edit_alamat.text()
#        status = ""
#        if self.ui.radio_aktif.isChecked():
#            status = "Aktif"
#        elif self.ui.radio_tidakAktif.isChecked():
#            status = "Tidak Aktif"

#        try:
#            mydb = mc.connect(
#                host="localhost",
#                user="root",
#                password="",
#                database="karyawan"
#                )
#            mycursor = mydb.cursor()
#            sql = """UPDATE data SET username = %s, password = %s, nama = %s, gaji = %s, alamat = %s, status = %s WHERE username = %s"""
#            val = (username, password, nama, gaji, alamat, status, username)

#            mycursor.execute(sql, val)

#            mydb.commit()
#            dlg = QMessageBox(self)
#            dlg.setWindowTitle("Sukses")
#            dlg.setText("Data tersimpan")
#            button = dlg.exec()

#            if button == QMessageBox.StandardButton.Ok:
#                print("OK!")

#        except mc.Error as err:
#            print("mysql exception: {}".format(err))

    def edit_page1(self):
        self.create_new_user_window = Ui_edit_karyawan1()
        self.close()
        self.create_new_user_window.show()

    def logout(self):
        self.create_new_user_window = Widget()
        self.close()
        self.create_new_user_window.show()

class Ui_edit_karyawan1(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("editpage_karyawan1.ui")
        self.setCentralWidget(self.ui)
        self.ui.btn_edit.clicked.connect(self.id)
        self.ui.btn_cancel.clicked.connect(self.cancel)

    def id(self):
        id = self.ui.edit_id.text()

        db = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="karyawan"
            )
        cursor = db.cursor()

        query = "SELECT * FROM data WHERE id = %s"
        val = (id,)
        cursor.execute(query, val)
        result = cursor.fetchone()

        if result is not None:
            self.close()
            self.next(id)

        else:
            QMessageBox.warning(self, "Error!", "Not found the ID")

    def next(self, id):
        self.create_new_user_window = Ui_edit_karyawan2(self)
        self.create_new_user_window.id = id
        self.create_new_user_window.show()
        self.close()

    def cancel(self):
        self.create_new_user_window = Ui_add_karyawan()
        self.close()
        self.create_new_user_window.show()


class Ui_edit_karyawan2(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("editpage_karyawan2.ui")
        self.setCentralWidget(self.ui)

        self.ui.btn_update.clicked.connect(self.update_data)
        self.ui.actionLogout.triggered.connect(self.logout)
        self.ui.btn_cancel.clicked.connect(self.cancel)
        self.ui.btn_exit.clicked.connect(self.close)

    def update_data(self, id):
        id = self.id
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
            sql = """UPDATE data SET username = %s, password = %s, nama = %s, gaji = %s, alamat = %s, status = %s WHERE id= %s"""
            val = (username, password, nama, gaji, alamat, status, id)

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

    def cancel(self):
        self.create_new_user_window = Ui_data_karyawan()
        self.create_new_user_window.show()
        self.close()

    def logout(self):
        self.create_new_user_window = Widget()
        self.close()
        self.create_new_user_window.show()


class Ui_edit_admin1(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("editpage_admin1.ui")
        self.setCentralWidget(self.ui)

        self.ui.btn_edit.clicked.connect(self.id)
        self.ui.btn_cancel.clicked.connect(self.cancel)

    def id(self):
        id = self.ui.edit_id.text()

        db = mc.connect(
            host="localhost",
            user="root",
            password="",
            database="karyawan"
            )
        cursor = db.cursor()

        query = "SELECT * FROM admin WHERE id = %s"
        val = (id,)
        cursor.execute(query, val)
        result = cursor.fetchone()

        if result is not None:
            self.close()
            self.next(id)

        else:
            QMessageBox.warning(self, "Error!", "Not found the ID")

    def next(self, id):
        self.create_new_user_window = Ui_edit_admin2(self)
        self.create_new_user_window.id = id
        self.create_new_user_window.show()
        self.close()

    def cancel(self):
        self.create_new_user_window = Ui_add_admin()
        self.close()
        self.create_new_user_window.show()


class Ui_edit_admin2(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("editpage_admin2.ui")
        self.setCentralWidget(self.ui)

        self.ui.btn_update.clicked.connect(self.update_data)
        self.ui.actionLogout.triggered.connect(self.logout)
        self.ui.btn_cancel.clicked.connect(self.cancel)
        self.ui.btn_exit.clicked.connect(self.close)

    def update_data(self, username):
        id = self.id
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
            sql = """UPDATE admin SET username = %s, nama = %s, password = %s WHERE id= %s"""
            val = (username, nama, password, id)

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

    def cancel(self):
        self.create_new_user_window = Ui_data_admin()
        self.create_new_user_window.show()
        self.close()

    def logout(self):
        self.create_new_user_window = Widget()
        self.close()
        self.create_new_user_window.show()

class Ui_delete_karyawan(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("delete_karyawan.ui")
        self.setCentralWidget(self.ui)

        self.ui.btn_delete.clicked.connect(self.delete_data)
        self.ui.btn_cancel.clicked.connect(self.close)

    def delete_data(self):
        id = self.ui.edit_id.text()

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="karyawan"
                )
            mycursor = mydb.cursor()
            sql = """DELETE FROM data where id = %s"""
            val = (id,)

            mycursor.execute(sql, val)

            mydb.commit()
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Sukses")
            dlg.setText("Hapus Data sukses")
            button = dlg.exec()

            if button == QMessageBox.StandardButton.Ok:
                print("OK!")

        except mc.Error as err:
            print("mysql exception: {}".format(err))

class Ui_delete_admin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("delete_admin.ui")
        self.setCentralWidget(self.ui)

        self.ui.btn_delete.clicked.connect(self.delete_data)
        self.ui.btn_cancel.clicked.connect(self.close)

    def delete_data(self):
        id = self.ui.edit_id.text()

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="karyawan"
                )
            mycursor = mydb.cursor()
            sql = """DELETE FROM admin where id = %s"""
            val = (id,)

            mycursor.execute(sql, val)

            mydb.commit()
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Sukses")
            dlg.setText("Hapus Data sukses")
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
