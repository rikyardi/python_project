# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from produk.produk import Ui_Product
from komponen.komponen import Ui_component
from garansi.guarantee import Ui_guarantee
from user.user import Ui_User
class Ui_Dashboard(object):
    def user(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_User()
        self.ui.setupUi(self.window)
        self.window.show()
    def garansi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_guarantee()
        self.ui.setupUi(self.window)
        self.window.show()
    def komponen(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_component()
        self.ui.setupUi(self.window)
        self.window.show()
    def product(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Product()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, Dashboard):
        Dashboard.setObjectName("Dashboard")
        Dashboard.resize(805, 458)
        Dashboard.setStyleSheet("background-color: rgb(112, 112, 112);")
        self.centralwidget = QtWidgets.QWidget(Dashboard)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 50, 781, 16))
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
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 120, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 780, 42))
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
        self.btn_operator = QtWidgets.QPushButton(self.centralwidget)
        self.btn_operator.setGeometry(QtCore.QRect(420, 190, 211, 53))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_operator.sizePolicy().hasHeightForWidth())
        self.btn_operator.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_operator.setFont(font)
        self.btn_operator.setStyleSheet("padding: 15px 25px;\n"
"  font-size: 24px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: rgb(60, 1, 255);\n"
"  background-color: rgb(0, 255, 238);\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;")
        self.btn_operator.setObjectName("btn_operator")
        self.btn_garansi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_garansi.setGeometry(QtCore.QRect(420, 280, 211, 53))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_garansi.sizePolicy().hasHeightForWidth())
        self.btn_garansi.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_garansi.setFont(font)
        self.btn_garansi.setStyleSheet("padding: 15px 25px;\n"
"  font-size: 24px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: rgb(60, 1, 255);\n"
"  background-color: rgb(0, 255, 238);\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;")
        self.btn_garansi.setObjectName("btn_garansi")
        self.btn_produk = QtWidgets.QPushButton(self.centralwidget)
        self.btn_produk.setGeometry(QtCore.QRect(150, 190, 211, 53))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_produk.sizePolicy().hasHeightForWidth())
        self.btn_produk.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_produk.setFont(font)
        self.btn_produk.setStyleSheet("  padding: 15px 25px;\n"
"  font-size: 24px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: rgb(60, 1, 255);\n"
"  background-color: rgb(0, 255, 238);\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;\n"
"hover{color:red}")
        self.btn_produk.setObjectName("btn_produk")
        self.btn_komponen = QtWidgets.QPushButton(self.centralwidget)
        self.btn_komponen.setGeometry(QtCore.QRect(150, 280, 211, 53))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_komponen.sizePolicy().hasHeightForWidth())
        self.btn_komponen.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_komponen.setFont(font)
        self.btn_komponen.setStyleSheet("padding: 15px 25px;\n"
"  font-size: 24px;\n"
"  text-align: center;\n"
"  cursor: pointer;\n"
"  outline: none;\n"
"color: rgb(60, 1, 255);\n"
"  background-color: rgb(0, 255, 238);\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"  box-shadow: 0 9px #999;")
        self.btn_komponen.setObjectName("btn_komponen")
        Dashboard.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Dashboard)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 21))
        self.menubar.setObjectName("menubar")
        self.menuDashboard = QtWidgets.QMenu(self.menubar)
        self.menuDashboard.setObjectName("menuDashboard")
        Dashboard.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Dashboard)
        self.statusbar.setObjectName("statusbar")
        Dashboard.setStatusBar(self.statusbar)
        self.actionProduk = QtWidgets.QAction(Dashboard)
        self.actionProduk.setObjectName("actionProduk")
        self.actionGaransi = QtWidgets.QAction(Dashboard)
        self.actionGaransi.setObjectName("actionGaransi")
        self.actionOperator = QtWidgets.QAction(Dashboard)
        self.actionOperator.setObjectName("actionOperator")
        self.actionKomponen = QtWidgets.QAction(Dashboard)
        self.actionKomponen.setObjectName("actionKomponen")
        self.menuDashboard.addAction(self.actionProduk)
        self.menuDashboard.addAction(self.actionGaransi)
        self.menuDashboard.addAction(self.actionOperator)
        self.menuDashboard.addAction(self.actionKomponen)
        self.menubar.addAction(self.menuDashboard.menuAction())

        self.btn_komponen.clicked.connect(self.komponen)
        self.actionKomponen.triggered.connect(self.komponen)
        self.btn_produk.clicked.connect(self.product)
        self.actionProduk.triggered.connect(self.product)
        self.btn_garansi.clicked.connect(self.garansi)
        self.actionGaransi.triggered.connect(self.garansi)
        self.btn_operator.clicked.connect(self.user)
        self.actionOperator.triggered.connect(self.user)

        self.retranslateUi(Dashboard)
        QtCore.QMetaObject.connectSlotsByName(Dashboard)

    def retranslateUi(self, Dashboard):
        _translate = QtCore.QCoreApplication.translate
        Dashboard.setWindowTitle(_translate("Dashboard", "MainWindow"))
        self.label_4.setText(_translate("Dashboard", "PILIH YANG INGIN ANDA KERJAKAN"))
        self.label_3.setText(_translate("Dashboard", "Dashboard"))
        self.label_2.setText(_translate("Dashboard", "Service Center Handphone & Laptop"))
        self.label.setText(_translate("Dashboard", "Hai, Admin"))
        self.btn_operator.setText(_translate("Dashboard", "User"))
        self.btn_garansi.setText(_translate("Dashboard", "Garansi"))
        self.btn_produk.setText(_translate("Dashboard", "Produk"))
        self.btn_komponen.setText(_translate("Dashboard", "Komponen"))
        self.menuDashboard.setTitle(_translate("Dashboard", "Dashboard"))
        self.actionProduk.setText(_translate("Dashboard", "Produk"))
        self.actionProduk.setStatusTip(_translate("Dashboard", "Open Product"))
        self.actionGaransi.setText(_translate("Dashboard", "Garansi"))
        self.actionGaransi.setStatusTip(_translate("Dashboard", "Open Garansi"))
        self.actionOperator.setText(_translate("Dashboard", "User"))
        self.actionOperator.setStatusTip(_translate("Dashboard", "Open User"))
        self.actionKomponen.setText(_translate("Dashboard", "Komponen"))
        self.actionKomponen.setStatusTip(_translate("Dashboard", "Open Komponen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dashboard = QtWidgets.QMainWindow()
    ui = Ui_Dashboard()
    ui.setupUi(Dashboard)
    Dashboard.show()
    sys.exit(app.exec_())
