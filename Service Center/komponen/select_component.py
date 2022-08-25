# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_component.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_select_component(object):
    def koneksi(self):
        db = pymysql.connect("localhost", "root", "", "test")
        cur = db.cursor()
    def cari(self):
        db = pymysql.connect("localhost", "root", "", "bingung")
        cur = db.cursor()
        a = self.lineEdit.text()
        cur.execute("SELECT * FROM component WHERE component_id='"+ a +"';")
        result = cur.fetchall()
        self.tableWidget.setRowCount(0)
        if (result):
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for colum_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        db.commit()
    def setupUi(self, select_component):
        self.koneksi()
        select_component.setObjectName("select_component")
        select_component.resize(780, 552)
        select_component.setStyleSheet("background-color: rgb(127, 127, 127);")
        self.centralwidget = QtWidgets.QWidget(select_component)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 40, 781, 16))
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
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 780, 42))
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
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 70, 781, 39))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 120, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btn_select = QtWidgets.QPushButton(self.centralwidget)
        self.btn_select.setGeometry(QtCore.QRect(470, 160, 75, 23))
        self.btn_select.setObjectName("btn_select")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(310, 120, 231, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 190, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(150, 230, 450, 192))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        select_component.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(select_component)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 21))
        self.menubar.setObjectName("menubar")
        select_component.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(select_component)
        self.statusbar.setObjectName("statusbar")
        select_component.setStatusBar(self.statusbar)

        self.btn_select.clicked.connect(self.cari)

        self.retranslateUi(select_component)
        QtCore.QMetaObject.connectSlotsByName(select_component)

    def retranslateUi(self, select_component):
        _translate = QtCore.QCoreApplication.translate
        select_component.setWindowTitle(_translate("select_component", "MainWindow"))
        self.label_3.setText(_translate("select_component", "Component"))
        self.label_2.setText(_translate("select_component", "Service Center Ice Tech"))
        self.label.setText(_translate("select_component", "Hai, Admin"))
        self.label_4.setText(_translate("select_component", "Searching For Component"))
        self.label_5.setText(_translate("select_component", "Masukkan kode komponen"))
        self.btn_select.setText(_translate("select_component", "Cari"))
        self.label_6.setText(_translate("select_component", "Berikut ini adalah produk yang anda cari "))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("select_component", "kode komponen"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("select_component", "nama komponen"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("select_component", "harga komponen"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("select_component", "Qty"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    select_component = QtWidgets.QMainWindow()
    ui = Ui_select_component()
    ui.setupUi(select_component)
    select_component.show()
    sys.exit(app.exec_())
