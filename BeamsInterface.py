from beamsLogic import user
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 432)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(120, 150, 41, 21))
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(100, 180, 51, 16))
        self.label_10.setObjectName("label_10")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 245, 91, 21))
        self.label_6.setObjectName("label_6")

        self.linkInput = QtWidgets.QLineEdit(self.centralwidget)
        self.linkInput.setGeometry(QtCore.QRect(150, 120, 271, 20))
        self.linkInput.setObjectName("linkInput")

        self.messageInput = QtWidgets.QLineEdit(self.centralwidget)
        self.messageInput.setGeometry(QtCore.QRect(150, 210, 271, 20))
        self.messageInput.setObjectName("messageInput")

        self.emailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.emailInput.setGeometry(QtCore.QRect(150, 150, 271, 20))
        self.emailInput.setObjectName("emailInput")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(100, 190, 51, 61))
        self.label_8.setObjectName("label_8")

        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(150, 180, 271, 20))
        self.passwordInput.setObjectName("passwordInput")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 120, 61, 21))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)

        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(310, 240, 111, 31))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)

        self.confirmButton.setFont(font)
        self.confirmButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.confirmButton.setObjectName("confirmButton")
        self.confirmButton.clicked.connect(self.getInputs)

        self.timeInput = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeInput.setGeometry(QtCore.QRect(150, 240, 111, 31))
        self.timeInput.setObjectName("timeInput")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 40, 271, 31))

        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def getInputs(self):
        link = self.linkInput.text()
        email = self.emailInput.text()
        password = self.passwordInput.text()
        message = self.messageInput.text()
        time = self.timeInput.text().split(":")
        hours = time[0]
        minutes = time[1]

        if "0" in minutes:
            minutes = time[1][1]
    
        User(email, password, message, link, int(hours), startMinute = int(minutes)).startFunction()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Email"))
        self.label_10.setText(_translate("MainWindow", "Password"))
        self.label_6.setText(_translate("MainWindow", "Send Message At"))
        self.label_8.setText(_translate("MainWindow", "Message"))
        self.label_7.setText(_translate("MainWindow", "Teams Link"))
        self.confirmButton.setText(_translate("MainWindow", "Confirm"))
        self.label.setText(_translate("MainWindow", "Beams - MS Teams Bot"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
