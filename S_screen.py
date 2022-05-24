from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
from PySide2 import QtCore, QtGui, QtWidgets
from windows import MainWindow
# GLOBALS
counter = 0
jumper = 10


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(340, 340)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBarBase = QFrame(self.centralwidget)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(10, 10, 320, 320))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBarBase)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
                                            "	border-radius: 150px;\n"
                                            "	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgb(10,70,86));\n"
                                            "}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBarBase)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet(u"QFrame{\n"
                                      "	border-radius: 150px;\n"
                                      "	background-color: rgba(189, 189, 189, 120);\n"
                                      "}")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBarBase)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(25, 25, 270, 270))
        self.container.setStyleSheet(u"QFrame{\n"
                                     "	border-radius: 135px;\n"
                                     "	background-color: rgb(189, 189, 189);\n"
                                     "}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.container)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 50, 193, 191))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelTitle = QLabel(self.widget)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet(u"background-color: none;\n"
                                      "color: #FFFFFF")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)

        self.labelPercentage = QLabel(self.widget)
        self.labelPercentage.setObjectName(u"labelPercentage")
        font1 = QFont()
        font1.setFamily(u"Roboto Thin")
        font1.setPointSize(60)
        self.labelPercentage.setFont(font1)
        self.labelPercentage.setStyleSheet(u"background-color: none;\n"
                                           "color:rgb(10, 70, 86)")
        self.labelPercentage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPercentage, 1, 0, 1.2, 1.2)

        self.labelLoadingInfo = QLabel(self.widget)
        self.labelLoadingInfo.setObjectName(u"labelLoadingInfo")
        self.labelLoadingInfo.setMinimumSize(QSize(0, 20))
        self.labelLoadingInfo.setMaximumSize(QSize(16777215, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(9)
        self.labelLoadingInfo.setFont(font2)
        self.labelLoadingInfo.setStyleSheet(u"QLabel{\n"
                                            "	border-radius: 10px;	\n"
                                            "	background-color: rgb(10, 70, 86);\n"
                                            "	color: #FFFFFF;\n"
                                            "	margin-left: 40px;\n"
                                            "	margin-right: 40px;\n"
                                            "}")
        self.labelLoadingInfo.setFrameShape(QFrame.NoFrame)
        self.labelLoadingInfo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelLoadingInfo, 2, 0, 1, 1)

        self.labelCredits = QLabel(self.widget)
        self.labelCredits.setObjectName(u"labelCredits")
        self.labelCredits.setFont(font2)
        self.labelCredits.setStyleSheet(u"background-color: none;\n"
                                        "color: rgb(18, 118, 145);")
        self.labelCredits.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelCredits, 3, 0, 1, 1)

        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate(
            "SplashScreen", u"MainWindow", None))
        self.labelTitle.setText(QCoreApplication.translate(
            "SplashScreen", u"<html><head/><body><p><span style=\" font-weight:600; color:rgb(10, 70, 86);\">EDU</span> Mangment System </p></body></html>", None))
        self.labelPercentage.setText(QCoreApplication.translate(
            "SplashScreen", u"<p><span style=\" font-size:60pt;\">0</span><span style=\" font-size:52pt; vertical-align:super;\">%</span></p>", None))
        self.labelLoadingInfo.setText(QCoreApplication.translate(
            "SplashScreen", u"loading...", None))
        self.labelCredits.setText(QCoreApplication.translate(
            "SplashScreen", u"by: Mohamed Elbahy", None))


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        # ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        # Set background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(15)

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    def progress(self):
        global counter
        global jumper
        value = counter

        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:60pt;">{VALUE}</span><span style=" font-size:52pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if(value > jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(newHtml)
            jumper += 7

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100:
            value = 1.000
        self.progressBarValue(value)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 0.7

    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(10,70,86, 255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace(
            "{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)
