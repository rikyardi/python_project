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
        db = pymysql.connect("localhost", "root", "", "hotel1")
        cur = db.cursor()
        a = self.lineEdit_kd.text()
        b = self.lineEdit_kd_2.text()
        c = self.comboBox.currentText()
        print (c)
        if c == "ID Customer":
            cur.execute("UPDATE customer SET id_customer = '" + b + "' WHERE id_customer = '" + a + "' ")
        elif c == "Nama ":
            cur.execute("UPDATE customer SET nama_cs = '" + b + "' WHERE id_customer = '" + a + "' ")
        elif c == "Alamat":
            cur.execute("UPDATE customer SET alamat_cs = '" + b + "' WHERE id_customer = '" + a + "' ")
        elif c == "Telepon":
            cur.execute("UPDATE customer SET no_telp_cs = '" + b + "' WHERE id_customer ='" + a + "' ")
        elif c == "Email":
            cur.execute("UPDATE customer SET email = '" + b + "' WHERE id_customer ='" + a + "' ")
        db.commit()
    def setupUi(self, update_customer):
        update_customer.setObjectName("update_customer")
        update_customer.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(update_customer)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 205, 721, 331))
        self.frame.setStyleSheet("border-radius:20px;\n"
"background-color:#40739e;\n"
"    font-family : century gothic;\n"
"    color:#ffffff;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_update = QtWidgets.QPushButton(self.frame)
        self.btn_update.setGeometry(QtCore.QRect(370, 260, 121, 41))
        self.btn_update.setStyleSheet("border-radius:20px;\n"
"background-color:#c23616;font-family : century gothic;color:#ffffff;")
        self.btn_update.setObjectName("btn_update")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(160, 30, 421, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(200, 60, 121, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_kd_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_kd_2.setGeometry(QtCore.QRect(210, 220, 311, 20))
        self.lineEdit_kd_2.setStyleSheet("border:none;\n"
"border-bottom:1px solid white;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.lineEdit_kd_2.setObjectName("lineEdit_kd_2")
        self.lineEdit_kd = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_kd.setGeometry(QtCore.QRect(210, 90, 211, 20))
        self.lineEdit_kd.setStyleSheet("border:none;\n"
"border-bottom:1px solid white;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.lineEdit_kd.setObjectName("lineEdit_kd")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(210, 150, 141, 22))
        self.comboBox.setStyleSheet("background-color:#353b48;\n"
"color:#ffffff;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(200, 120, 351, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_8.setGeometry(QtCore.QRect(750, 25, 31, 31))
        self.graphicsView_8.setStyleSheet("background-color:#c23616\n"
"")
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_9.setGeometry(QtCore.QRect(740, 15, 31, 31))
        self.graphicsView_9.setStyleSheet("background-color:#353b48")
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(310, 85, 191, 51))
        self.frame_2.setStyleSheet("border-radius:20px;\n"
"background-color:#40739e;font-family : century gothic;color:#ffffff;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 15, 241, 41))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 0, 781, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 60, 781, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
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
        self.btn_update.setText(_translate("update_customer", "Update"))
        self.label_11.setText(_translate("update_customer", "Masukkan ID Customer yang ingin anda update"))
        self.label_6.setText(_translate("update_customer", "ID Customer"))
        self.comboBox.setItemText(0, _translate("update_customer", "ID Customer"))
        self.comboBox.setItemText(1, _translate("update_customer", "Nama "))
        self.comboBox.setItemText(2, _translate("update_customer", "Alamat"))
        self.comboBox.setItemText(3, _translate("update_customer", "Telepon"))
        self.comboBox.setItemText(4, _translate("update_customer", "Email"))
        self.label_12.setText(_translate("update_customer", "Pilih menu yang ingin anda update"))
        self.label_3.setText(_translate("update_customer", "Update Customer"))
        self.label.setText(_translate("update_customer", "HOTEL SUKAMAJU"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_customer = QtWidgets.QMainWindow()
    ui = Ui_update_customer()
    ui.setupUi(update_customer)
    update_customer.show()
    sys.exit(app.exec_())
