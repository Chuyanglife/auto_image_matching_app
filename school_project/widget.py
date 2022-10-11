# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Desktop\大学\大三下\专题\UI python\widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(452, 282)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background image/pictureresult.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("QWidget#Form{\n"
"    \n"
"    \n"
"background-color: qlineargradient(spread:pad, x1:0.091, y1:0.102, x2:0.991, y2:0.997, stop:0 rgba(209, 107, 165, 255), stop:1 rgba(255, 255, 255, 255));}\n"
"    \n"
"\n"
"\n"
"\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 371, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 24pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(20, 40, 411, 141))
        self.listWidget.setStyleSheet("QListWidget{\n"
"border-radius:10px;\n"
"}")
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setWordWrap(False)
        self.listWidget.setObjectName("listWidget")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 200, 91, 61))
        self.pushButton_3.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);")
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 190, 61, 31))
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(170, 255, 255);\n"
"")
        self.pushButton.setIconSize(QtCore.QSize(15, 15))
        self.pushButton.setCheckable(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 190, 71, 31))
        self.pushButton_2.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(170, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 190, 71, 31))
        self.pushButton_4.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(170, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(20, 230, 311, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "相似系列圖片自動整理系統1.4"))
        self.label.setText(_translate("Form", "<strong>選擇的資料夾："))
        self.listWidget.setStatusTip(_translate("Form", "path"))
        self.listWidget.setSortingEnabled(False)
        self.pushButton_3.setToolTip(_translate("Form", "進入主畫面(4)"))
        self.pushButton_3.setStatusTip(_translate("Form", "進入主畫面"))
        self.pushButton_3.setText(_translate("Form", "進入主畫面"))
        self.pushButton_3.setShortcut(_translate("Form", "4"))
        self.pushButton.setToolTip(_translate("Form", "選擇資料夾(1)"))
        self.pushButton.setStatusTip(_translate("Form", "選擇資料夾"))
        self.pushButton.setText(_translate("Form", "選擇資料夾"))
        self.pushButton.setShortcut(_translate("Form", "1"))
        self.pushButton_2.setToolTip(_translate("Form", "開始掃描(2)"))
        self.pushButton_2.setStatusTip(_translate("Form", "開始掃描"))
        self.pushButton_2.setText(_translate("Form", "開始掃描"))
        self.pushButton_2.setShortcut(_translate("Form", "2"))
        self.pushButton_4.setToolTip(_translate("Form", "取消扫描(3)"))
        self.pushButton_4.setStatusTip(_translate("Form", "取消扫描"))
        self.pushButton_4.setText(_translate("Form", "取消扫描"))
        self.pushButton_4.setShortcut(_translate("Form", "3"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

