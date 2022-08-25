# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'daftar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql, random, ctypes
class Ui_Daftar(object):
    def koneksi(self):
        self.con = pymysql.connect("localhost", "root", "", "hotel1")
        self.cur = self.con.cursor()

    def getData(self):
        self.koneksi()

        id_cs = random.randrange(0,99999)
        a = self.nama_cs.text()
        b = self.no_telp_cs.text()
        c = self.alamat_cs.toPlainText()
        d = self.email_cs.text()
        e = self.username.text()
        f = self.password.text()

        self.cur.execute("insert into customer values('"+str(id_cs)+"','"+a+"','"+b+"','"+c+"','"+d+"','"+e+"','"+f+"')")
        self.con.commit()
        ctypes.windll.user32.MessageBoxW(0, "Berhasil Mendaftar", "Sukses", 0)
        self.nama_cs.setText("")
        self.no_telp_cs.setText("")
        self.alamat_cs.setPlainText("")
        self.email_cs.setText("")
        self.username.setText("")
        self.password.setText("")

    def setupUi(self, Daftar):
        Daftar.setObjectName("Daftar")
        Daftar.resize(418, 515)
        Daftar.setStyleSheet("* {\n"
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
"QPlainTextEdit{\n"
"    background : transparent;\n"
"    border : none;\n"
"    border-bottom : 1px solid white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Daftar)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(140, 10, 161, 101))
        self.frame_2.setStyleSheet("background : #F18C8E;\n"
"border-radius : 50px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(70, 10, 21, 21))
        self.frame_3.setStyleSheet("border-radius:10px;\n"
"background:white;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(30, 40, 111, 31))
        self.label.setStyleSheet("font: 75 italic 14pt \"Kristen ITC\";\n"
"color : white;")
        self.label.setObjectName("label")
        self.frame_3.raise_()
        self.label.raise_()
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(50, 60, 321, 431))
        self.frame_4.setStyleSheet("*{\n"
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
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.nama_cs = QtWidgets.QLineEdit(self.frame_4)
        self.nama_cs.setGeometry(QtCore.QRect(30, 80, 261, 31))
        self.nama_cs.setObjectName("nama_cs")
        self.login_2 = QtWidgets.QPushButton(self.frame_4)
        self.login_2.setGeometry(QtCore.QRect(30, 370, 261, 41))
        self.login_2.setStyleSheet("*{\n"
"background : maroon;\n"
"}\n"
"\n"
"*:hover{\n"
"    background: pink;\n"
"}")
        self.login_2.setObjectName("login_2")
        self.login_2.clicked.connect(self.getData)
        self.email_cs = QtWidgets.QLineEdit(self.frame_4)
        self.email_cs.setGeometry(QtCore.QRect(30, 240, 261, 31))
        self.email_cs.setObjectName("email_cs")
        self.no_telp_cs = QtWidgets.QLineEdit(self.frame_4)
        self.no_telp_cs.setGeometry(QtCore.QRect(30, 200, 261, 31))
        self.no_telp_cs.setObjectName("no_telp_cs")
        self.alamat_cs = QtWidgets.QPlainTextEdit(self.frame_4)
        self.alamat_cs.setGeometry(QtCore.QRect(30, 120, 261, 71))
        self.alamat_cs.setStyleSheet("border-radius: 0px;")
        self.alamat_cs.setObjectName("alamat_cs")
        self.username = QtWidgets.QLineEdit(self.frame_4)
        self.username.setGeometry(QtCore.QRect(30, 280, 261, 31))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.frame_4)
        self.password.setGeometry(QtCore.QRect(30, 320, 261, 31))
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.frame_4.raise_()
        self.frame_2.raise_()
        Daftar.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Daftar)
        self.statusbar.setObjectName("statusbar")
        Daftar.setStatusBar(self.statusbar)

        self.retranslateUi(Daftar)
        QtCore.QMetaObject.connectSlotsByName(Daftar)

    def retranslateUi(self, Daftar):
        _translate = QtCore.QCoreApplication.translate
        Daftar.setWindowTitle(_translate("Daftar", "MainWindow"))
        self.label.setText(_translate("Daftar", "Buat Akun"))
        self.nama_cs.setPlaceholderText(_translate("Daftar", "Nama Lengkap"))
        self.login_2.setText(_translate("Daftar", "Daftar"))
        self.email_cs.setPlaceholderText(_translate("Daftar", "Email"))
        self.no_telp_cs.setPlaceholderText(_translate("Daftar", "No Telp"))
        self.alamat_cs.setPlaceholderText(_translate("Daftar", "Alamat Anda"))
        self.username.setPlaceholderText(_translate("Daftar", "Username"))
        self.password.setPlaceholderText(_translate("Daftar", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Daftar = QtWidgets.QMainWindow()
    ui = Ui_Daftar()
    ui.setupUi(Daftar)
    Daftar.show()
    sys.exit(app.exec_())
