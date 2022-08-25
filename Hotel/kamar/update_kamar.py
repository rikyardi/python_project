# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_kamar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_update_room(object):
    def update(self):
        db = pymysql.connect("localhost","root","","hotel1")
        cur = db.cursor()
        a = self.lineEdit_id.text()
        b = self.lineEdit_menu.text()
        c = self.comboBox.currentText()
        if c == "ID Kamar":
            cur.execute("UPDATE kamar SET id_kamar = '"+b+"' WHERE id_kamar = '"+a+"' ")
        elif c == "Kelas Kamar":
            cur.execute("UPDATE kamar SET kelas_kamar = '"+b+"' WHERE id_kamar = '"+a+"' ")
        elif c == "Status":
            cur.execute("UPDATE kamar SET status = '"+b+"' WHERE id_kamar = '"+a+"' ")
        db.commit()
    def setupUi(self, update_room):
        update_room.setObjectName("update_room")
        update_room.resize(800, 609)
        update_room.setStyleSheet("* {\n"
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
        self.centralwidget = QtWidgets.QWidget(update_room)
        self.centralwidget.setObjectName("centralwidget")
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
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(200, 120, 351, 21))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(280, 0, 251, 80))
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
        update_room.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(update_room)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        update_room.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(update_room)
        self.statusbar.setObjectName("statusbar")
        update_room.setStatusBar(self.statusbar)

        self.btn_update.clicked.connect(self.update)

        self.retranslateUi(update_room)
        QtCore.QMetaObject.connectSlotsByName(update_room)

    def retranslateUi(self, update_room):
        _translate = QtCore.QCoreApplication.translate
        update_room.setWindowTitle(_translate("update_room", "MainWindow"))
        self.btn_update.setText(_translate("update_room", "Update"))
        self.label_11.setText(_translate("update_room", "Masukkan ID Kamar yang ingin anda update"))
        self.label_6.setText(_translate("update_room", "ID Kamar"))
        self.lineEdit_id.setPlaceholderText(_translate("update_room", "ID Kamar..."))
        self.comboBox.setItemText(0, _translate("update_room", "ID Kamar"))
        self.comboBox.setItemText(1, _translate("update_room", "Kelas Kamar"))
        self.comboBox.setItemText(2, _translate("update_room", "Status"))
        self.label_12.setText(_translate("update_room", "Pilih menu yang ingin anda update"))
        self.label.setText(_translate("update_room", "Update Kamar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_room = QtWidgets.QMainWindow()
    ui = Ui_update_room()
    ui.setupUi(update_room)
    update_room.show()
    sys.exit(app.exec_())
