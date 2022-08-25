# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_customer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_update_customer(object):
    def update(self):
        db = pymysql.connect("localhost","root","","hotel1")
        cur = db.cursor()
        a = self.lineEdit_id.text()
        b = self.lineEdit_menu.text()
        c = self.comboBox.currentText()
        if c == "ID Customer":
            cur.execute("UPDATE customer SET id_customer = '"+b+"' WHERE id_customer = '"+a+"' ")
        elif c == "Nama":
            cur.execute("UPDATE customer SET nama_cs = '"+b+"' WHERE id_customer = '"+a+"' ")
        elif c == "Alamat":
            cur.execute("UPDATE customer SET alamat_cs = '"+b+"' WHERE id_customer = '"+a+"' ")
        elif c == "Telepon":
            cur.execute("UPDATE customer SET no_telp_cs = '"+b+"' WHERE id_customer ='"+a+"' ")
        db.commit()
    def setupUi(self, update_customer):
        update_customer.setObjectName("update_customer")
        update_customer.resize(800, 600)
        update_customer.setStyleSheet("* {\n"
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
        self.centralwidget = QtWidgets.QWidget(update_customer)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(290, 0, 251, 80))
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
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(40, 130, 721, 331))
        self.frame_2.setStyleSheet("*{\n"
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
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.btn_update = QtWidgets.QPushButton(self.frame_2)
        self.btn_update.setGeometry(QtCore.QRect(370, 260, 121, 41))
        self.btn_update.setStyleSheet("")
        self.btn_update.setObjectName("btn_update")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(160, 30, 421, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(200, 60, 121, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_menu = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_menu.setGeometry(QtCore.QRect(210, 220, 311, 20))
        self.lineEdit_menu.setStyleSheet("border:none;\n"
"border-bottom:1px solid white;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.lineEdit_menu.setObjectName("lineEdit_menu")
        self.lineEdit_id = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_id.setGeometry(QtCore.QRect(210, 90, 211, 20))
        self.lineEdit_id.setStyleSheet("border:none;\n"
"border-bottom:1px solid white;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(210, 150, 141, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(200, 120, 351, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        update_customer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(update_customer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        update_customer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(update_customer)
        self.statusbar.setObjectName("statusbar")
        update_customer.setStatusBar(self.statusbar)

        self.btn_update.clicked.connect(self.update)

        self.retranslateUi(update_customer)
        QtCore.QMetaObject.connectSlotsByName(update_customer)

    def retranslateUi(self, update_customer):
        _translate = QtCore.QCoreApplication.translate
        update_customer.setWindowTitle(_translate("update_customer", "MainWindow"))
        self.label.setText(_translate("update_customer", "Update Customer"))
        self.btn_update.setText(_translate("update_customer", "Update"))
        self.label_11.setText(_translate("update_customer", "Masukkan ID Customer yang ingin anda update"))
        self.label_6.setText(_translate("update_customer", "ID Customer"))
        self.comboBox.setItemText(0, _translate("update_customer", "ID Customer"))
        self.comboBox.setItemText(1, _translate("update_customer", "Nama"))
        self.comboBox.setItemText(2, _translate("update_customer", "Alamat"))
        self.comboBox.setItemText(3, _translate("update_customer", "Telepon"))
        self.label_12.setText(_translate("update_customer", "Pilih menu yang ingin anda update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_customer = QtWidgets.QMainWindow()
    ui = Ui_update_customer()
    ui.setupUi(update_customer)
    update_customer.show()
    sys.exit(app.exec_())
