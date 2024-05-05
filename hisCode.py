def __init__(self):
    QMainWindow.__init__(self)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)
    self.resize(self.minimumSizeHint())
    self.ui.widget_4.hide()

    self.ui.detailsMenuButton.clicked.connect(lambda: widget.resize(1800, 1000))
    self.ui.XButton.clicked.connect(lambda: widget.resize(1368, 1000))
    self.ui.logoutButton.clicked.connect(self.goToLoginPage)

    # Chats navigation
    self.ui.promoButton.clicked.connect(lambda: self.ui.chats_stackedwidget.setCurrentWidget(self.ui.promopage))
    self.ui.groupeButton.clicked.connect(lambda: self.ui.chats_stackedwidget.setCurrentWidget(self.ui.grouppage))
    self.ui.lobbybutton.clicked.connect(lambda: self.ui.chats_stackedwidget.setCurrentWidget(self.ui.lobbypage))

    # chat details page navigation

    self.ui.imageButtton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.mediapage))
    self.ui.fileButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.filespage))
    # message_body =
    self.ui.sendmessageButton.clicked.connect(self.add_promo_sent_message_to_ui)
    self.ui.uploadfileButton.clicked.connect(self.add_promo_received_message_to_ui)

    # self.ui.sendmessageButton.clicked.connect(lambda: self.copy_frame())
    # send message
    # self.ui.sendmessageButton.clicked.connect()
    # upload file in message
    # self.ui.uploadfileButton.clicked.connect()
    # upload profile pic
    # self.ui.pushButton_5.clicked.connect()
    # logout
    # self.ui.logout.clicked.connect()
    # search in chat
    # self.ui.addimageButton.clicked.connect()


def add_promo_sent_message_to_ui(self, ):
    # Create a new instance of the frame
    messagebody = self.ui.messageinput.toPlainText()

    # Copy contents of original_frame to new_frame
    self.sendermessageFrame_2 = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents_3)
    self.sendermessageFrame_2.setMinimumSize(QtCore.QSize(0, 90))
    self.sendermessageFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.sendermessageFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
    self.sendermessageFrame_2.setObjectName("sendermessageFrame_2")
    self.sendermessageFrame_2.setMinimumSize(QtCore.QSize(467, 50))
    self.sendermessageFrame_2.setMaximumSize(QtCore.QSize(16777215, 90))
    self.sendermessageFrame_2.setBaseSize(QtCore.QSize(467, 50))
    self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.sendermessageFrame_2)
    self.horizontalLayout_13.setObjectName("horizontalLayout_13")
    self.sendermessagebodyFrame_2 = QtWidgets.QFrame(self.sendermessageFrame_2)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.sendermessagebodyFrame_2.sizePolicy().hasHeightForWidth())
    self.sendermessagebodyFrame_2.setSizePolicy(sizePolicy)
    self.sendermessagebodyFrame_2.setMinimumSize(QtCore.QSize(467, 50))
    self.sendermessagebodyFrame_2.setMaximumSize(QtCore.QSize(16777215, 90))
    self.sendermessagebodyFrame_2.setBaseSize(QtCore.QSize(467, 50))
    self.sendermessagebodyFrame_2.setStyleSheet("background-color: #EBFFED;\n"
                                                "top: 18px;\n"
                                                "left: 540px;\n"
                                                "padding: 8px 12px 8px 12px;\n"
                                                "\n"
                                                "border-radius: 16px;\n"
                                                "border-bottom-right-radius: 0px;\n"
                                                "\n"
                                                "")
    self.sendermessagebodyFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.sendermessagebodyFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
    self.sendermessagebodyFrame_2.setObjectName("sendermessagebodyFrame_2")
    self.gridLayout_8 = QtWidgets.QGridLayout(self.sendermessagebodyFrame_2)
    self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
    self.gridLayout_8.setHorizontalSpacing(0)
    self.gridLayout_8.setVerticalSpacing(3)
    self.gridLayout_8.setObjectName("gridLayout_8")
    self.sendermessagetext_2 = QtWidgets.QLabel(self.sendermessagebodyFrame_2)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.sendermessagetext_2.sizePolicy().hasHeightForWidth())
    self.sendermessagetext_2.setSizePolicy(sizePolicy)
    self.sendermessagetext_2.setMinimumSize(QtCore.QSize(443, 50))
    self.sendermessagetext_2.setMaximumSize(QtCore.QSize(592, 50))
    font = QtGui.QFont()
    font.setFamily("Open Sans")
    font.setPointSize(12)
    self.sendermessagetext_2.setFont(font)
    self.sendermessagetext_2.setStyleSheet("background-color: transparent;\n"
                                           "color:#181D25;\n"
                                           "\n"
                                           "")
    self.sendermessagetext_2.setWordWrap(True)
    self.sendermessagetext_2.setObjectName("sendermessagetext_2")
    self.gridLayout_8.addWidget(self.sendermessagetext_2, 0, 0, 1, 1)
    self.sendermessagetime_2 = QtWidgets.QLabel(self.sendermessagebodyFrame_2)
    font = QtGui.QFont()
    font.setFamily("Open Sans")
    font.setPointSize(10)
    self.sendermessagetime_2.setFont(font)
    self.sendermessagetime_2.setStyleSheet("background:transparent;\n"
                                           "color:#929FB1;\n"
                                           "padding:0;")
    self.sendermessagetime_2.setObjectName("sendermessagetime_2")
    self.gridLayout_8.addWidget(self.sendermessagetime_2, 1, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
    self.horizontalLayout_13.addWidget(self.sendermessagebodyFrame_2, 0, QtCore.Qt.AlignRight)
    self.senderpic_2 = QtWidgets.QLabel(self.sendermessageFrame_2)
    self.senderpic_2.setMinimumSize(QtCore.QSize(56, 56))
    self.senderpic_2.setMaximumSize(QtCore.QSize(56, 56))
    self.senderpic_2.setText("")
    self.senderpic_2.setPixmap(QtGui.QPixmap(":/icons/icons/avatar (1).png"))
    self.senderpic_2.setObjectName("senderpic_2")
    self.horizontalLayout_13.addWidget(self.senderpic_2)
    self.ui.verticalLayout_8.addWidget(self.sendermessageFrame_2)
    self.sendermessagetext_2.setText(str(messagebody))
    self.sendermessagetime_2.setText("19:45")
    scroll_bar = self.ui.promoscrollarea.verticalScrollBar()
    scroll_bar.setValue(scroll_bar.maximum())


def append_message_to_body(self,frame,message,current_user)

def add_promo_received_message_to_ui(self):
    self.receivermessageFrame_2 = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents_3)
    self.receivermessageFrame_2.setMinimumSize(QtCore.QSize(550, 90))
    self.receivermessageFrame_2.setMaximumSize(QtCore.QSize(443, 90))
    self.receivermessageFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.receivermessageFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
    self.receivermessageFrame_2.setObjectName("receivermessageFrame_2")
    self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.receivermessageFrame_2)
    self.horizontalLayout_14.setObjectName("horizontalLayout_14")
    self.senderpic_4 = QtWidgets.QLabel(self.receivermessageFrame_2)
    self.senderpic_4.setMinimumSize(QtCore.QSize(56, 56))
    self.senderpic_4.setMaximumSize(QtCore.QSize(56, 56))
    self.senderpic_4.setText("")
    self.senderpic_4.setPixmap(QtGui.QPixmap(":/icons/icons/avatar (1).png"))
    self.senderpic_4.setObjectName("senderpic_4")
    self.horizontalLayout_14.addWidget(self.senderpic_4)
    self.receivermessagebodyFrame_2 = QtWidgets.QFrame(self.receivermessageFrame_2)
    self.receivermessagebodyFrame_2.setMinimumSize(QtCore.QSize(0, 0))
    self.receivermessagebodyFrame_2.setMaximumSize(QtCore.QSize(592, 90))
    self.receivermessagebodyFrame_2.setStyleSheet("background-color: #FFFFFF;\n"
                                                  "top: 618px;\n"
                                                  "left: 86px;\n"
                                                  "padding: 8px 12px 8px 12px;\n"
                                                  "\n"
                                                  "border-radius: 16px;\n"
                                                  "border-bottom-left-radius: 0px;\n"
                                                  "")
    self.receivermessagebodyFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.receivermessagebodyFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
    self.receivermessagebodyFrame_2.setObjectName("receivermessagebodyFrame_2")
    self.gridLayout_9 = QtWidgets.QGridLayout(self.receivermessagebodyFrame_2)
    self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
    self.gridLayout_9.setHorizontalSpacing(0)
    self.gridLayout_9.setVerticalSpacing(3)
    self.gridLayout_9.setObjectName("gridLayout_9")
    self.receivermessagetime_2 = QtWidgets.QLabel(self.receivermessagebodyFrame_2)
    self.receivermessagetime_2.setMaximumSize(QtCore.QSize(16777215, 10))
    font = QtGui.QFont()
    font.setFamily("Open Sans")
    font.setPointSize(10)
    self.receivermessagetime_2.setFont(font)
    self.receivermessagetime_2.setStyleSheet("background:transparent;\n"
                                             "color:#929FB1;\n"
                                             "padding:0;")
    self.receivermessagetime_2.setObjectName("receivermessagetime_2")
    self.gridLayout_9.addWidget(self.receivermessagetime_2, 1, 1, 1, 1)
    self.receivermessagetext_2 = QtWidgets.QLabel(self.receivermessagebodyFrame_2)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.receivermessagetext_2.sizePolicy().hasHeightForWidth())
    self.receivermessagetext_2.setSizePolicy(sizePolicy)
    self.receivermessagetext_2.setMinimumSize(QtCore.QSize(443, 50))
    self.receivermessagetext_2.setMaximumSize(QtCore.QSize(592, 90))
    font = QtGui.QFont()
    font.setFamily("Open Sans")
    font.setPointSize(12)
    self.receivermessagetext_2.setFont(font)
    self.receivermessagetext_2.setStyleSheet("background-color: transparent;\n"
                                             "color:#181D25;\n"
                                             "")
    self.receivermessagetext_2.setWordWrap(True)
    self.receivermessagetext_2.setObjectName("receivermessagetext_2")
    self.gridLayout_9.addWidget(self.receivermessagetext_2, 0, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
    self.horizontalLayout_14.addWidget(self.receivermessagebodyFrame_2)
    self.ui.verticalLayout_8.addWidget(self.receivermessageFrame_2)


def add_chat_message_sender(self):
    self.first_frame = self.ui.promoscrollarea.findChildren(QFrame)[0]

    self.clone_layout = QVBoxLayout()

    # Copy contents of the first frame to the clone layout
    for child_widget in self.first_frame.children():
        # Create a copy of the child widget
        if isinstance(child_widget, QFrame):
            for child2 in child_widget.children():
                if isinstance(child2, QFrame):  # Example widget type
                    cloned_widget = QLabel(child2.text(), self)
                    self.clone_layout.addWidget(cloned_widget)


def goToLoginPage(self):
    widget.setCurrentIndex(widget.currentIndex() - 1)
    widget.setMaximumSize(1000, 832)
    widget.adjustSize()
    widget.resize(1000, 832)











