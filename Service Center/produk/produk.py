# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Produk.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import pymysql
from produk.select_product import Ui_select_product
from produk.update_product import Ui_update_product
from produk.insert_produk import Ui_Insert_product
from produk.delete_product import Ui_delete_product
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Product(object):
    def cari(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_select_product()
        self.ui.setupUi(self.window)
        self.window.show()

    def insert(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Insert_product()
        self.ui.setupUi(self.window)
        self.window.show()

    def delete(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_delete_product()
        self.ui.setupUi(self.window)
        self.window.show()

    def update(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_update_product()
        self.ui.setupUi(self.window)
        self.window.show()
    def lihat(self):
        db = pymysql.connect("localhost", "root", "", "bingung")
        cur = db.cursor()
        cur.execute("SELECT * FROM product")
        result = cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()
    def setupUi(self, Product):
        Product.setObjectName("Product")
        Product.resize(794, 600)
        Product.setStyleSheet("background-color: rgb(112, 112, 112);")
        self.centralwidget = QtWidgets.QWidget(Product)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_cari = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cari.setGeometry(QtCore.QRect(10, 390, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cari.sizePolicy().hasHeightForWidth())
        self.btn_cari.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_cari.setFont(font)
        self.btn_cari.setStyleSheet("  padding: 15px 25px;\n"
"  font-size: 15px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: rgb(60, 1, 255);\n"
"  background-color: rgb(0, 255, 238);\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;\n"
"hover{color:red}")
        self.btn_cari.setObjectName("btn_cari")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 50, 781, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(781, 0))
        self.line.setMaximumSize(QtCore.QSize(781, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.line.setFont(font)
        self.line.setStyleSheet("  padding: 15px 25px;\n"
"  font-size: 15px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: rgb(60, 1, 255);\n"
"  background-color: rgb(0, 255, 238);\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;\n"
"hover{color:red}")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn_all = QtWidgets.QPushButton(self.centralwidget)
        self.btn_all.setGeometry(QtCore.QRect(340, 340, 111, 23))
        self.btn_all.setStyleSheet("color: rgb(22, 1, 255);\n"
"  background-color: rgb(0, 255, 238);\n"
"")
        self.btn_all.setObjectName("btn_all")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(190, 390, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet("  padding: 15px 25px;\n"
"  font-size: 15px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: rgb(60, 1, 255);\n"
"  background-color: rgb(0, 255, 238);\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;\n"
"hover{color:red}")
        self.btn_delete.setObjectName("btn_delete")
        self.btn_tambah = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tambah.setGeometry(QtCore.QRect(580, 390, 201, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tambah.sizePolicy().hasHeightForWidth())
        self.btn_tambah.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_tambah.setFont(font)
        self.btn_tambah.setStyleSheet("  padding: 15px 25px;\n"
"  font-size: 15px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: rgb(60, 1, 255);\n"
"  background-color: rgb(0, 255, 238);\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;\n"
"hover{color:red}")
        self.btn_tambah.setObjectName("btn_tambah")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 780, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(400, 390, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_update.sizePolicy().hasHeightForWidth())
        self.btn_update.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_update.setFont(font)
        self.btn_update.setStyleSheet("  padding: 15px 25px;\n"
"  font-size: 15px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: rgb(60, 1, 255);\n"
"  background-color: rgb(0, 255, 238);\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;\n"
"hover{color:red}")
        self.btn_update.setObjectName("btn_update")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(200, 70, 411, 261))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        Product.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Product)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 21))
        self.menubar.setObjectName("menubar")
        Product.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Product)
        self.statusbar.setObjectName("statusbar")
        Product.setStatusBar(self.statusbar)

        self.btn_all.clicked.connect(self.lihat)
        self.btn_tambah.clicked.connect(self.insert)
        self.btn_cari.clicked.connect(self.cari)
        self.btn_update.clicked.connect(self.update)
        self.btn_delete.clicked.connect(self.delete)

        self.retranslateUi(Product)
        QtCore.QMetaObject.connectSlotsByName(Product)

    def retranslateUi(self, Product):
        _translate = QtCore.QCoreApplication.translate
        Product.setWindowTitle(_translate("Product", "MainWindow"))
        self.btn_cari.setText(_translate("Product", "Mencari Produk"))
        self.line.setWhatsThis(_translate("Product", "<html><head/><body><p>s</p></body></html>"))
        self.btn_all.setText(_translate("Product", "Lihat Semua Produk"))
        self.btn_delete.setText(_translate("Product", "Menghapus Produk"))
        self.btn_tambah.setText(_translate("Product", "Menambahkan Produk"))
        self.label_3.setText(_translate("Product", "PRODUK"))
        self.label_2.setText(_translate("Product", "Service Center Handphone & Laptop"))
        self.label.setText(_translate("Product", "Hai, Admin"))
        self.btn_update.setText(_translate("Product", "Update Produk"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Product", "kode produk"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Product", "nama produk"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Product", "Spesifikasi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Product", "Tipe"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Product = QtWidgets.QMainWindow()
    ui = Ui_Product()
    ui.setupUi(Product)
    Product.show()
    sys.exit(app.exec_())
