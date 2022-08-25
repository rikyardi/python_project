# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_component.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_Update_component(object):
    def update(self):
        db = pymysql.connect("localhost","root","","bingung")
        cur = db.cursor()
        a = self.lineEdit_kd.text()
        b = self.lineEdit_kd_2.text()
        c = self.comboBox.currentText()
        if c == "ID komponen":
            cur.execute("UPDATE component SET component_id = '"+b+"' WHERE component_id = '"+a+"' ")
        elif c == "Nama komponen":
            cur.execute("UPDATE component SET component_name = '"+b+"' WHERE component_id = '"+a+"' ")
        elif c == "Harga komponen":
            cur.execute("UPDATE component SET component_price = '"+b+"' WHERE component_id = '"+a+"' ")
        elif c == "Qty":
            cur.execute("UPDATE component SET component_qty = '"+b+"' WHERE component_id ='"+a+"' ")
        db.commit()
    def text(self):
        if (self.update) == True:
            self.label_menu.setText("Update Berhasil")
        elif (self.update) == False:
            self.label_menu.setText("Update Gagal")

    def setupUi(self, Update_component):
        Update_component.setObjectName("Update_component")
        Update_component.resize(800, 600)
        Update_component.setStyleSheet("background-color: rgb(112, 112, 112);")
        self.centralwidget = QtWidgets.QWidget(Update_component)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 40, 801, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.line.setFont(font)
        self.line.setStyleSheet("padding: 15px 25px;\n"
"  font-size: 24px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"  color: #fff;\n"
"  background-color: rgb(0, 255, 238);\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 60, 801, 41))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_kd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_kd.setGeometry(QtCore.QRect(360, 140, 181, 20))
        self.lineEdit_kd.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_kd.setObjectName("lineEdit_kd")
        self.btn_insert = QtWidgets.QPushButton(self.centralwidget)
        self.btn_insert.setGeometry(QtCore.QRect(430, 300, 101, 41))
        self.btn_insert.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(170, 255, 0);")
        self.btn_insert.setObjectName("btn_insert")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(240, 140, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Iskoola Pota")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(230, 110, 321, 21))
        font = QtGui.QFont()
        font.setFamily("Iskoola Pota")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(190, 170, 431, 21))
        font = QtGui.QFont()
        font.setFamily("Iskoola Pota")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(340, 200, 111, 22))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_kd_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_kd_2.setGeometry(QtCore.QRect(240, 260, 311, 20))
        self.lineEdit_kd_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_kd_2.setObjectName("lineEdit_kd_2")
        self.label_menu = QtWidgets.QLabel(self.centralwidget)
        self.label_menu.setGeometry(QtCore.QRect(100, 230, 591, 21))
        font = QtGui.QFont()
        font.setFamily("Iskoola Pota")
        font.setPointSize(12)
        self.label_menu.setFont(font)
        self.label_menu.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_menu.setText("")
        self.label_menu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_menu.setObjectName("label_menu")
        Update_component.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Update_component)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Update_component.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Update_component)
        self.statusbar.setObjectName("statusbar")
        Update_component.setStatusBar(self.statusbar)

        self.btn_insert.clicked.connect(self.update)
        self.btn_insert.clicked.connect(self.text)

        self.retranslateUi(Update_component)
        QtCore.QMetaObject.connectSlotsByName(Update_component)

    def retranslateUi(self, Update_component):
        _translate = QtCore.QCoreApplication.translate
        Update_component.setWindowTitle(_translate("Update_component", "MainWindow"))
        self.label_4.setText(_translate("Update_component", "UPDATE A COMPONENT"))
        self.label_3.setText(_translate("Update_component", "UPDATE"))
        self.label_2.setText(_translate("Update_component", "Service Center Handphone & Laptop"))
        self.label.setText(_translate("Update_component", "Hai, Admin"))
        self.btn_insert.setText(_translate("Update_component", "Update Component"))
        self.label_6.setText(_translate("Update_component", "Kode Komponen"))
        self.label_9.setText(_translate("Update_component", "Masukkan Kode Komponen yang ingin anda update"))
        self.label_10.setText(_translate("Update_component", "Pilih menu yang ingin anda update"))
        self.comboBox.setItemText(0, _translate("Update_component", "ID komponen"))
        self.comboBox.setItemText(1, _translate("Update_component", "Nama komponen"))
        self.comboBox.setItemText(2, _translate("Update_component", "Harga komponen"))
        self.comboBox.setItemText(3, _translate("Update_component", "Qty"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Update_component = QtWidgets.QMainWindow()
    ui = Ui_Update_component()
    ui.setupUi(Update_component)
    Update_component.show()
    sys.exit(app.exec_())
