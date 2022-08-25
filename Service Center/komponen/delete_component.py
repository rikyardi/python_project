# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_component.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_Delete_component(object):
    def delete(self):
        db = pymysql.connect("localhost", "root", "", "bingung")
        cur = db.cursor()
        a = self.lineEdit.text()
        cur.execute("DELETE FROM component WHERE component_id='" + a + "';")
        db.commit()

    def setupUi(self, Delete_component):
        Delete_component.setObjectName("Delete_component")
        Delete_component.resize(800, 600)
        Delete_component.setStyleSheet("background-color: rgb(112, 112, 112);")
        self.centralwidget = QtWidgets.QWidget(Delete_component)
        self.centralwidget.setObjectName("centralwidget")
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 260, 491, 191))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_success = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(17)
        self.label_success.setFont(font)
        self.label_success.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_success.setAlignment(QtCore.Qt.AlignCenter)
        self.label_success.setObjectName("label_success")
        self.horizontalLayout_2.addWidget(self.label_success)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 150, 251, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 140, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(500, 190, 75, 23))
        self.btn_delete.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(170, 255, 0);")
        self.btn_delete.setObjectName("btn_delete")
        Delete_component.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Delete_component)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Delete_component.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Delete_component)
        self.statusbar.setObjectName("statusbar")
        Delete_component.setStatusBar(self.statusbar)

        self.btn_delete.clicked.connect(self.delete)

        self.retranslateUi(Delete_component)
        QtCore.QMetaObject.connectSlotsByName(Delete_component)

    def retranslateUi(self, Delete_component):
        _translate = QtCore.QCoreApplication.translate
        Delete_component.setWindowTitle(_translate("Delete_component", "MainWindow"))
        self.label_4.setText(_translate("Delete_component", "DELETE A COMPONENT"))
        self.label_3.setText(_translate("Delete_component", "DELETE"))
        self.label_2.setText(_translate("Delete_component", "Service Center Handphone & Laptop"))
        self.label.setText(_translate("Delete_component", "Hai, Admin"))
        self.label_success.setText(_translate("Delete_component", "Masukkan kode produk yang ingin anda hapus"))
        self.label_5.setText(_translate("Delete_component", "Kode produk yang ingin dihapus"))
        self.btn_delete.setText(_translate("Delete_component", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Delete_component = QtWidgets.QMainWindow()
    ui = Ui_Delete_component()
    ui.setupUi(Delete_component)
    Delete_component.show()
    sys.exit(app.exec_())
