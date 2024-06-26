# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChatloginPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(1200, 832)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setMinimumSize(QtCore.QSize(1200, 832))
        Login.setMaximumSize(QtCore.QSize(1200, 832))
        Login.setStyleSheet("font-family: \'Open Sans\';")
        self.centralwidget = QtWidgets.QWidget(Login)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 832))
        self.centralwidget.setStyleSheet("background:white;")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setMinimumSize(QtCore.QSize(200, 935))
        self.main_widget.setMaximumSize(QtCore.QSize(550, 935))
        self.main_widget.setObjectName("main_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 170, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.signin_widget = QtWidgets.QWidget(self.main_widget)
        self.signin_widget.setMinimumSize(QtCore.QSize(0, 200))
        self.signin_widget.setObjectName("signin_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.signin_widget)
        self.verticalLayout_2.setContentsMargins(60, -1, -1, -1)
        self.verticalLayout_2.setSpacing(50)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.signin_widget)
        self.label.setMinimumSize(QtCore.QSize(380, 50))
        self.label.setMaximumSize(QtCore.QSize(290, 37))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.email = QtWidgets.QLineEdit(self.signin_widget)
        self.email.setMinimumSize(QtCore.QSize(380, 66))
        self.email.setMaximumSize(QtCore.QSize(380, 66))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        self.email.setFont(font)
        self.email.setStyleSheet("border: 2px solid #B5B5B5;\n"
"border-radius:10px;\n"
"color: #9A9A9A;\n"
"padding-left:20px;\n"
"")
        self.email.setObjectName("email")
        self.verticalLayout_2.addWidget(self.email)
        self.password = QtWidgets.QLineEdit(self.signin_widget)
        self.password.setMinimumSize(QtCore.QSize(380, 66))
        self.password.setMaximumSize(QtCore.QSize(380, 66))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        self.password.setFont(font)
        self.password.setStyleSheet("border: 2px solid #B5B5B5;\n"
"border-radius:10px;\n"
"color: #9A9A9A;\n"
"padding-left:20px;\n"
"")
        self.password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password.setInputMask("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout_2.addWidget(self.password)
        self.signinButton = QtWidgets.QPushButton(self.signin_widget)
        self.signinButton.setMinimumSize(QtCore.QSize(380, 66))
        self.signinButton.setMaximumSize(QtCore.QSize(380, 66))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        self.signinButton.setFont(font)
        self.signinButton.setStyleSheet("background: #33E765;\n"
"border:none;\n"
"color:white;\n"
"border-radius: 9px;")
        self.signinButton.setObjectName("signinButton")
        self.verticalLayout_2.addWidget(self.signinButton)
        self.verticalLayout.addWidget(self.signin_widget, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 223, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.main_widget)
        self.background_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background_widget.sizePolicy().hasHeightForWidth())
        self.background_widget.setSizePolicy(sizePolicy)
        self.background_widget.setMinimumSize(QtCore.QSize(680, 935))
        self.background_widget.setMaximumSize(QtCore.QSize(680, 935))
        self.background_widget.setStyleSheet("*{\n"
"background-image: url(\":/icons/icons/Vector (3).png\");\n"
"}")
        self.background_widget.setObjectName("background_widget")
        self.horizontalLayout.addWidget(self.background_widget)
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.label.setText(_translate("Login", "Welcome Back"))
        self.email.setPlaceholderText(_translate("Login", "Your Email"))
        self.password.setPlaceholderText(_translate("Login", "Your Password"))
        self.signinButton.setText(_translate("Login", "Sign in"))
import resources_rc
