# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_update.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_user_update(object):
    def update(self):
        db = pymysql.connect("localhost","root","","hotel1")
        cur = db.cursor()
        a = self.lineEdit_kd.text()
        b = self.lineEdit_kd_2.text()
        c = self.comboBox.currentText()
        if c == "User ID":
            cur.execute("UPDATE user SET id_user = '" + b + "' WHERE id_user = '" + a + "' ")
        elif c == "Nama":
            cur.execute("UPDATE user SET nama = '" + b + "' WHERE id_user = '" + a + "' ")
        elif c == "Alamat":
            cur.execute("UPDATE user SET alamat = '" + b + "' WHERE id_user = '" + a + "' ")
        elif c == "Telepon":
            cur.execute("UPDATE user SET no_telp = '" + b + "' WHERE id_user ='" + a + "' ")
        elif c == "Jabatan":
            cur.execute("UPDATE user SET role = '" + b + "' WHERE id_user ='" + a + "' ")
        db.commit()
    def setupUi(self, user_update):
        user_update.setObjectName("user_update")
        user_update.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(user_update)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_8.setGeometry(QtCore.QRect(750, 25, 31, 31))
        self.graphicsView_8.setStyleSheet("background-color:#c23616\n"
"")
        self.graphicsView_8.setObjectName("graphicsView_8")
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
        self.lineEdit_kd_2.setGeometry(QtCore.QRect(210, 210, 311, 20))
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
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 60, 781, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_9.setGeometry(QtCore.QRect(740, 15, 31, 31))
        self.graphicsView_9.setStyleSheet("background-color:#353b48")
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(320, 85, 171, 51))
        self.frame_2.setStyleSheet("border-radius:20px;\n"
"background-color:#40739e;font-family : century gothic;color:#ffffff;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(15, 10, 141, 31))
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
        user_update.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(user_update)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        user_update.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(user_update)
        self.statusbar.setObjectName("statusbar")
        user_update.setStatusBar(self.statusbar)

        self.btn_update.clicked.connect(self.update)

        self.retranslateUi(user_update)
        QtCore.QMetaObject.connectSlotsByName(user_update)

    def retranslateUi(self, user_update):
        _translate = QtCore.QCoreApplication.translate
        user_update.setWindowTitle(_translate("user_update", "MainWindow"))
        self.btn_update.setText(_translate("user_update", "Update"))
        self.label_11.setText(_translate("user_update", "Masukkan ID User yang ingin anda update"))
        self.label_6.setText(_translate("user_update", "User ID"))
        self.comboBox.setItemText(0, _translate("user_update", "User ID"))
        self.comboBox.setItemText(1, _translate("user_update", "Nama"))
        self.comboBox.setItemText(2, _translate("user_update", "Alamat"))
        self.comboBox.setItemText(3, _translate("user_update", "Telepon"))
        self.comboBox.setItemText(4, _translate("user_update", "Jabatan"))
        self.label_12.setText(_translate("user_update", "Pilih menu yang ingin anda update"))
        self.label_3.setText(_translate("user_update", "USER UPDATE"))
        self.label.setText(_translate("user_update", "Hotel Sukamaju"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    user_update = QtWidgets.QMainWindow()
    ui = Ui_user_update()
    ui.setupUi(user_update)
    user_update.show()
    sys.exit(app.exec_())
