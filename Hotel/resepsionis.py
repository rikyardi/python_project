# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resepsionis.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from customer.customer import Ui_customer
from kamar.kamar import Ui_kamar
from transaksi.transaksi import Ui_Transaksi
import pymysql

class Ui_resepsionis(object):
    def transaksi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Transaksi()
        self.ui.setupUi(self.window)
        self.window.show()
    def kamar(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = Ui_kamar()
        self.ui.setupUi(self.window)
        self.window.show()
    def customer(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = Ui_customer()
        self.ui.setupUi(self.window)
        self.window.show()
    def select_all(self):
        db = pymysql.connect("localhost","root","","hotel1")
        cur = db.cursor()
        cur.execute("SELECT transaksi.no_transaksi, customer.nama_cs, transaksi.id_kamar, transaksi.id_resepsionis, transaksi.tgl_masuk, transaksi.tgl_keluar FROM customer, transaksi WHERE transaksi.id_cs = customer.id_customer;")
        result = cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()

    def setupUi(self, resepsionis):
        resepsionis.setObjectName("resepsionis")
        resepsionis.resize(955, 514)
        resepsionis.setStyleSheet("* {\n"
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
        self.centralwidget = QtWidgets.QWidget(resepsionis)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(380, 0, 251, 80))
        self.frame.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 211, 31))
        self.label.setStyleSheet("font: 75 italic 14pt \"Kristen ITC\";\n"
"color : white;")
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(280, 90, 651, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 10pt \"Times New Roman\";\n"
"color : Black;")
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
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
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 100, 221, 301))
        self.frame_2.setStyleSheet("*{\n"
"background-color:rgb(255, 0, 127);\n"
"color:#ffffff;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    background : #305F72;\n"
"    border-radius : 20px;\n"
"    font: 10pt \"Kristen ITC\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: #568EA6;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_customer = QtWidgets.QPushButton(self.frame_2)
        self.btn_customer.setGeometry(QtCore.QRect(10, 20, 201, 61))
        self.btn_customer.setObjectName("btn_customer")
        self.btn_kamar = QtWidgets.QPushButton(self.frame_2)
        self.btn_kamar.setGeometry(QtCore.QRect(10, 120, 201, 61))
        self.btn_kamar.setObjectName("btn_kamar")
        self.btn_transaksi = QtWidgets.QPushButton(self.frame_2)
        self.btn_transaksi.setGeometry(QtCore.QRect(10, 220, 201, 61))
        self.btn_transaksi.setObjectName("btn_transaksi")
        self.btn_all = QtWidgets.QPushButton(self.centralwidget)
        self.btn_all.setGeometry(QtCore.QRect(440, 410, 181, 41))
        self.btn_all.setStyleSheet("QPushButton{\n"
"    background : #305F72;\n"
"    border-radius : 20px;\n"
"    font: 10pt \"Kristen ITC\";\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background: #568EA6;\n"
"}\n"
"")
        self.btn_all.setObjectName("btn_all")
        resepsionis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(resepsionis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 955, 21))
        self.menubar.setObjectName("menubar")
        resepsionis.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(resepsionis)
        self.statusbar.setObjectName("statusbar")
        resepsionis.setStatusBar(self.statusbar)

        self.btn_all.clicked.connect(self.select_all)
        self.btn_customer.clicked.connect(self.customer)
        self.btn_kamar.clicked.connect(self.kamar)
        self.btn_transaksi.clicked.connect(self.transaksi)

        self.retranslateUi(resepsionis)
        QtCore.QMetaObject.connectSlotsByName(resepsionis)

    def retranslateUi(self, resepsionis):
        _translate = QtCore.QCoreApplication.translate
        resepsionis.setWindowTitle(_translate("resepsionis", "MainWindow"))
        self.label.setText(_translate("resepsionis", "HOTEL SUKAMAJU"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("resepsionis", "Nomor Transaksi"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("resepsionis", "Nama Customer"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("resepsionis", "ID Kamar"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("resepsionis", "ID Resepsionis"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("resepsionis", "Tgl Check-In"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("resepsionis", "Tgl Check-Out"))
        self.btn_customer.setText(_translate("resepsionis", "Customer"))
        self.btn_kamar.setText(_translate("resepsionis", "Kamar"))
        self.btn_transaksi.setText(_translate("resepsionis", "Transaksi"))
        self.label_14.setText(_translate("transaksi", "Resepsionis"))
        self.btn_all.setText(_translate("resepsionis", "Lihat Semua Transaksi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    resepsionis = QtWidgets.QMainWindow()
    ui = Ui_resepsionis()
    ui.setupUi(resepsionis)
    resepsionis.show()
    sys.exit(app.exec_())
