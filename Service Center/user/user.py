# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'User.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from user.insert_user import Ui_insert_user
from user.delete_user import Ui_delete_user
from user.select_user import Ui_select_user
from user.update_user import Ui_update_user
import pymysql

class Ui_User(object):
    def update(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_update_user()
        self.ui.setupUi(self.window)
        self.window.show()

    def select(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = Ui_select_user()
        self.ui.setupUi(self.window)
        self.window.show()

    def delete(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = Ui_delete_user()
        self.ui.setupUi(self.window)
        self.window.show()

    def insert(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_insert_user()
        self.ui.setupUi(self.window)
        self.window.show()

    def lihat(self):
        db = pymysql.connect("localhost","root","","bingung")
        cur = db.cursor()
        cur.execute("SELECT user_id, user_name, user_address, user_telp, user_email, user_gender, user_position FROM user;")
        result = cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()
    def setupUi(self, User):
        User.setObjectName("User")
        User.resize(789, 600)
        User.setStyleSheet("background-color: rgb(127, 127, 127);")
        self.centralwidget = QtWidgets.QWidget(User)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 40, 801, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.line.setFont(font)
        self.line.setStyleSheet("padding: 15px 25px;\n"
"  font-size: 24px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"  color: #fff;\n"
"  background-color: rgb(0, 255, 238);\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 42))
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
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
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
        self.btn_all = QtWidgets.QPushButton(self.centralwidget)
        self.btn_all.setGeometry(QtCore.QRect(340, 350, 111, 23))
        self.btn_all.setStyleSheet("color: rgb(22, 1, 255);\n"
"  background-color: rgb(0, 255, 238);\n"
"")
        self.btn_all.setObjectName("btn_all")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 60, 801, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(200, 410, 181, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet("  padding: 15px 25px;\n"
"  font-size: 12px;\n"
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
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(410, 410, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_update.sizePolicy().hasHeightForWidth())
        self.btn_update.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_update.setFont(font)
        self.btn_update.setStyleSheet("  padding: 15px 25px;\n"
"  font-size: 11px;\n"
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
        self.btn_tambah = QtWidgets.QPushButton(self.centralwidget)
        self.btn_tambah.setGeometry(QtCore.QRect(590, 410, 191, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_tambah.sizePolicy().hasHeightForWidth())
        self.btn_tambah.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_tambah.setFont(font)
        self.btn_tambah.setStyleSheet("  padding: 15px 25px;\n"
"  font-size: 12px;\n"
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
        self.btn_cari.setGeometry(QtCore.QRect(10, 410, 161, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_cari.sizePolicy().hasHeightForWidth())
        self.btn_cari.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_cari.setFont(font)
        self.btn_cari.setStyleSheet("  padding: 15px 25px;\n"
"  font-size: 12px;\n"
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
        User.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(User)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 21))
        self.menubar.setObjectName("menubar")
        User.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(User)
        self.statusbar.setObjectName("statusbar")
        User.setStatusBar(self.statusbar)

        self.btn_all.clicked.connect(self.lihat)
        self.btn_tambah.clicked.connect(self.insert)
        self.btn_delete.clicked.connect(self.delete)
        self.btn_update.clicked.connect(self.update)
        self.btn_cari.clicked.connect(self.select)

        self.retranslateUi(User)
        QtCore.QMetaObject.connectSlotsByName(User)

    def retranslateUi(self, User):
        _translate = QtCore.QCoreApplication.translate
        User.setWindowTitle(_translate("User", "MainWindow"))
        self.label_3.setText(_translate("User", "User"))
        self.label_2.setText(_translate("User", "Service Center"))
        self.label.setText(_translate("User", "Hai, Admin"))
        self.btn_all.setText(_translate("User", "Lihat Semua User"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("User", "ID User"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("User", "Nama User"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("User", "Alamat User"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("User", "No. Telp"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("User", "Alamat Email"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("User", "Kelamin"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("User", "Jabatan"))
        self.btn_delete.setText(_translate("User", "Menghapus User"))
        self.btn_update.setText(_translate("User", "Update User"))
        self.btn_tambah.setText(_translate("User", "Menambahkan User"))
        self.btn_cari.setText(_translate("User", "Mencari User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    User = QtWidgets.QMainWindow()
    ui = Ui_User()
    ui.setupUi(User)
    User.show()
    sys.exit(app.exec_())
