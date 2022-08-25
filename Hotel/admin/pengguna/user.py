# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from admin.pengguna.update_user import Ui_user_update
import pymysql

class Ui_user(object):
    def update(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_user_update()
        self.ui.setupUi(self.window)
        self.window.show()
    def select(self):
        db = pymysql.connect("localhost", "root", "", "hotel1")
        cur = db.cursor()
        cur.execute("SELECT id_user, nama, alamat, no_telp, role FROM user")
        result = cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        db.close()
    def setupUi(self, user):
        user.setObjectName("user")
        user.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(user)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_8.setGeometry(QtCore.QRect(750, 10, 31, 31))
        self.graphicsView_8.setStyleSheet("background-color:#c23616\n"
"")
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_9.setGeometry(QtCore.QRect(740, 0, 31, 31))
        self.graphicsView_9.setStyleSheet("background-color:#353b48")
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 0, 241, 41))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(150, 130, 531, 261))
        self.tableWidget.setStyleSheet("background-color:white;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(370, 65, 81, 51))
        self.frame_2.setStyleSheet("border-radius:20px;\n"
"background-color:#40739e;font-family : century gothic;color:#ffffff;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(15, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btn_all = QtWidgets.QPushButton(self.centralwidget)
        self.btn_all.setGeometry(QtCore.QRect(150, 410, 141, 41))
        self.btn_all.setStyleSheet("color: white;\n"
"  background-color: #c23616;\n"
"border-radius:20px;\n"
"\n"
"")
        self.btn_all.setObjectName("btn_all")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 45, 781, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(520, 410, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_update.sizePolicy().hasHeightForWidth())
        self.btn_update.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(-1)
        self.btn_update.setFont(font)
        self.btn_update.setStyleSheet("padding: 15px 25px;\n"
"  font-size: 13px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: white;\n"
"  background-color: #40739e;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;")
        self.btn_update.setObjectName("btn_update")
        user.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(user)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        user.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(user)
        self.statusbar.setObjectName("statusbar")
        user.setStatusBar(self.statusbar)

        self.btn_all.clicked.connect(self.select)
        self.btn_update.clicked.connect(self.update)

        self.retranslateUi(user)
        QtCore.QMetaObject.connectSlotsByName(user)

    def retranslateUi(self, user):
        _translate = QtCore.QCoreApplication.translate
        user.setWindowTitle(_translate("user", "MainWindow"))
        self.label.setText(_translate("user", "HOTEL SUKAMAJU"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("user", "ID User"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("user", "Nama"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("user", "Alamat"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("user", "No. Telp"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("user", "Jabatan"))
        self.label_2.setText(_translate("user", "USER"))
        self.btn_all.setText(_translate("user", "Lihat Semua User"))
        self.btn_update.setText(_translate("user", "Update User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    user = QtWidgets.QMainWindow()
    ui = Ui_user()
    ui.setupUi(user)
    user.show()
    sys.exit(app.exec_())
