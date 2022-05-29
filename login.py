import oop_res
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
import sys
import database as db
from database import my_cursor
from S_screen import SplashScreen
# the following code is the login form code made with pyqt5 designer

# form class


class Form((QMainWindow)):
    def __init__(self):
        super(Form, self).__init__()
        loadUi('UIs\login_window.ui', self)
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
        self.ui = SignWindow()
        self.ui.setupUi()
        self.ui.show()

# sign up class


class SignWindow(QMainWindow):
    def __init__(self):
        super(SignWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        loadUi('UIs\SignForm.ui', self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.SignButton.clicked.connect(self.sign_check)
        self.BackButton.clicked.connect(self.close_function)
    # checking for the data if it valid to be added into the database

    def sign_check(self):
        user = self.UserName.text()
        email = self.email.text()
        password = self.Passwd.text()
        conf_password = self.conf_passwd.text()
        vpass = False
        vemail = False
        vname = False
        if len(user) == 0:
            self.Failure_msg.setText('Please input the user field.')
        else:
            vname = True
        if len(password) == 0 or len(conf_password) == 0:
            self.Failure_msg.setText('Please input the password fields.')
        else:
            if password != conf_password:
                self.Failure_msg.setText("passwords don't match")
            elif password == conf_password:
                vpass = True

        if len(email) == 0:
            self.Failure_msg.setText('Please input the email field.')
        else:
            if '@' not in email:
                self.Failure_msg.setText('email is not valid')
            elif '@' in email:
                vemail = True
        if vemail and vpass and vname:
            # if all value are valid we call a query to add a new admin
            db.add_admin(user, email, password)
            self.Failure_msg.setText('admin added successfully')

    def close_function(self):
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Form()
    main_window.show()
    sys.exit(app.exec_())
