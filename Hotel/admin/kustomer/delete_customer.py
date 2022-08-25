# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_customer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_delete_customer(object):
    def delete(self):
        db = pymysql.connect("localhost","root","","hotel1")
        cur = db.cursor()
        a = self.lineEdit.text()
        cur.execute("DELETE FROM customer WHERE id_customer ='"+a+"'; ")
        db.commit()

    def setupUi(self, delete_customer):
        delete_customer.setObjectName("delete_customer")
        delete_customer.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(delete_customer)
        self.centralwidget.setObjectName("centralwidget")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 65, 781, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(320, 90, 181, 51))
        self.frame_2.setStyleSheet("border-radius:20px;\n"
"background-color:#40739e;font-family : century gothic;color:#ffffff;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(15, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 5, 781, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_8.setGeometry(QtCore.QRect(750, 30, 31, 31))
        self.graphicsView_8.setStyleSheet("background-color:#c23616\n"
"")
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 241, 41))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_9.setGeometry(QtCore.QRect(740, 20, 31, 31))
        self.graphicsView_9.setStyleSheet("background-color:#353b48")
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(230, 240, 391, 201))
        self.frame.setStyleSheet("background-color: #353b48;\n"
"color:#ffffff;\n"
"border-radius: 20px;\n"
"font-family:century gothic;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_delete = QtWidgets.QPushButton(self.frame)
        self.btn_delete.setGeometry(QtCore.QRect(230, 120, 111, 41))
        self.btn_delete.setStyleSheet("border-radius:20px;\n"
"background-color:#c23616;font-family : century gothic;color:#ffffff;")
        self.btn_delete.setObjectName("btn_delete")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(80, 30, 231, 31))
        font = QtGui.QFont()
        font.setFamily("century gothic")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(70, 70, 251, 20))
        self.lineEdit.setStyleSheet("border:none;\n"
"border-bottom:1px solid white;\n"
"background:transparent;\n"
"color:#ffffff;")
        self.lineEdit.setObjectName("lineEdit")
        delete_customer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(delete_customer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        delete_customer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(delete_customer)
        self.statusbar.setObjectName("statusbar")
        delete_customer.setStatusBar(self.statusbar)

        self.btn_delete.clicked.connect(self.delete)

        self.retranslateUi(delete_customer)
        QtCore.QMetaObject.connectSlotsByName(delete_customer)

    def retranslateUi(self, delete_customer):
        _translate = QtCore.QCoreApplication.translate
        delete_customer.setWindowTitle(_translate("delete_customer", "MainWindow"))
        self.label_2.setText(_translate("delete_customer", "Delete Customer"))
        self.label.setText(_translate("delete_customer", "HOTELSUKAMAJU"))
        self.btn_delete.setText(_translate("delete_customer", "Delete"))
        self.label_5.setText(_translate("delete_customer", "ID Customer yang ingin dihapus"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete_customer = QtWidgets.QMainWindow()
    ui = Ui_delete_customer()
    ui.setupUi(delete_customer)
    delete_customer.show()
    sys.exit(app.exec_())
