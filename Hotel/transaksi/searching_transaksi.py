# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searching_transaksi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from datetime import datetime
import sys

class Ui_searching_room(object):
    def search(self):
        db = pymysql.connect("localhost", "root", "", "hotel1")
        cur = db.cursor()
        a = self.lineEdit.text()
        cur.execute("SELECT transaksi.no_transaksi, customer.nama_cs, user.nama, transaksi.tgl_masuk, transaksi.tgl_keluar "
                    "FROM transaksi JOIN customer ON transaksi.id_cs = customer.id_customer "
                    "JOIN user ON transaksi.id_resepsionis = user.id_user WHERE no_transaksi ='"+a+"' ")
        result = cur.fetchall()

        cur.execute("SELECT tgl_masuk, tgl_keluar FROM transaksi WHERE no_transaksi ='" + a + "' ")
        b = cur.fetchall()
        cur.execute("SELECT harga FROM transaksi JOIN kamar ON transaksi.id_kamar = kamar.id_kamar JOIN harga ON kamar.id_harga = harga.id_harga WHERE no_transaksi ='" + a + "' ")
        c = cur.fetchall()
        tgl_masuk = b[0][0]
        tgl_keluar = b[0][1]
        harga = c[0][0]
        tanggal = harga * (tgl_keluar - tgl_masuk).days
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
                self.tableWidget.setItem(row_number, colum_number+1, QtWidgets.QTableWidgetItem(str(tanggal)))
        db.commit()

    def setupUi(self, searching_room):
        searching_room.setObjectName("searching_room")
        searching_room.resize(800, 600)
        searching_room.setStyleSheet("* {\n"
"    background:#F1D1B5;\n"
"}\n"
"\n"
"QFrame {\n"
"    border-radius : 20px;\n"
"    background : rgb(120, 120, 120);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background : transparent;\n"
"    border : none;\n"
"    border-bottom : 1px solid white;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(searching_room)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(300, 0, 251, 80))
        self.frame_2.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 20, 211, 31))
        self.label.setStyleSheet("font: 75 italic 14pt \"Kristen ITC\";\n"
"color : white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(15, 140, 781, 361))
        self.frame.setStyleSheet("QPushButton{\n"
"    background : #305F72;\n"
"    border-radius : 20px;\n"
"    font: 10pt \"Kristen ITC\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: #568EA6;\n"
"}\n"
"background-color: #353b48;\n"
"color:#ffffff;\n"
"border-radius: 20px;\n"
"font-family:century gothic;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(60, 80, 651, 261))
        self.tableWidget.setStyleSheet("background-color:white;\n"
"color:black;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.btn_select = QtWidgets.QPushButton(self.frame)
        self.btn_select.setGeometry(QtCore.QRect(320, 20, 181, 41))
        self.btn_select.setStyleSheet("")
        self.btn_select.setObjectName("btn_select")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(40, 20, 251, 31))
        self.lineEdit.setStyleSheet("border:none;\n"
"border-bottom:1px solid white;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        searching_room.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(searching_room)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        searching_room.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(searching_room)
        self.statusbar.setObjectName("statusbar")
        searching_room.setStatusBar(self.statusbar)

        self.btn_select.clicked.connect(self.search)

        self.retranslateUi(searching_room)
        QtCore.QMetaObject.connectSlotsByName(searching_room)

    def retranslateUi(self, searching_room):
        _translate = QtCore.QCoreApplication.translate
        searching_room.setWindowTitle(_translate("searching_room", "MainWindow"))
        self.label.setText(_translate("searching_room", "Search Transaksi"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("searching_room", "No. Transaksi"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("searching_room", "Nama Customer"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("searching_room", "Nama Resepsionis"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("searching_room", "Tanggal Check-In"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("searching_room", "Tanggal Check-Out"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("searching_room", "Harga"))
        self.btn_select.setText(_translate("searching_room", "Masukkan ID Transaksi"))
        self.lineEdit.setPlaceholderText(_translate("searching_room", "No. Transaksi..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    searching_room = QtWidgets.QMainWindow()
    ui = Ui_searching_room()
    ui.setupUi(searching_room)
    searching_room.show()
    sys.exit(app.exec_())
