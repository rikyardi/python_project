# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# from daftar_cs.daftar import Ui_Daftar
from resepsionis import Ui_resepsionis
from admin.admin import Ui_admin
import pymysql, ctypes


class Ui_MainWindow(object):
    def koneksi(self):
        con = pymysql.connect("localhost", "root", "", "hotel1")
        self.cur = con.cursor()

    def form_daftar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Daftar()
        self.ui.setupUi(self.window)
        self.window.show()

    def CekLogin(self):
        self.koneksi()
        a = self.username.text()
        b = self.password.text()

        self.cur.execute("select * from customer where username_cs='"+a+"' and password_cs='"+b+"' ")
        data = self.cur.fetchall()
        self.cur.execute("select * from user where username='" +a+ "' and password='" +b+ "' ")
        data1 = self.cur.fetchall()
        if (data):
            print ("ini customer")
        elif(data1):
            if(data1[0][6] == "Admin"):
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_admin()
                self.ui.setupUi(self.window)
                self.window.show()
            else:
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_resepsionis()
                self.ui.setupUi(self.window)
                self.window.show()
                print("resepsionis")

        else:
            print("error")
            # if(data):
        #     if(data[0][7] == "Customer" ):
        #         print("ini customer")
        #     if(data[0][7] == "Resepsionis"):
        #         print("ini resepsions")
        #     if(data[0][7] == "Admin"):
        #         print("ini admin")
        #     print("login Sukses")
        # else:
        #     print("gagal")
        #     ctypes.windll.user32.MessageBoxW(0, "Username dan Password yang Anda Masukan Salah!", "Gagal Login", 0)



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 407)
        MainWindow.setMaximumSize(QtCore.QSize(415, 407))
        MainWindow.setStyleSheet("* {\n"
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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 70, 341, 291))
        self.frame.setStyleSheet("*{\n"
"background-color:#F18C8E;\n"
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
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(40, 60, 261, 31))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(40, 130, 261, 31))
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton(self.frame)
        self.login.setGeometry(QtCore.QRect(40, 190, 261, 41))
        self.login.setStyleSheet("")
        self.login.setObjectName("login")
        self.login.clicked.connect(self.CekLogin)
        self.login_2 = QtWidgets.QPushButton(self.frame)
        self.login_2.setGeometry(QtCore.QRect(40, 240, 261, 41))
        self.login_2.setStyleSheet("*{\n"
"background : maroon;\n"
"}\n"
"\n"
"*:hover{\n"
"    background: pink;\n"
"}")
        self.login_2.setObjectName("login_2")
        self.login_2.clicked.connect(self.form_daftar)
        self.username.raise_()
        self.password.raise_()
        self.login.raise_()
        self.login_2.raise_()
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(130, 20, 161, 101))
        self.frame_2.setStyleSheet("background : #F18C8E;\n"
"border-radius : 50px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(70, 30, 21, 21))
        self.frame_3.setStyleSheet("border-radius:10px;\n"
"background:white;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(30, 60, 111, 31))
        self.label.setStyleSheet("font: 75 italic 14pt \"Kristen ITC\";\n"
"color : white;")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.login.setText(_translate("MainWindow", "Login"))
        self.login_2.setText(_translate("MainWindow", "Daftar"))
        self.label.setText(_translate("MainWindow", "Form Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
