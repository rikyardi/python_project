# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searching_customer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_searching_customer(object):
    def select(self):
        db = pymysql.connect("localhost", "root", "", "hotel1")
        cur = db.cursor()
        a = self.lineEdit.text()
        cur.execute("SELECT id_customer, nama_cs, alamat_cs, no_telp_cs FROM customer WHERE id_customer='" + a + "'")
        result = cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        db.commit()

    def setupUi(self, searching_customer):
        searching_customer.setObjectName("searching_customer")
        searching_customer.resize(800, 678)
        searching_customer.setStyleSheet("* {\n"
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
        self.centralwidget = QtWidgets.QWidget(searching_customer)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(130, 150, 551, 361))
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
        self.tableWidget.setGeometry(QtCore.QRect(70, 80, 431, 261))
        self.tableWidget.setStyleSheet("background-color:white;\n"
"color:black;")
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
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(270, 10, 251, 80))
        self.frame_2.setStyleSheet("background-color: rgb(255, 0, 127);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 20, 211, 31))
        self.label.setStyleSheet("font: 75 italic 14pt \"Kristen ITC\";\n"
"color : white;")
        self.label.setObjectName("label")
        searching_customer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(searching_customer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        searching_customer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(searching_customer)
        self.statusbar.setObjectName("statusbar")
        searching_customer.setStatusBar(self.statusbar)

        self.btn_select.clicked.connect(self.select)

        self.retranslateUi(searching_customer)
        QtCore.QMetaObject.connectSlotsByName(searching_customer)

    def retranslateUi(self, searching_customer):
        _translate = QtCore.QCoreApplication.translate
        searching_customer.setWindowTitle(_translate("searching_customer", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("searching_customer", "ID Customer"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("searching_customer", "Nama Customer"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("searching_customer", "Alamat Customer"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("searching_customer", "No. Telp"))
        self.btn_select.setText(_translate("searching_customer", "Masukkan ID Customer"))
        self.lineEdit.setPlaceholderText(_translate("searching_customer", "ID Customer"))
        self.label.setText(_translate("searching_customer", "Searching Customer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    searching_customer = QtWidgets.QMainWindow()
    ui = Ui_searching_customer()
    ui.setupUi(searching_customer)
    searching_customer.show()
    sys.exit(app.exec_())
