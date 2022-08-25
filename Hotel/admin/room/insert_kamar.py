# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insert_kamar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_insert_kamar(object):
    def insert(self):
        db = pymysql.connect("localhost","root","","hotel1")
        cur = db.cursor()
        id_kamar = self.lineEdit_id.text()
        harga = self.lineEdit_nama.text()
        status = self.lineEdit_alamat.text()
        kelas = self.comboBox.currentText()
        cur.execute("INSERT INTO kamar VALUES('"+id_kamar+"','"+kelas+"','"+harga+"','"+status+"') ")
        db.commit()
    def setupUi(self, insert_kamar):
        insert_kamar.setObjectName("insert_kamar")
        insert_kamar.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(insert_kamar)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 241, 41))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_8.setGeometry(QtCore.QRect(750, 30, 31, 31))
        self.graphicsView_8.setStyleSheet("background-color:#c23616\n"
"")
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_9.setGeometry(QtCore.QRect(740, 20, 31, 31))
        self.graphicsView_9.setStyleSheet("background-color:#353b48")
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 5, 781, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(330, 90, 151, 51))
        self.frame_2.setStyleSheet("border-radius:20px;\n"
"background-color:#40739e;font-family : century gothic;color:#ffffff;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 65, 781, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(90, 190, 621, 371))
        self.frame.setStyleSheet("border-radius:20px;\n"
"background-color:#40739e;font-family : century gothic;color:#ffffff;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(40, 270, 191, 20))
        self.comboBox.setStyleSheet("background-color:#353b48;\n"
"color:#ffffff;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(40, 160, 81, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_id = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_id.setGeometry(QtCore.QRect(50, 70, 191, 20))
        self.lineEdit_id.setStyleSheet("border:none;\n"
"border-bottom:1px solid white;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 100, 161, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color : rgb(255, 255, 255)")
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(40, 230, 111, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_13.setObjectName("label_13")
        self.lineEdit_nama = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_nama.setGeometry(QtCore.QRect(50, 130, 191, 20))
        self.lineEdit_nama.setStyleSheet("border:none;\n"
"border-bottom:1px solid white;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.lineEdit_nama.setObjectName("lineEdit_nama")
        self.btn_insert = QtWidgets.QPushButton(self.frame)
        self.btn_insert.setGeometry(QtCore.QRect(360, 150, 111, 41))
        self.btn_insert.setStyleSheet("border-radius:20px;\n"
"background-color:#c23616;font-family : century gothic;color:#ffffff;")
        self.btn_insert.setObjectName("btn_insert")
        self.lineEdit_alamat = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_alamat.setGeometry(QtCore.QRect(50, 190, 191, 20))
        self.lineEdit_alamat.setStyleSheet("border:none;\n"
"border-bottom:1px solid white;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.lineEdit_alamat.setObjectName("lineEdit_alamat")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 40, 161, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        insert_kamar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(insert_kamar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        insert_kamar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(insert_kamar)
        self.statusbar.setObjectName("statusbar")
        insert_kamar.setStatusBar(self.statusbar)

        self.btn_insert.clicked.connect(self.insert)

        self.retranslateUi(insert_kamar)
        QtCore.QMetaObject.connectSlotsByName(insert_kamar)

    def retranslateUi(self, insert_kamar):
        _translate = QtCore.QCoreApplication.translate
        insert_kamar.setWindowTitle(_translate("insert_kamar", "MainWindow"))
        self.label.setText(_translate("insert_kamar", "HOTEL SUKAMAJU"))
        self.label_2.setText(_translate("insert_kamar", "Insert kamar"))
        self.comboBox.setItemText(0, _translate("insert_kamar", "Standar Room (STD)"))
        self.comboBox.setItemText(1, _translate("insert_kamar", "Superior Room (SUP)"))
        self.comboBox.setItemText(2, _translate("insert_kamar", "Deluxe Room (DLX)"))
        self.comboBox.setItemText(3, _translate("insert_kamar", "Junior Suit Room (JRSTE)"))
        self.comboBox.setItemText(4, _translate("insert_kamar", "Suit Room"))
        self.comboBox.setItemText(5, _translate("insert_kamar", "Presidental Suit"))
        self.label_5.setText(_translate("insert_kamar", "Status"))
        self.label_7.setText(_translate("insert_kamar", "Harga"))
        self.label_13.setText(_translate("insert_kamar", "Kelas Kamar"))
        self.btn_insert.setText(_translate("insert_kamar", "INSERT"))
        self.label_6.setText(_translate("insert_kamar", "ID Kamar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    insert_kamar = QtWidgets.QMainWindow()
    ui = Ui_insert_kamar()
    ui.setupUi(insert_kamar)
    insert_kamar.show()
    sys.exit(app.exec_())
