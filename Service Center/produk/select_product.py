# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_product.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_select_product(object):
    def select(self):
        db = pymysql.connect("localhost", "root", "", "bingung")
        cur = db.cursor()
        a = self.lineEdit.text()
        cur.execute("SELECT * FROM product WHERE product_id='" + a + "'")
        results = cur.fetchall()
        if (results):
            for row in results:
                self.lineEdit_2.setText("" + row[1])
                self.plainTextEdit.setPlainText("" + row[2])
                self.lineEdit_3.setText("" + row[3])
        else:
            self.lineEdit_2.setText("Tidak ada")
            self.plainTextEdit.setPlainText("Tidak ada")
            self.lineEdit_3.setText("Tidak ada")
        db.commit()
    def setupUi(self, select_product):
        select_product.setObjectName("select_product")
        select_product.resize(800, 600)
        select_product.setStyleSheet("background-color: rgb(112, 112, 112);")
        self.centralwidget = QtWidgets.QWidget(select_product)
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
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 811, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(16)
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
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 60, 791, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Kozuka Mincho Pro H")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 150, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 150, 231, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.btn_select = QtWidgets.QPushButton(self.centralwidget)
        self.btn_select.setGeometry(QtCore.QRect(470, 190, 75, 23))
        self.btn_select.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(170, 255, 0);")
        self.btn_select.setObjectName("btn_select")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 220, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 270, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(130, 300, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(130, 420, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 270, 231, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(310, 300, 231, 111))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 420, 231, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        select_product.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(select_product)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        select_product.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(select_product)
        self.statusbar.setObjectName("statusbar")
        select_product.setStatusBar(self.statusbar)

        self.btn_select.clicked.connect(self.select)

        self.retranslateUi(select_product)
        QtCore.QMetaObject.connectSlotsByName(select_product)

    def retranslateUi(self, select_product):
        _translate = QtCore.QCoreApplication.translate
        select_product.setWindowTitle(_translate("select_product", "MainWindow"))
        self.label_3.setText(_translate("select_product", "SEARCHING"))
        self.label_2.setText(_translate("select_product", "Service Center"))
        self.label.setText(_translate("select_product", "Hai, Admin"))
        self.label_4.setText(_translate("select_product", "Searching For Product"))
        self.label_5.setText(_translate("select_product", "Masukkan kode produk"))
        self.btn_select.setText(_translate("select_product", "Cari"))
        self.label_6.setText(_translate("select_product", "Berikut ini adalah produk yang anda cari "))
        self.label_7.setText(_translate("select_product", "Nama Produk"))
        self.label_8.setText(_translate("select_product", "Spesifikasi Produk"))
        self.label_9.setText(_translate("select_product", "Tipe Produk"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    select_product = QtWidgets.QMainWindow()
    ui = Ui_select_product()
    ui.setupUi(select_product)
    select_product.show()
    sys.exit(app.exec_())
