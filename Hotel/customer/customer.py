# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from customer.update_customer import Ui_update_customer
from customer.searching_customer import Ui_searching_customer
import pymysql

class Ui_customer(object):
    def search(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_searching_customer()
        self.ui.setupUi(self.window)
        self.window.show()
    def update(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_update_customer()
        self.ui.setupUi(self.window)
        self.window.show()
    def select_all(self):
        db = pymysql.connect("localhost", "root", "", "hotel1")
        cur = db.cursor()
        cur.execute("SELECT id_customer, nama_cs, alamat_cs, no_telp_cs FROM customer")
        result = cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()

    def setupUi(self, customer):
        customer.setObjectName("customer")
        customer.resize(800, 600)
        customer.setStyleSheet("* {\n"
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
        self.centralwidget = QtWidgets.QWidget(customer)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(240, 0, 251, 80))
        self.frame.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 211, 31))
        self.label.setStyleSheet("font: 75 italic 14pt \"Kristen ITC\";\n"
"color : white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(160, 110, 421, 311))
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
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.btn_all = QtWidgets.QPushButton(self.centralwidget)
        self.btn_all.setGeometry(QtCore.QRect(610, 220, 181, 41))
        self.btn_all.setStyleSheet("QPushButton{\n"
"    background : rgb(85, 0, 0);\n"
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
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(160, 450, 181, 41))
        self.btn_update.setStyleSheet("QPushButton{\n"
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
        self.btn_update.setObjectName("btn_update")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(410, 450, 181, 41))
        self.btn_search.setStyleSheet("QPushButton{\n"
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
        self.btn_search.setObjectName("btn_search")
        customer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(customer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        customer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(customer)
        self.statusbar.setObjectName("statusbar")
        customer.setStatusBar(self.statusbar)

        self.btn_all.clicked.connect(self.select_all)
        self.btn_update.clicked.connect(self.update)
        self.btn_search.clicked.connect(self.search)

        self.retranslateUi(customer)
        QtCore.QMetaObject.connectSlotsByName(customer)

    def retranslateUi(self, customer):
        _translate = QtCore.QCoreApplication.translate
        customer.setWindowTitle(_translate("customer", "MainWindow"))
        self.label.setText(_translate("customer", "Customer"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("customer", "ID Customer"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("customer", "Nama Customer"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("customer", "Alamat"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("customer", "Telpon"))
        self.btn_all.setText(_translate("customer", "Lihat Semua Customer"))
        self.btn_update.setText(_translate("customer", "Update Customer"))
        self.btn_search.setText(_translate("customer", "Searching Customer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    customer = QtWidgets.QMainWindow()
    ui = Ui_customer()
    ui.setupUi(customer)
    customer.show()
    sys.exit(app.exec_())
