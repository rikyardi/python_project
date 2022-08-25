# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_product.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_delete_product(object):
    def delete(self):
        db = pymysql.connect("localhost", "root", "", "bingung")
        cur = db.cursor()
        a = self.lineEdit_kd.text()
        cur.execute("DELETE FROM product WHERE product_id='" + a + "';")
        db.commit()
    def setupUi(self, delete_product):
        delete_product.setObjectName("delete_product")
        delete_product.resize(800, 600)
        delete_product.setStyleSheet("background-color: rgb(112, 112, 112);")
        self.centralwidget = QtWidgets.QWidget(delete_product)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 60, 799, 39))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
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
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
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
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 120, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_kd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_kd.setGeometry(QtCore.QRect(300, 130, 251, 20))
        self.lineEdit_kd.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_kd.setObjectName("lineEdit_kd")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(470, 170, 75, 23))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(170, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(130, 240, 491, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_success = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(17)
        self.label_success.setFont(font)
        self.label_success.setText("")
        self.label_success.setAlignment(QtCore.Qt.AlignCenter)
        self.label_success.setObjectName("label_success")
        self.horizontalLayout_2.addWidget(self.label_success)
        delete_product.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(delete_product)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        delete_product.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(delete_product)
        self.statusbar.setObjectName("statusbar")
        delete_product.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.delete)

        self.retranslateUi(delete_product)
        QtCore.QMetaObject.connectSlotsByName(delete_product)

    def retranslateUi(self, delete_product):
        _translate = QtCore.QCoreApplication.translate
        delete_product.setWindowTitle(_translate("delete_product", "MainWindow"))
        self.label_4.setText(_translate("delete_product", "DELETE A PRODUCT"))
        self.label_3.setText(_translate("delete_product", "Delete"))
        self.label_2.setText(_translate("delete_product", "Service Center "))
        self.label.setText(_translate("delete_product", "Hai, Admin"))
        self.label_5.setText(_translate("delete_product", "Kode produk yang ingin dihapus"))
        self.pushButton.setText(_translate("delete_product", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete_product = QtWidgets.QMainWindow()
    ui = Ui_delete_product()
    ui.setupUi(delete_product)
    delete_product.show()
    sys.exit(app.exec_())
