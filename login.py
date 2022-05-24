import oop_res
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
import sys
import database as db
from database import my_cursor
import Sign
from S_screen import SplashScreen
# the following code is the login form code made with pyqt5 designer

# form class


class Form(QDialog):
    def __init__(self):
        super(Form, self).__init__()
        loadUi('UIs\loginForm.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.LoginButton.clicked.connect(self.login_function)
        self.Sign_upButton.clicked.connect(self.open_signForm)

# a function to check if the input values matches the ones in the data base or not

    def login_function(self):
        user = self.UserName.text()
        password = self.Passwd.text()
        if len(user) == 0 or len(password) == 0:
            self.Failure_msg.setText("Please input all fields.")

        else:
            res = db.login_check(user)
            # check if query result = password
            if res == password:
                self.close()
                self.ui = SplashScreen()
                # self.ui.setupUi()
                # self.ui.show()
            else:
                self.Failure_msg.setText('wrong password or user name')

    def open_signForm(self):
        self.ui = Sign.SignWindow()
        self.ui.setupUi()
        self.ui.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Form()
    main_window.show()
    sys.exit(app.exec_())
