# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guarantee.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from garansi.select_guarantee import Ui_select_guarantee
from garansi.insert_guarantee import Ui_insert_guarantee
from garansi.update_guarantee import Ui_update_guarantee
from garansi.delete_guarantee import Ui_delete_guarantee
import pymysql

class Ui_guarantee(object):
    def lihat(self):
        db = pymysql.connect("localhost", "root", "", "bingung")
        cur = db.cursor()
        cur.execute("SELECT * FROM guarantee;")
        result = cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()
    def delete(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_delete_guarantee()
        self.ui.setupUi(self.window)
        self.window.show()

    def update(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = Ui_update_guarantee()
        self.ui.setupUi(self.window)
        self.window.show()

    def insert(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_insert_guarantee()
        self.ui.setupUi(self.window)
        self.window.show()

    def select(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_select_guarantee()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, guarantee):
        guarantee.setObjectName("guarantee")
        guarantee.resize(800, 600)
        guarantee.setStyleSheet("background-color: rgb(112, 112, 112);")
        self.centralwidget = QtWidgets.QWidget(guarantee)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_all = QtWidgets.QPushButton(self.centralwidget)
        self.btn_all.setGeometry(QtCore.QRect(330, 330, 111, 23))
        self.btn_all.setStyleSheet("color: rgb(22, 1, 255);\n"
"  background-color: rgb(0, 255, 238);\n"
"")
        self.btn_all.setObjectName("btn_all")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 805, 42))
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
        self.btn_tambah = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tambah.setGeometry(QtCore.QRect(570, 380, 201, 51))
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
        self.btn_cari = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cari.setGeometry(QtCore.QRect(0, 380, 161, 51))
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
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(80, 60, 631, 258))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 40, 781, 16))
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
        self.line.setStyleSheet("  font-size: 15px;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: rgb(60, 1, 255);\n"
"  background-color: rgb(0, 255, 238);\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;\n"
"")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(390, 380, 151, 51))
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
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(180, 380, 181, 51))
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
        guarantee.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(guarantee)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        guarantee.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(guarantee)
        self.statusbar.setObjectName("statusbar")
        guarantee.setStatusBar(self.statusbar)

        self.btn_cari.clicked.connect(self.select)
        self.btn_update.clicked.connect(self.update)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_tambah.clicked.connect(self.insert)
        self.btn_all.clicked.connect(self.lihat)

        self.retranslateUi(guarantee)
        QtCore.QMetaObject.connectSlotsByName(guarantee)

    def retranslateUi(self, guarantee):
        _translate = QtCore.QCoreApplication.translate
        guarantee.setWindowTitle(_translate("guarantee", "MainWindow"))
        self.btn_all.setText(_translate("guarantee", "Lihat Semua Garansi"))
        self.label_3.setText(_translate("guarantee", "GUARANTEE"))
        self.label_2.setText(_translate("guarantee", "Service Center Handphone & Laptop"))
        self.label.setText(_translate("guarantee", "Hai, Admin"))
        self.btn_tambah.setText(_translate("guarantee", "Menambahkan Garansi"))
        self.btn_cari.setText(_translate("guarantee", "Mencari Garansi"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("guarantee", "Guarantee ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("guarantee", "Guarantee Start Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("guarantee", "Guarantee End Date"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("guarantee", "Guarantee Serial"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("guarantee", "Guarantee Product ID"))
        self.line.setWhatsThis(_translate("guarantee", "<html><head/><body><p>s</p></body></html>"))
        self.btn_update.setText(_translate("guarantee", "Update Garansi"))
        self.btn_delete.setText(_translate("guarantee", "Menghapus Garansi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    guarantee = QtWidgets.QMainWindow()
    ui = Ui_guarantee()
    ui.setupUi(guarantee)
    guarantee.show()
    sys.exit(app.exec_())
