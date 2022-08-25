# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'service_center.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_MainWindow(object):
    def koneksi(self):
        con = pymysql.connect("localhost", "root", "", "univ_service_center")
        cur = con.cursor()

    def lihat(self):
        con = pymysql.connect("localhost", "root", "", "univ_service_center")
        cur = con.cursor()

        a = self.lineEdit_3.text()
        cur.execute("select * from service inner join user on service_operator = user_id where service_id='"+a+"' UNION select * from service inner join user on user_id = service_engineer where service_id='"+a+"' ")

        result = cur.fetchall()
        if (result):
            self.lineEdit.setText(""+str(result[0][11]))
            self.lineEdit_2.setText("" +str(result[1][11]))
            self.lineEdit_4.setText(""+str(result[0][5]))
            self.textEdit.setText(""+str(result[0][4]))
            self.lineEdit_5.setText("" + str(result[0][6]))
            self.lineEdit_6.setText(""+ str(result[0][7]))
            self.lineEdit_7.setText(""+ str(result[0][9]))

            cur.execute("select * from product where product_id='"+str(result[0][8])+"'")
            data = cur.fetchall()
            if(data):
                self.lineEdit_8.setText("" + str(data[0][1]))
            else:
                self.lineEdit_8.setText("Tidak Ada")

        else:
            self.lineEdit.setText("Tidak Ada")
            self.lineEdit_2.setText("Tidak Ada")
            self.textEdit.setText("Tidak Ada")
            self.lineEdit_4.setText("Tidak Ada")
            self.lineEdit_5.setText("Tidak Ada")
            self.lineEdit_6.setText("Tidak Ada")
            self.lineEdit_7.setText("Tidak Ada")
            self.lineEdit_8.setText("Tidak Ada")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(497, 428)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgb(180, 180, 180), stop:0 rgba(120, 120, 120));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 461, 391))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(180, 180, 180), stop:1 rgba(120, 120, 120));\n"
"}\n"
"*{\n"
"    font-family : century gothic;\n"
"}\n"
"QLabel{\n"
"    background : transparent;\n"
"}\n"
"QLineEdit{\n"
"    background : transparent;\n"
"    border : none;\n"
"}\n"
"QPushButton{\n"
"    background : transparent;\n"
"    border_radius : 20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background : pink;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 30, 261, 31))
        self.label.setStyleSheet("font-family : century gothic;\n"
"font-size : 24px;    \n"
"background : transparent;\n"
"font-weight : bold;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 71, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(90, 120, 113, 20))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 140, 113, 20))
        self.lineEdit_2.setStyleSheet("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 180, 71, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 160, 113, 20))
        self.lineEdit_4.setStyleSheet("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 160, 71, 21))
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(30, 200, 391, 151))
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(310, 140, 113, 20))
        self.lineEdit_5.setStyleSheet("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(250, 140, 71, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(250, 160, 71, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(310, 160, 113, 20))
        self.lineEdit_6.setStyleSheet("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(250, 180, 71, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_7.setGeometry(QtCore.QRect(310, 180, 113, 20))
        self.lineEdit_7.setStyleSheet("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 80, 181, 21))
        self.lineEdit_3.setStyleSheet("border : 1px solid;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 70, 91, 41))
        self.pushButton_2.setStyleSheet("border-radius: 20px;\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.lihat)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(250, 120, 71, 21))
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_8.setGeometry(QtCore.QRect(310, 120, 113, 20))
        self.lineEdit_8.setStyleSheet("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Status Transaksi Anda"))
        self.label_2.setText(_translate("MainWindow", "Operator : "))
        self.label_3.setText(_translate("MainWindow", "Engineer :"))
        self.label_4.setText(_translate("MainWindow", "Complaint : "))
        self.label_5.setText(_translate("MainWindow", "Garansi :"))
        self.label_6.setText(_translate("MainWindow", "Tanggal :"))
        self.label_7.setText(_translate("MainWindow", "Estimasi : "))
        self.label_8.setText(_translate("MainWindow", "Status : "))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Masukan ID Anda"))
        self.pushButton_2.setText(_translate("MainWindow", "Cek ID Anda"))
        self.label_9.setText(_translate("MainWindow", "Product : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
