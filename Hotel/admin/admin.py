# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from admin.kustomer.customer import Ui_customer
from admin.room.kamar import Ui_kamar
from admin.pengguna.user import Ui_user

class Ui_admin(object):
    def user(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_user()
        self.ui.setupUi(self.window)
        self.window.show()
    def kamar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_kamar()
        self.ui.setupUi(self.window)
        self.window.show()
    def customer(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_customer()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, admin):
        admin.setObjectName("admin")
        admin.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(admin)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 0, 781, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(290, 85, 221, 41))
        self.frame_3.setStyleSheet("border-radius:20px;\n"
"background-color:#40739e;font-family : century gothic;color:#ffffff;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 15, 241, 41))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(100, 195, 611, 271))
        self.frame.setStyleSheet("background-color: #353b48;\n"
"color:#ffffff;\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(80, 30, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.btn_kamar = QtWidgets.QPushButton(self.frame)
        self.btn_kamar.setGeometry(QtCore.QRect(230, 140, 151, 53))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_kamar.sizePolicy().hasHeightForWidth())
        self.btn_kamar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_kamar.setFont(font)
        self.btn_kamar.setStyleSheet("padding: 15px 25px;\n"
"  font-size: 24px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: white;\n"
"  background-color: #c23616;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;")
        self.btn_kamar.setObjectName("btn_kamar")
        self.btn_transaksi = QtWidgets.QPushButton(self.frame)
        self.btn_transaksi.setGeometry(QtCore.QRect(30, 140, 151, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_transaksi.sizePolicy().hasHeightForWidth())
        self.btn_transaksi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_transaksi.setFont(font)
        self.btn_transaksi.setStyleSheet("padding: 15px 25px;\n"
"  font-size: 24px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: white;\n"
"  background-color: #c23616;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;")
        self.btn_transaksi.setObjectName("btn_transaksi")
        self.btn_user = QtWidgets.QPushButton(self.frame)
        self.btn_user.setGeometry(QtCore.QRect(430, 140, 131, 53))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_user.sizePolicy().hasHeightForWidth())
        self.btn_user.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_user.setFont(font)
        self.btn_user.setStyleSheet("padding: 15px 25px;\n"
"  font-size: 24px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: white;\n"
"  background-color: #40739e;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;")
        self.btn_user.setObjectName("btn_user")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 60, 781, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        admin.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(admin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        admin.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(admin)
        self.statusbar.setObjectName("statusbar")
        admin.setStatusBar(self.statusbar)

        self.btn_kamar.clicked.connect(self.kamar)
        self.btn_user.clicked.connect(self.user)
        self.btn_transaksi.clicked.connect(self.customer)

        self.retranslateUi(admin)
        QtCore.QMetaObject.connectSlotsByName(admin)

    def retranslateUi(self, admin):
        _translate = QtCore.QCoreApplication.translate
        admin.setWindowTitle(_translate("admin", "MainWindow"))
        self.label_2.setText(_translate("admin", "ADMIN"))
        self.label.setText(_translate("admin", "HOTEL SUKAMAJU"))
        self.label_4.setText(_translate("admin", "PILIH YANG INGIN ANDA KERJAKAN"))
        self.btn_kamar.setText(_translate("admin", "Kamar"))
        self.btn_transaksi.setText(_translate("admin", "Customer"))
        self.btn_user.setText(_translate("admin", "User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin = QtWidgets.QMainWindow()
    ui = Ui_admin()
    ui.setupUi(admin)
    admin.show()
    sys.exit(app.exec_())
