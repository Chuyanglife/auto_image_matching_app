# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\Desktop\school_project\ui_view\splash_screen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        SplashScreen.setObjectName("SplashScreen")
        SplashScreen.resize(429, 283)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/background image/pictureresult.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SplashScreen.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(SplashScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(56, 58, 89);\n"
"    color: rgb(220, 220, 220);\n"
"    border-radius :10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_tittle = QtWidgets.QLabel(self.frame)
        self.label_tittle.setGeometry(QtCore.QRect(0, 40, 401, 81))
        self.label_tittle.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_tittle.setFont(font)
        self.label_tittle.setStyleSheet("color: rgb(254, 121, 199);")
        self.label_tittle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tittle.setObjectName("label_tittle")
        self.label_description = QtWidgets.QLabel(self.frame)
        self.label_description.setGeometry(QtCore.QRect(10, 100, 391, 21))
        self.label_description.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(30, 180, 341, 21))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    background-color: rgb(98, 114, 164);\n"
"    color: rgb(200, 200, 200);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    border-radius:10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_loading = QtWidgets.QLabel(self.frame)
        self.label_loading.setGeometry(QtCore.QRect(10, 210, 391, 21))
        self.label_loading.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_loading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.verticalLayout.addWidget(self.frame)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QtCore.QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QtCore.QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate("SplashScreen", "MainWindow"))
        self.label_tittle.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600;\">相似系列圖片自動整理系統</span></p></body></html>"))
        self.label_description.setText(_translate("SplashScreen", "<html><head/><body><p><span style=\" font-weight:600;\">照片匹配 </span>電腦app</p></body></html>"))
        self.label_loading.setText(_translate("SplashScreen", "loading....."))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SplashScreen = QtWidgets.QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(SplashScreen)
    SplashScreen.show()
    sys.exit(app.exec_())

