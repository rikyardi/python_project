# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transaksi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_transaksi(object):
    def __init__(self, id_data):
        super().__init__()
        self.id_login = id_data
        self.koneksi()
        self.cur.execute("select nama_cs from customer where id_customer ='"+self.id_login+"' ")
        self.data = self.cur.fetchall()


    def koneksi(self):
        self.con = pymysql.connect("localhost","root","","hotel1")
        self.cur = self.con.cursor()

    def getData(self):
        self.koneksi()
        nama = self.lineEdit_nama.text()
        kamar = self.comboBox.currentText()
        self.cur.execute("SELECT id_customer FROM customer WHERE nama_cs ='"+nama+"'; ")
        id_cs = self.cur.fetchall()
        a = id_cs[0][0]
        b = self.lineEdit_CheckIn.text()
        c = self.lineEdit_CheckOut.text()
        wi = self.comboBox_2.currentText()


        self.cur.execute("INSERT INTO transaksi (id_cs, kelas_kamar, tgl_masuk, tgl_keluar, wilayah) VALUES"
                         "('"+a+"','"+kamar+"','"+b+"','"+c+"','"+wi+"'); ")
        self.con.commit()
        # self.cur.execute("SELECT id_kamar FROM kamar WHERE kelas_kamar='"+kamar+"' AND status='Tersedia'; ")
        # id_kamar = self.cur.fetchall()
        # self.con.commit()
        # b = id_kamar[0][0]
        # self.kamar = b
        # print(b)

    def insert(self):
        self.koneksi()

        c = self.res
        b = self.kamar
        a = self.cs
        print(a)
        print(b)
        print(c)
        check_in = self.lineEdit_CheckIn.text()
        check_out = self.lineEdit_CheckOut.text()
        wilayah = self.comboBox_2.currentText()

        self.cur.execute("INSERT INTO transaksi (id_cs, kelas_kamar, id_resepsionis, tgl_masuk, tgl_keluar, wilayah) VALUES"
                         "('"+a+"','"+b+"','"+c+"','"+check_in+"','"+check_out+"','"+wilayah+"'); ")
        self.con.commit()
    def setupUi(self, transaksi):
        
        transaksi.setObjectName("transaksi")
        transaksi.resize(800, 600)
        transaksi.setStyleSheet("* {\n"
"    background:rgb(170, 170, 255);\n"
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
        self.centralwidget = QtWidgets.QWidget(transaksi)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(280, 0, 251, 80))
        self.frame.setStyleSheet("background-color: rgb(0, 255, 238);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 211, 31))
        self.label.setStyleSheet("font: 75 italic 14pt \"Kristen ITC\";\n"
"color : white;")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(90, 110, 621, 371))
        self.frame_2.setStyleSheet("*{\n"
"background-color:#40739e;\n"
"color:#ffffff;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    background : rgb(255, 170, 127);\n"
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
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(40, 250, 191, 20))
        self.comboBox.setStyleSheet("background-color:#353b48;\n"
"color:#ffffff;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(40, 140, 181, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(40, 80, 161, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color : rgb(255, 255, 255)")
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(40, 210, 111, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.lineEdit_CheckIn = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_CheckIn.setGeometry(QtCore.QRect(50, 110, 191, 20))
        self.lineEdit_CheckIn.setStyleSheet("border:none;\n"
"border-bottom:1px solid white;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.lineEdit_CheckIn.setObjectName("lineEdit_CheckIn")
        self.btn_insert = QtWidgets.QPushButton(self.frame_2)
        self.btn_insert.setGeometry(QtCore.QRect(440, 280, 111, 41))
        self.btn_insert.setStyleSheet("")
        self.btn_insert.setObjectName("btn_insert")
        self.lineEdit_CheckOut = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_CheckOut.setGeometry(QtCore.QRect(50, 170, 191, 20))
        self.lineEdit_CheckOut.setStyleSheet("border:none;\n"
"border-bottom:1px solid white;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.lineEdit_CheckOut.setObjectName("lineEdit_CheckOut")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(40, 20, 161, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 50, 191, 20))
        self.comboBox_2.setStyleSheet("background-color:#353b48;\n"
"color:#ffffff;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(40, 280, 111, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
    
        self.lineEdit_nama = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_nama.setGeometry(QtCore.QRect(330, 50, 191, 20))
        self.lineEdit_nama.setStyleSheet("border:none;\n"
"border-bottom:1px solid white;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.lineEdit_nama.setText("" + str(self.data[0][0]))
        self.lineEdit_nama.setObjectName("lineEdit_nama")

        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(320, 20, 181, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        transaksi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(transaksi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        transaksi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(transaksi)
        self.statusbar.setObjectName("statusbar")
        transaksi.setStatusBar(self.statusbar)

        self.btn_insert.clicked.connect(self.getData)

        self.retranslateUi(transaksi)
        QtCore.QMetaObject.connectSlotsByName(transaksi)

    def retranslateUi(self, transaksi):
        _translate = QtCore.QCoreApplication.translate
        transaksi.setWindowTitle(_translate("transaksi", "MainWindow"))
        self.label.setText(_translate("transaksi", "HOTEL SUKAMAJU"))
        self.comboBox.setItemText(0, _translate("transaksi", "Standar Room (STD)"))
        self.comboBox.setItemText(1, _translate("transaksi", "Superior Room (SUP)"))
        self.comboBox.setItemText(2, _translate("transaksi", "Deluxe Room (DLX)"))
        self.comboBox.setItemText(3, _translate("transaksi", "Junior Suit Room (JRSTE)"))
        self.comboBox.setItemText(4, _translate("transaksi", "Suit Room"))
        self.comboBox.setItemText(5, _translate("transaksi", "Presidental Suit"))
        self.label_5.setText(_translate("transaksi", "Tanggal Check-Out"))
        self.label_7.setText(_translate("transaksi", "Tanggal Check-In"))
        self.label_13.setText(_translate("transaksi", "Kelas Kamar"))
        self.btn_insert.setText(_translate("transaksi", "INSERT"))
        self.label_6.setText(_translate("transaksi", "Wilayah"))
        self.comboBox_2.setItemText(0, _translate("transaksi", "Jakarta Pusat"))
        self.comboBox_2.setItemText(1, _translate("transaksi", "Jakarta Barat"))
        self.comboBox_2.setItemText(2, _translate("transaksi", "Jakarta Timur"))
        self.comboBox_2.setItemText(3, _translate("transaksi", "Jakarta Utara"))
        self.comboBox_2.setItemText(4, _translate("transaksi", "Jakarta Selatan"))
        self.label_8.setText(_translate("transaksi", "Nama Customer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    transaksi = QtWidgets.QMainWindow()
    ui.setupUi(transaksi)
    transaksi.show()
    sys.exit(app.exec_())
