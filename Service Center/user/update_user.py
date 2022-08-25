# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_user.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_update_user(object):
    def update(self):
        db =  pymysql.connect("localhost","root","","bingung")
        cur = db.cursor()
        a = self.lineEdit_kd.text()
        b = self.lineEdit_kd_2.text()
        c = self.comboBox.currentText()
        if c == "User ID":
            cur.execute("UPDATE user SET user_id='"+b+"' WHERE user_id='"+a+"' ")
        elif c == "Nama":
            cur.execute("UPDATE user SET user_name='" + b + "' WHERE user_id='" + a + "' ")
        elif c == "Alamat":
            cur.execute("UPDATE user SET user_address='" + b + "' WHERE user_id='" + a + "' ")
        elif c == "Telepon":
            cur.execute("UPDATE user SET user_telp='" + b + "' WHERE user_id='" + a + "' ")
        elif c == "email":
            cur.execute("UPDATE user SET user_email='" + b + "' WHERE user_id='" + a + "' ")
        elif c == "gender":
            cur.execute("UPDATE user SET user_gender='" + b + "' WHERE user_id='" + a + "' ")
        elif c == "position":
            cur.execute("UPDATE user SET user_position='" + b + "' WHERE user_id='" + a + "' ")
        elif c == "username":
            cur.execute("UPDATE user SET user_username='" + b + "' WHERE user_id='" + a + "' ")
        elif c == "password":
            cur.execute("UPDATE user SET user_password='" + b + "' WHERE user_id='" + a + "' ")
        db.commit()

    def setupUi(self, update_user):
        update_user.setObjectName("update_user")
        update_user.resize(800, 600)
        update_user.setStyleSheet("background-color: rgb(112, 112, 112);")
        self.centralwidget = QtWidgets.QWidget(update_user)
        self.centralwidget.setObjectName("centralwidget")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(200, 170, 431, 21))
        font = QtGui.QFont()
        font.setFamily("Iskoola Pota")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 140, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Iskoola Pota")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 40, 781, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(781, 0))
        self.line.setMaximumSize(QtCore.QSize(781, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.line.setFont(font)
        self.line.setStyleSheet("  padding: 15px 25px;\n"
"  font-size: 15px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: rgb(60, 1, 255);\n"
"  background-color: rgb(0, 255, 238);\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;\n"
"hover{color:red}")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(350, 200, 111, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 780, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.label_menu = QtWidgets.QLabel(self.centralwidget)
        self.label_menu.setGeometry(QtCore.QRect(110, 230, 591, 21))
        font = QtGui.QFont()
        font.setFamily("Iskoola Pota")
        font.setPointSize(12)
        self.label_menu.setFont(font)
        self.label_menu.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_menu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_menu.setObjectName("label_menu")
        self.lineEdit_kd_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_kd_2.setGeometry(QtCore.QRect(250, 260, 311, 20))
        self.lineEdit_kd_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_kd_2.setObjectName("lineEdit_kd_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 60, 801, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(240, 110, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Iskoola Pota")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.lineEdit_kd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_kd.setGeometry(QtCore.QRect(370, 140, 181, 20))
        self.lineEdit_kd.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_kd.setObjectName("lineEdit_kd")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(440, 300, 101, 41))
        self.btn_update.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(170, 255, 0);")
        self.btn_update.setObjectName("btn_update")
        update_user.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(update_user)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        update_user.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(update_user)
        self.statusbar.setObjectName("statusbar")
        update_user.setStatusBar(self.statusbar)

        self.btn_update.clicked.connect(self.update)

        self.retranslateUi(update_user)
        QtCore.QMetaObject.connectSlotsByName(update_user)

    def retranslateUi(self, update_user):
        _translate = QtCore.QCoreApplication.translate
        update_user.setWindowTitle(_translate("update_user", "MainWindow"))
        self.label_12.setText(_translate("update_user", "Pilih menu yang ingin anda update"))
        self.label_6.setText(_translate("update_user", "User ID"))
        self.line.setWhatsThis(_translate("update_user", "<html><head/><body><p>s</p></body></html>"))
        self.comboBox.setItemText(0, _translate("update_user", "User ID"))
        self.comboBox.setItemText(1, _translate("update_user", "Nama"))
        self.comboBox.setItemText(2, _translate("update_user", "Alamat"))
        self.comboBox.setItemText(3, _translate("update_user", "Telepon"))
        self.comboBox.setItemText(4, _translate("update_user", "email"))
        self.comboBox.setItemText(5, _translate("update_user", "gender"))
        self.comboBox.setItemText(6, _translate("update_user", "position"))
        self.comboBox.setItemText(7, _translate("update_user", "username"))
        self.comboBox.setItemText(8, _translate("update_user", "password"))
        self.label_7.setText(_translate("update_user", "UPDATE"))
        self.label_8.setText(_translate("update_user", "Service Center"))
        self.label_9.setText(_translate("update_user", "Hai, Admin"))
        self.label_menu.setText(_translate("update_user", "Untuk Position hanya bisa Manager, Administrator, Engineer, Operator"))
        self.label_10.setText(_translate("update_user", "UPDATE A USER"))
        self.label_11.setText(_translate("update_user", "Masukkan ID User yang ingin anda update"))
        self.btn_update.setText(_translate("update_user", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_user = QtWidgets.QMainWindow()
    ui = Ui_update_user()
    ui.setupUi(update_user)
    update_user.show()
    sys.exit(app.exec_())
