# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreateStudent.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateStudent(object):
    def setupUi(self, CreateStudent):
        CreateStudent.setObjectName("CreateStudent")
        CreateStudent.resize(1280, 832)
        CreateStudent.setMinimumSize(QtCore.QSize(1280, 832))
        CreateStudent.setMaximumSize(QtCore.QSize(1280, 832))
        CreateStudent.setStyleSheet("font-family: \'Open Sans\';")
        self.centralwidget = QtWidgets.QWidget(CreateStudent)
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 832))
        self.centralwidget.setMaximumSize(QtCore.QSize(1280, 832))
        self.centralwidget.setStyleSheet("background:white;")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMinimumSize(QtCore.QSize(457, 530))
        self.widget_3.setMaximumSize(QtCore.QSize(457, 530))
        self.widget_3.setStyleSheet("#Qlabel{\n"
"color: #96E49ECC;\n"
"\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #595959;\n"
"")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #595959;\n"
"")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #595959;\n"
"")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #595959;\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.firstname = QtWidgets.QLineEdit(self.widget_3)
        self.firstname.setMinimumSize(QtCore.QSize(172, 41))
        self.firstname.setMaximumSize(QtCore.QSize(172, 41))
        self.firstname.setStyleSheet("border: 1px solid #ABABAB;\n"
"border-radius:    4px;\n"
"padding: 12px;\n"
"font-size: 14px;")
        self.firstname.setObjectName("firstname")
        self.gridLayout.addWidget(self.firstname, 1, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.widget_3)
        self.password.setMinimumSize(QtCore.QSize(440, 41))
        self.password.setMaximumSize(QtCore.QSize(368, 41))
        self.password.setStyleSheet("border: 1px solid #ABABAB;\n"
"border-radius:    4px;\n"
"padding: 12px;\n"
"font-size: 14px;")
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 8, 0, 1, 1)
        self.email = QtWidgets.QLineEdit(self.widget_3)
        self.email.setMinimumSize(QtCore.QSize(440, 41))
        self.email.setMaximumSize(QtCore.QSize(368, 41))
        self.email.setStyleSheet("border: 1px solid #ABABAB;\n"
"border-radius:    4px;\n"
"padding: 12px;\n"
"font-size: 14px;")
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 6, 0, 1, 1)
        self.username = QtWidgets.QLineEdit(self.widget_3)
        self.username.setMinimumSize(QtCore.QSize(440, 41))
        self.username.setMaximumSize(QtCore.QSize(368, 41))
        self.username.setStyleSheet("border: 1px solid #ABABAB;\n"
"border-radius:    4px;\n"
"padding: 12px;\n"
"font-size: 14px;")
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 3, 0, 1, 1)
        self.signup_button = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(16)
        self.signup_button.setFont(font)
        self.signup_button.setStyleSheet("background: #33E765;\n"
"border:none;\n"
"width: 173.27px;\n"
"height: 41.26px;\n"
"top: 630px;\n"
"left: 155px;\n"
"gap: 0px;\n"
"border-radius: 3px;\n"
"opacity: 0px;\n"
"color: White;\n"
"")
        self.signup_button.setObjectName("signup_button")
        self.gridLayout.addWidget(self.signup_button, 12, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: #595959;\n"
"")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 0, 1, 1)
        self.promo = QtWidgets.QComboBox(self.widget_3)
        self.promo.setMinimumSize(QtCore.QSize(165, 41))
        self.promo.setMaximumSize(QtCore.QSize(165, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 105, 105, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.promo.setPalette(palette)
        self.promo.setStyleSheet("*{\n"
"border: 1px solid #ABABAB;\n"
"border-radius:    4px;\n"
"padding: 12px;\n"
"font-size: 14px;\n"
"color: #595959;\n"
"\n"
"\n"
"}\n"
"QComboBox::down-arrow {\n"
"    border: none !important;\n"
"    background-color: transparent !important;\n"
"    image: url(\":/icons/icons/caret_down.png\"); /* or any other styles */\n"
"    \n"
"\n"
"}")
        self.promo.setObjectName("promo")
        self.promo.addItem("")
        self.promo.addItem("")
        self.gridLayout.addWidget(self.promo, 10, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #595959;\n"
"")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 9, 1, 1, 1)
        self.lastname = QtWidgets.QLineEdit(self.widget_3)
        self.lastname.setMinimumSize(QtCore.QSize(172, 41))
        self.lastname.setMaximumSize(QtCore.QSize(172, 41))
        self.lastname.setStyleSheet("border: 1px solid #ABABAB;\n"
"border-radius:    4px;\n"
"padding: 12px;\n"
"font-size: 14px;")
        self.lastname.setObjectName("lastname")
        self.gridLayout.addWidget(self.lastname, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #595959;\n"
"")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.groupe = QtWidgets.QComboBox(self.widget_3)
        self.groupe.setMinimumSize(QtCore.QSize(165, 41))
        self.groupe.setMaximumSize(QtCore.QSize(165, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 54, 70, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 54, 70, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 127, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(89, 89, 89))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(105, 54, 70, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        self.groupe.setPalette(palette)
        self.groupe.setStyleSheet("*{\n"
"border: 1px solid #ABABAB;\n"
"border-radius:    4px;\n"
"padding: 12px;\n"
"font-size: 14px;\n"
"color: #595959;\n"
"\n"
"}\n"
"QComboBox::down-arrow {\n"
"    border:none;\n"
"    image: url(\":/icons/icons/caret_down.png\"); /* or any other styles */\n"
"\n"
"}")
        self.groupe.setObjectName("groupe")
        self.groupe.addItem("")
        self.groupe.addItem("")
        self.gridLayout.addWidget(self.groupe, 10, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget_3)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 11, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_3, 0, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(680, 935))
        self.widget_2.setStyleSheet("*{\n"
"background-image: url(\":/icons/icons/Vector (2).png\");\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout.addWidget(self.widget_2)
        CreateStudent.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateStudent)
        QtCore.QMetaObject.connectSlotsByName(CreateStudent)

    def retranslateUi(self, CreateStudent):
        _translate = QtCore.QCoreApplication.translate
        CreateStudent.setWindowTitle(_translate("CreateStudent", "MainWindow"))
        self.label.setText(_translate("CreateStudent", "Create Student"))
        self.label_5.setText(_translate("CreateStudent", "Email"))
        self.label_6.setText(_translate("CreateStudent", "Password"))
        self.label_4.setText(_translate("CreateStudent", "User Name"))
        self.label_2.setText(_translate("CreateStudent", "First Name"))
        self.firstname.setPlaceholderText(_translate("CreateStudent", "Enter text"))
        self.password.setPlaceholderText(_translate("CreateStudent", "Enter text"))
        self.email.setPlaceholderText(_translate("CreateStudent", "Enter text"))
        self.username.setPlaceholderText(_translate("CreateStudent", "Enter text"))
        self.signup_button.setText(_translate("CreateStudent", "Sign Up"))
        self.label_7.setText(_translate("CreateStudent", "Promo"))
        self.promo.setItemText(0, _translate("CreateStudent", "Option 1"))
        self.promo.setItemText(1, _translate("CreateStudent", "Option 2"))
        self.label_8.setText(_translate("CreateStudent", "Groupe"))
        self.lastname.setPlaceholderText(_translate("CreateStudent", "Enter text"))
        self.label_3.setText(_translate("CreateStudent", "Last Name"))
        self.groupe.setItemText(0, _translate("CreateStudent", "Option 1"))
        self.groupe.setItemText(1, _translate("CreateStudent", "OPtion 2"))
import resources_rc
