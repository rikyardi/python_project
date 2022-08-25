# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kamar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from admin.room.delete_kamar import Ui_delete_kamar
from admin.room.update_kamar import Ui_update_kamar
from admin.room.insert_kamar import Ui_insert_kamar
import pymysql

class Ui_kamar(object):
    def insert(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_insert_kamar()
        self.ui.setupUi(self.window)
        self.window.show()
    def update(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_update_kamar()
        self.ui.setupUi(self.window)
        self.window.show()
    def delete(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_delete_kamar()
        self.ui.setupUi(self.window)
        self.window.show()
    def select(self):
        db = pymysql.connect("localhost","root","", "hotel1")
        cur = db.cursor()
        cur.execute("SELECT kamar.id_kamar, kamar.kelas_kamar, harga.harga, kamar.status FROM kamar, harga WHERE kamar.id_harga = harga.id_harga;")
        result = cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        db.commit()
    def setupUi(self, kamar):
        kamar.setObjectName("kamar")
        kamar.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(kamar)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 0, 781, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_8.setGeometry(QtCore.QRect(750, 25, 31, 31))
        self.graphicsView_8.setStyleSheet("background-color:#c23616\n"
"")
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_9.setGeometry(QtCore.QRect(740, 15, 31, 31))
        self.graphicsView_9.setStyleSheet("background-color:#353b48")
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(320, 495, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_update.sizePolicy().hasHeightForWidth())
        self.btn_update.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.btn_update.setFont(font)
        self.btn_update.setStyleSheet("padding: 15px 25px;\n"
"  font-size: 13px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: white;\n"
"  background-color: #40739e;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;")
        self.btn_update.setObjectName("btn_update")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 15, 241, 41))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(170, 150, 441, 261))
        self.tableWidget.setStyleSheet("background-color:white;")
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
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(360, 80, 81, 51))
        self.frame_2.setStyleSheet("border-radius:20px;\n"
"background-color:#40739e;font-family : century gothic;color:#ffffff;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(15, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_all = QtWidgets.QPushButton(self.centralwidget)
        self.btn_all.setGeometry(QtCore.QRect(330, 435, 141, 41))
        self.btn_all.setStyleSheet("color: white;\n"
"  background-color: #c23616;\n"
"border-radius:20px;\n"
"\n"
"")
        self.btn_all.setObjectName("btn_all")
        self.btn_tambah = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tambah.setGeometry(QtCore.QRect(510, 495, 211, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tambah.sizePolicy().hasHeightForWidth())
        self.btn_tambah.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.btn_tambah.setFont(font)
        self.btn_tambah.setStyleSheet("padding: 15px 25px;\n"
"  font-size: 13px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: white;\n"
"  background-color: #40739e;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;")
        self.btn_tambah.setObjectName("btn_tambah")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(100, 495, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet("padding: 15px 25px;\n"
"  font-size: 13px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: white;\n"
"  background-color: #40739e;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;")
        self.btn_delete.setObjectName("btn_delete")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 60, 781, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        kamar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(kamar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        kamar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(kamar)
        self.statusbar.setObjectName("statusbar")
        kamar.setStatusBar(self.statusbar)

        self.btn_all.clicked.connect(self.select)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_update.clicked.connect(self.update)
        self.btn_tambah.clicked.connect(self.insert)

        self.retranslateUi(kamar)
        QtCore.QMetaObject.connectSlotsByName(kamar)

    def retranslateUi(self, kamar):
        _translate = QtCore.QCoreApplication.translate
        kamar.setWindowTitle(_translate("kamar", "MainWindow"))
        self.btn_update.setText(_translate("kamar", "Update Kamar"))
        self.label.setText(_translate("kamar", "HOTEL SUKAMAJU"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("kamar", "ID Kamar"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("kamar", "Kelas Kamar"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("kamar", "Harga"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("kamar", "Status"))
        self.label_2.setText(_translate("kamar", "Kamar"))
        self.btn_all.setText(_translate("kamar", "Lihat Semua Kamar"))
        self.btn_tambah.setText(_translate("kamar", "Menambahkan Kamar"))
        self.btn_delete.setText(_translate("kamar", "Menghapus Kamar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    kamar = QtWidgets.QMainWindow()
    ui = Ui_kamar()
    ui.setupUi(kamar)
    kamar.show()
    sys.exit(app.exec_())
