import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtCore import QObject, QEvent, Qt

from Chatapp import *
from loginPage import*
from CreateStudent import *

from mainTools import *
from mongo import *


db = getDb()

global User



from PyQt5.QtWidgets import QApplication,QMainWindow

from pymongo.server_api import  ServerApi
from pymongo.mongo_client import MongoClient
import threading
#import motor.motor_asyncio
import  Callbacks


# Import the generated class
# class MongoDBWatcher(threading.Thread):
#     def __init__(self, gui_handler):
#         super().__init__()
#         self.gui_handler = gui_handler
#         self.stop_event = threading.Event()
#         self.mongo =MongoClient("mongodb+srv://MOUL_BALON:luqbmQXfJfW7lwJY@cluster0b.ucohiqk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0B",server_api=ServerApi('1'))


#     def run(self):
#         db = self.mongo['bddd']
#         collection = db['your_collection_name']

#         with collection.watch(full_document='updateLookup') as stream:
#             while not self.stop_event.is_set():
#                 try:
#                     change = stream.next()
#                     updated_value = change.get('fullDocument', {}).get('field_to_update')
#                     if updated_value is not None:
#                         self.gui_handler.update_gui(updated_value)
#                 except StopIteration:
#                     # Handle end of stream or other errors
#                     break
#                 except Exception as e:
#                     print(f"Error in MongoDB change watcher: {e}")

#     def stop(self):
#         self.stop_event.set()


class MyMainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(self.minimumSizeHint())
        self.ui.widget_4.hide()
        
        self.ui.detailsMenuButton.clicked.connect(lambda: widget.resize(1800,1000))
        self.ui.XButton.clicked.connect(lambda: widget.resize(1368,1000))
        self.ui.logoutButton.clicked.connect(self.goToLoginPage)

        #Chats navigation
        self.ui.promoButton.clicked.connect(lambda: self.ui.chats_stackedwidget.setCurrentWidget(self.ui.promopage))
        self.ui.groupeButton.clicked.connect(lambda: self.ui.chats_stackedwidget.setCurrentWidget(self.ui.grouppage))
        self.ui.lobbybutton.clicked.connect(lambda: self.ui.chats_stackedwidget.setCurrentWidget(self.ui.lobbypage))

        #chat details page navigation
        
        self.ui.imageButtton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.mediapage))
        self.ui.fileButton.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.filespage))
        #message_body = 
        
        
        self.ui.sendmessageButton.clicked.connect(self.add_sent_message_to_ui)
        self.ui.uploadfileButton.clicked.connect(self.add_received_message_to_ui)
        self.ui.promoscrollarea.verticalScrollBar().setValue(self.ui.promoscrollarea.verticalScrollBar().maximum())
        self.ui.groupescrollarea.verticalScrollBar().setValue(self.ui.groupescrollarea.verticalScrollBar().maximum())
        self.ui.lobbyscrollarea.verticalScrollBar().setValue(self.ui.lobbyscrollarea.verticalScrollBar().maximum())
        # get the message u want to show on the screen
        # message = "hello"
        
        # self.ui.promoButton.clicked.connect(lambda: self.add_received_message_to_ui(message))
        # self.ui.groupeButton.clicked.connect(lambda: self.add_received_message_to_ui(message))
        # self.ui.lobbybutton.clicked.connect(lambda: self.add_received_message_to_ui(message))

        #self.ui.sendmessageButton.clicked.connect(lambda: self.copy_frame())
        #send message
        #self.ui.sendmessageButton.clicked.connect()
        #upload file in message
        #self.ui.uploadfileButton.clicked.connect()
        #upload profile pic
        #self.ui.pushButton_5.clicked.connect()
        #logout
        #self.ui.logout.clicked.connect()
        #search in chat
        #self.ui.addimageButton.clicked.connect()
    

    


    def add_sent_message_to_ui(self):
        # Create a new instance of the frame
        
        messagebody = self.ui.messageinput.toPlainText()
        user = widget.property("user")
        print("current property : ",user)
        if len(messagebody) != 0:
            if self.ui.chats_stackedwidget.currentIndex() == 0:
                collection = get_collection("promos",db)
                print("the useris : ",user)
                query = {"promo":user[7]}
                promo = execute_query(collection,query)[0]
                message = {"sender":user[6],"type":"text","content":messagebody}
                promo = add_message(message, promo, collection)

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
                self.gridLayout_8.addWidget(self.sendermessagetime_2, 1, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
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
                self.sendermessagetime_2.setText(user[6])

            self.ui.promoscrollarea.verticalScrollBar().setValue(self.ui.promoscrollarea.verticalScrollBar().maximum())
            
                #scroll_bar.setValue(scroll_bar.minimum())

            if self.ui.chats_stackedwidget.currentIndex() == 1:

                collection = get_collection("groups",db)
                
                query = {"group":user[7]+user[8]}
                promo = execute_query(collection,query)[0]
                message = {"sender":user[6],"type":"text","content":messagebody}
                promo = add_message(message, promo, collection)

                self.sendermessageFrame = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents)
                self.sendermessageFrame.setMinimumSize(QtCore.QSize(0, 90))
                self.sendermessageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.sendermessageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.sendermessageFrame.setObjectName("sendermessageFrame")
                self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.sendermessageFrame)
                self.horizontalLayout_10.setObjectName("horizontalLayout_10")
                self.sendermessagebodyFrame = QtWidgets.QFrame(self.sendermessageFrame)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.sendermessagebodyFrame.sizePolicy().hasHeightForWidth())
                self.sendermessagebodyFrame.setSizePolicy(sizePolicy)
                self.sendermessagebodyFrame.setMinimumSize(QtCore.QSize(467, 50))
                self.sendermessagebodyFrame.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.sendermessagebodyFrame.setBaseSize(QtCore.QSize(467, 50))
                self.sendermessagebodyFrame.setStyleSheet("background-color: #EBFFED;\n"
        "top: 18px;\n"
        "left: 540px;\n"
        "padding: 8px 12px 8px 12px;\n"
        "\n"
        "border-radius: 16px;\n"
        "border-bottom-right-radius: 0px;\n"
        "\n"
        "")
                self.sendermessagebodyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.sendermessagebodyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.sendermessagebodyFrame.setObjectName("sendermessagebodyFrame")
                self.gridLayout_4 = QtWidgets.QGridLayout(self.sendermessagebodyFrame)
                self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
                self.gridLayout_4.setHorizontalSpacing(0)
                self.gridLayout_4.setVerticalSpacing(3)
                self.gridLayout_4.setObjectName("gridLayout_4")
                self.sendermessagetext = QtWidgets.QLabel(self.sendermessagebodyFrame)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.sendermessagetext.sizePolicy().hasHeightForWidth())
                self.sendermessagetext.setSizePolicy(sizePolicy)
                self.sendermessagetext.setMinimumSize(QtCore.QSize(443, 50))
                self.sendermessagetext.setMaximumSize(QtCore.QSize(592, 16777215))
                font = QtGui.QFont()
                font.setFamily("Open Sans")
                font.setPointSize(12)
                self.sendermessagetext.setFont(font)
                self.sendermessagetext.setStyleSheet("background-color: transparent;\n"
        "color:#181D25;\n"
        "\n"
        "")
                self.sendermessagetext.setWordWrap(True)
                self.sendermessagetext.setObjectName("sendermessagetext")
                self.gridLayout_4.addWidget(self.sendermessagetext, 0, 0, 1, 1)
                self.sendermessagetime = QtWidgets.QLabel(self.sendermessagebodyFrame)
                font = QtGui.QFont()
                font.setFamily("Open Sans")
                font.setPointSize(10)
                self.sendermessagetime.setFont(font)
                self.sendermessagetime.setStyleSheet("background:transparent;\n"
        "color:#929FB1;\n"
        "padding:0;")
                self.sendermessagetime.setObjectName("sendermessagetime")
                self.gridLayout_4.addWidget(self.sendermessagetime, 1, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
                self.horizontalLayout_10.addWidget(self.sendermessagebodyFrame, 0, QtCore.Qt.AlignRight)
                self.senderpic = QtWidgets.QLabel(self.sendermessageFrame)
                self.senderpic.setMinimumSize(QtCore.QSize(56, 56))
                self.senderpic.setMaximumSize(QtCore.QSize(56, 56))
                self.senderpic.setText("")
                self.senderpic.setPixmap(QtGui.QPixmap(":/icons/icons/avatar (1).png"))
                self.senderpic.setObjectName("senderpic")
                self.horizontalLayout_10.addWidget(self.senderpic)
                self.ui.verticalLayout_9.addWidget(self.sendermessageFrame)
                self.sendermessagetext.setText(str(messagebody))
                self.sendermessagetime.setText(user[6])

            self.ui.verticalLayout_4.update()
            self.ui.groupescrollarea.verticalScrollBar().setValue(self.ui.groupescrollarea.verticalScrollBar().maximum())
            self.ui.verticalLayout_4.update()

            if self.ui.chats_stackedwidget.currentIndex() == 2:

                collection = get_collection("all",db)
                
                query = {"all":"all"}
                lobby = execute_query(collection,query)[0]
                message = {"sender":user[6],"type":"text","content":messagebody}
                lobby = add_message(message, lobby, collection)

                self.sendermessageFrame_3 = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents_4)
                self.sendermessageFrame_3.setMinimumSize(QtCore.QSize(0, 90))
                self.sendermessageFrame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.sendermessageFrame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.sendermessageFrame_3.setObjectName("sendermessageFrame_3")
                self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.sendermessageFrame_3)
                self.horizontalLayout_15.setObjectName("horizontalLayout_15")
                self.sendermessagebodyFrame_3 = QtWidgets.QFrame(self.sendermessageFrame_3)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.sendermessagebodyFrame_3.sizePolicy().hasHeightForWidth())
                self.sendermessagebodyFrame_3.setSizePolicy(sizePolicy)
                self.sendermessagebodyFrame_3.setMinimumSize(QtCore.QSize(467, 50))
                self.sendermessagebodyFrame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.sendermessagebodyFrame_3.setBaseSize(QtCore.QSize(467, 50))
                self.sendermessagebodyFrame_3.setStyleSheet("background-color: #EBFFED;\n"
        "top: 18px;\n"
        "left: 540px;\n"
        "padding: 8px 12px 8px 12px;\n"
        "\n"
        "border-radius: 16px;\n"
        "border-bottom-right-radius: 0px;\n"
        "\n"
        "")
                self.sendermessagebodyFrame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.sendermessagebodyFrame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.sendermessagebodyFrame_3.setObjectName("sendermessagebodyFrame_3")
                self.gridLayout_10 = QtWidgets.QGridLayout(self.sendermessagebodyFrame_3)
                self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
                self.gridLayout_10.setHorizontalSpacing(0)
                self.gridLayout_10.setVerticalSpacing(3)
                self.gridLayout_10.setObjectName("gridLayout_10")
                self.sendermessagetext_3 = QtWidgets.QLabel(self.sendermessagebodyFrame_3)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.sendermessagetext_3.sizePolicy().hasHeightForWidth())
                self.sendermessagetext_3.setSizePolicy(sizePolicy)
                self.sendermessagetext_3.setMinimumSize(QtCore.QSize(443, 50))
                self.sendermessagetext_3.setMaximumSize(QtCore.QSize(592, 16777215))
                font = QtGui.QFont()
                font.setFamily("Open Sans")
                font.setPointSize(12)
                self.sendermessagetext_3.setFont(font)
                self.sendermessagetext_3.setStyleSheet("background-color: transparent;\n"
        "color:#181D25;\n"
        "\n"
        "")
                self.sendermessagetext_3.setWordWrap(True)
                self.sendermessagetext_3.setObjectName("sendermessagetext_3")
                self.gridLayout_10.addWidget(self.sendermessagetext_3, 0, 0, 1, 1)
                self.sendermessagetime_3 = QtWidgets.QLabel(self.sendermessagebodyFrame_3)
                font = QtGui.QFont()
                font.setFamily("Open Sans")
                font.setPointSize(10)
                self.sendermessagetime_3.setFont(font)
                self.sendermessagetime_3.setStyleSheet("background:transparent;\n"
        "color:#929FB1;\n"
        "padding:0;")
                self.sendermessagetime_3.setObjectName("sendermessagetime_3")
                self.gridLayout_10.addWidget(self.sendermessagetime_3, 1, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
                self.horizontalLayout_15.addWidget(self.sendermessagebodyFrame_3, 0, QtCore.Qt.AlignRight)
                self.senderpic_5 = QtWidgets.QLabel(self.sendermessageFrame_3)
                self.senderpic_5.setMinimumSize(QtCore.QSize(56, 56))
                self.senderpic_5.setMaximumSize(QtCore.QSize(56, 56))
                self.senderpic_5.setText("")
                self.senderpic_5.setPixmap(QtGui.QPixmap(":/icons/icons/avatar (1).png"))
                self.senderpic_5.setObjectName("senderpic_5")
                self.horizontalLayout_15.addWidget(self.senderpic_5)
                self.ui.verticalLayout_11.addWidget(self.sendermessageFrame_3)
                self.sendermessagetext_3.setText(str(messagebody))
                self.sendermessagetime_3.setText(user[6])

            self.ui.verticalLayout_4.update()
            self.ui.groupescrollarea.verticalScrollBar().setValue(self.ui.groupescrollarea.verticalScrollBar().maximum())
            self.ui.verticalLayout_4.update()   

    def add_received_message_to_ui(self):
        user = widget.property("user")
        if self.ui.chats_stackedwidget.currentIndex() == 0:
            
            
            chats = get_chats("promo","",user[7])

            for message in chats["messages"]:

                
                
                messagecontent = message["content"]
                sender = message["sender"]

                if sender == user[6] :
            
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
                    self.gridLayout_8.addWidget(self.sendermessagetime_2, 1, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
                    self.horizontalLayout_13.addWidget(self.sendermessagebodyFrame_2, 0, QtCore.Qt.AlignRight)
                    self.senderpic_2 = QtWidgets.QLabel(self.sendermessageFrame_2)
                    self.senderpic_2.setMinimumSize(QtCore.QSize(56, 56))
                    self.senderpic_2.setMaximumSize(QtCore.QSize(56, 56))
                    self.senderpic_2.setText("")
                    self.senderpic_2.setPixmap(QtGui.QPixmap(":/icons/icons/avatar (1).png"))
                    self.senderpic_2.setObjectName("senderpic_2")
                    self.horizontalLayout_13.addWidget(self.senderpic_2)
                    self.ui.verticalLayout_8.addWidget(self.sendermessageFrame_2)
                    self.sendermessagetext_2.setText(str(messagecontent))
                    self.sendermessagetime_2.setText(sender)
                else:
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
                    self.gridLayout_9.addWidget(self.receivermessagetext_2, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                    self.horizontalLayout_14.addWidget(self.receivermessagebodyFrame_2)
                    self.ui.verticalLayout_8.addWidget(self.receivermessageFrame_2)
                    self.receivermessagetext_2.setText(str(messagecontent))
                    self.receivermessagetime_2.setText(sender)


        if self.ui.chats_stackedwidget.currentIndex() == 1:

            chats = get_chats("group",user[7]+user[8],"")
            

            for message in chats["messages"]:

                
                
                messagecontent = message["content"]
                sender = message["sender"]

                if sender == user[6] :
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
                    self.gridLayout_8.addWidget(self.sendermessagetime_2, 1, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
                    self.horizontalLayout_13.addWidget(self.sendermessagebodyFrame_2, 0, QtCore.Qt.AlignRight)
                    self.senderpic_2 = QtWidgets.QLabel(self.sendermessageFrame_2)
                    self.senderpic_2.setMinimumSize(QtCore.QSize(56, 56))
                    self.senderpic_2.setMaximumSize(QtCore.QSize(56, 56))
                    self.senderpic_2.setText("")
                    self.senderpic_2.setPixmap(QtGui.QPixmap(":/icons/icons/avatar (1).png"))
                    self.senderpic_2.setObjectName("senderpic_2")
                    self.horizontalLayout_13.addWidget(self.senderpic_2)
                    self.ui.verticalLayout_8.addWidget(self.sendermessageFrame_2)
                    self.sendermessagetext_2.setText(str(messagecontent))
                    self.sendermessagetime_2.setText(sender)
                else:
                    self.receivermessageFrame = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents)
                    self.receivermessageFrame.setMinimumSize(QtCore.QSize(550, 90))
                    self.receivermessageFrame.setMaximumSize(QtCore.QSize(443, 90))
                    self.receivermessageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                    self.receivermessageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
                    self.receivermessageFrame.setObjectName("receivermessageFrame")
                    self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.receivermessageFrame)
                    self.horizontalLayout_12.setObjectName("horizontalLayout_12")
                    self.senderpic_3 = QtWidgets.QLabel(self.receivermessageFrame)
                    self.senderpic_3.setMinimumSize(QtCore.QSize(56, 56))
                    self.senderpic_3.setMaximumSize(QtCore.QSize(56, 56))
                    self.senderpic_3.setText("")
                    self.senderpic_3.setPixmap(QtGui.QPixmap(":/icons/icons/avatar (1).png"))
                    self.senderpic_3.setObjectName("senderpic_3")
                    self.horizontalLayout_12.addWidget(self.senderpic_3)
                    self.receivermessagebodyFrame = QtWidgets.QFrame(self.receivermessageFrame)
                    self.receivermessagebodyFrame.setMinimumSize(QtCore.QSize(0, 0))
                    self.receivermessagebodyFrame.setMaximumSize(QtCore.QSize(592, 90))
                    self.receivermessagebodyFrame.setStyleSheet("background-color: #FFFFFF;\n"
            "top: 618px;\n"
            "left: 86px;\n"
            "padding: 8px 12px 8px 12px;\n"
            "\n"
            "border-radius: 16px;\n"
            "border-bottom-left-radius: 0px;\n"
            "")
                    self.receivermessagebodyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                    self.receivermessagebodyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
                    self.receivermessagebodyFrame.setObjectName("receivermessagebodyFrame")
                    self.gridLayout_6 = QtWidgets.QGridLayout(self.receivermessagebodyFrame)
                    self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
                    self.gridLayout_6.setHorizontalSpacing(0)
                    self.gridLayout_6.setVerticalSpacing(3)
                    self.gridLayout_6.setObjectName("gridLayout_6")
                    self.receivermessagetext = QtWidgets.QLabel(self.receivermessagebodyFrame)
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(self.receivermessagetext.sizePolicy().hasHeightForWidth())
                    self.receivermessagetext.setSizePolicy(sizePolicy)
                    self.receivermessagetext.setMinimumSize(QtCore.QSize(443, 40))
                    self.receivermessagetext.setMaximumSize(QtCore.QSize(592, 90))
                    font = QtGui.QFont()
                    font.setFamily("Open Sans")
                    font.setPointSize(12)
                    self.receivermessagetext.setFont(font)
                    self.receivermessagetext.setStyleSheet("background-color: transparent;\n"
            "color:#181D25;\n"
            "")
                    self.receivermessagetext.setWordWrap(True)
                    self.receivermessagetext.setObjectName("receivermessagetext")
                    self.gridLayout_6.addWidget(self.receivermessagetext, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                    self.receivermessagetime = QtWidgets.QLabel(self.receivermessagebodyFrame)
                    self.receivermessagetime.setMaximumSize(QtCore.QSize(16777215, 10))
                    font = QtGui.QFont()
                    font.setFamily("Open Sans")
                    font.setPointSize(10)
                    self.receivermessagetime.setFont(font)
                    self.receivermessagetime.setStyleSheet("background:transparent;\n"
            "color:#929FB1;\n"
            "padding:0;")
                    self.receivermessagetime.setObjectName("receivermessagetime")
                    self.gridLayout_6.addWidget(self.receivermessagetime, 1, 1, 1, 1)
                    self.horizontalLayout_12.addWidget(self.receivermessagebodyFrame)
                    self.ui.verticalLayout_9.addWidget(self.receivermessageFrame)
                    self.receivermessagetext.setText(messagecontent)
                    self.receivermessagetime.setText(sender)

        if self.ui.chats_stackedwidget.currentIndex() == 2:

            chats = get_chats("all","","")
            

            for message in chats["messages"]:

                
                
                messagecontent = message["content"]
                sender = message["sender"]

                if sender == user[6] :
                    self.sendermessageFrame_3 = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents_4)
                    self.sendermessageFrame_3.setMinimumSize(QtCore.QSize(0, 90))
                    self.sendermessageFrame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                    self.sendermessageFrame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                    self.sendermessageFrame_3.setObjectName("sendermessageFrame_3")
                    self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.sendermessageFrame_3)
                    self.horizontalLayout_15.setObjectName("horizontalLayout_15")
                    self.sendermessagebodyFrame_3 = QtWidgets.QFrame(self.sendermessageFrame_3)
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(self.sendermessagebodyFrame_3.sizePolicy().hasHeightForWidth())
                    self.sendermessagebodyFrame_3.setSizePolicy(sizePolicy)
                    self.sendermessagebodyFrame_3.setMinimumSize(QtCore.QSize(467, 50))
                    self.sendermessagebodyFrame_3.setMaximumSize(QtCore.QSize(16777215, 90))
                    self.sendermessagebodyFrame_3.setBaseSize(QtCore.QSize(467, 50))
                    self.sendermessagebodyFrame_3.setStyleSheet("background-color: #EBFFED;\n"
            "top: 18px;\n"
            "left: 540px;\n"
            "padding: 8px 12px 8px 12px;\n"
            "\n"
            "border-radius: 16px;\n"
            "border-bottom-right-radius: 0px;\n"
            "\n"
            "")
                    self.sendermessagebodyFrame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                    self.sendermessagebodyFrame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                    self.sendermessagebodyFrame_3.setObjectName("sendermessagebodyFrame_3")
                    self.gridLayout_10 = QtWidgets.QGridLayout(self.sendermessagebodyFrame_3)
                    self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
                    self.gridLayout_10.setHorizontalSpacing(0)
                    self.gridLayout_10.setVerticalSpacing(3)
                    self.gridLayout_10.setObjectName("gridLayout_10")
                    self.sendermessagetext_3 = QtWidgets.QLabel(self.sendermessagebodyFrame_3)
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(self.sendermessagetext_3.sizePolicy().hasHeightForWidth())
                    self.sendermessagetext_3.setSizePolicy(sizePolicy)
                    self.sendermessagetext_3.setMinimumSize(QtCore.QSize(443, 50))
                    self.sendermessagetext_3.setMaximumSize(QtCore.QSize(592, 90))
                    font = QtGui.QFont()
                    font.setFamily("Open Sans")
                    font.setPointSize(12)
                    self.sendermessagetext_3.setFont(font)
                    self.sendermessagetext_3.setStyleSheet("background-color: transparent;\n"
            "color:#181D25;\n"
            "\n"
            "")
                    self.sendermessagetext_3.setWordWrap(True)
                    self.sendermessagetext_3.setObjectName("sendermessagetext_3")
                    self.gridLayout_10.addWidget(self.sendermessagetext_3, 0, 0, 1, 1)
                    self.sendermessagetime_3 = QtWidgets.QLabel(self.sendermessagebodyFrame_3)
                    font = QtGui.QFont()
                    font.setFamily("Open Sans")
                    font.setPointSize(10)
                    self.sendermessagetime_3.setFont(font)
                    self.sendermessagetime_3.setStyleSheet("background:transparent;\n"
            "color:#929FB1;\n"
            "padding:0;")
                    self.sendermessagetime_3.setObjectName("sendermessagetime_3")
                    self.gridLayout_10.addWidget(self.sendermessagetime_3, 1, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
                    self.horizontalLayout_15.addWidget(self.sendermessagebodyFrame_3, 0, QtCore.Qt.AlignRight)
                    self.senderpic_5 = QtWidgets.QLabel(self.sendermessageFrame_3)
                    self.senderpic_5.setMinimumSize(QtCore.QSize(56, 56))
                    self.senderpic_5.setMaximumSize(QtCore.QSize(56, 56))
                    self.senderpic_5.setText("")
                    self.senderpic_5.setPixmap(QtGui.QPixmap(":/icons/icons/avatar (1).png"))
                    self.senderpic_5.setObjectName("senderpic_5")
                    self.horizontalLayout_15.addWidget(self.senderpic_5)
                    self.ui.verticalLayout_11.addWidget(self.sendermessageFrame_3)
                    self.sendermessagetext_3.setText(str(messagecontent))
                    self.sendermessagetime_3.setText(user[6])
                else:

                    self.receivermessageFrame_3 = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents_4)
                    self.receivermessageFrame_3.setMinimumSize(QtCore.QSize(550, 90))
                    self.receivermessageFrame_3.setMaximumSize(QtCore.QSize(443, 90))
                    self.receivermessageFrame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                    self.receivermessageFrame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                    self.receivermessageFrame_3.setObjectName("receivermessageFrame_3")
                    self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.receivermessageFrame_3)
                    self.horizontalLayout_16.setObjectName("horizontalLayout_16")
                    self.senderpic_6 = QtWidgets.QLabel(self.receivermessageFrame_3)
                    self.senderpic_6.setMinimumSize(QtCore.QSize(56, 56))
                    self.senderpic_6.setMaximumSize(QtCore.QSize(56, 56))
                    self.senderpic_6.setText("")
                    self.senderpic_6.setPixmap(QtGui.QPixmap(":/icons/icons/avatar (1).png"))
                    self.senderpic_6.setObjectName("senderpic_6")
                    self.horizontalLayout_16.addWidget(self.senderpic_6)
                    self.receivermessagebodyFrame_3 = QtWidgets.QFrame(self.receivermessageFrame_3)
                    self.receivermessagebodyFrame_3.setMinimumSize(QtCore.QSize(0, 0))
                    self.receivermessagebodyFrame_3.setMaximumSize(QtCore.QSize(592, 90))
                    self.receivermessagebodyFrame_3.setStyleSheet("background-color: #FFFFFF;\n"
            "top: 618px;\n"
            "left: 86px;\n"
            "padding: 8px 12px 8px 12px;\n"
            "\n"
            "border-radius: 16px;\n"
            "border-bottom-left-radius: 0px;\n"
            "")
                    self.receivermessagebodyFrame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                    self.receivermessagebodyFrame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                    self.receivermessagebodyFrame_3.setObjectName("receivermessagebodyFrame_3")
                    self.gridLayout_11 = QtWidgets.QGridLayout(self.receivermessagebodyFrame_3)
                    self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
                    self.gridLayout_11.setHorizontalSpacing(0)
                    self.gridLayout_11.setVerticalSpacing(3)
                    self.gridLayout_11.setObjectName("gridLayout_11")
                    self.receivermessagetext_3 = QtWidgets.QLabel(self.receivermessagebodyFrame_3)
                    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                    sizePolicy.setHorizontalStretch(0)
                    sizePolicy.setVerticalStretch(0)
                    sizePolicy.setHeightForWidth(self.receivermessagetext_3.sizePolicy().hasHeightForWidth())
                    self.receivermessagetext_3.setSizePolicy(sizePolicy)
                    self.receivermessagetext_3.setMinimumSize(QtCore.QSize(443, 40))
                    self.receivermessagetext_3.setMaximumSize(QtCore.QSize(592, 100))
                    font = QtGui.QFont()
                    font.setFamily("Open Sans")
                    font.setPointSize(12)
                    self.receivermessagetext_3.setFont(font)
                    self.receivermessagetext_3.setStyleSheet("background-color: transparent;\n"
            "color:#181D25;\n"
            "")
                    self.receivermessagetext_3.setWordWrap(True)
                    self.receivermessagetext_3.setObjectName("receivermessagetext_3")
                    self.gridLayout_11.addWidget(self.receivermessagetext_3, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
                    self.receivermessagetime_3 = QtWidgets.QLabel(self.receivermessagebodyFrame_3)
                    self.receivermessagetime_3.setMaximumSize(QtCore.QSize(16777215, 10))
                    font = QtGui.QFont()
                    font.setFamily("Open Sans")
                    font.setPointSize(10)
                    self.receivermessagetime_3.setFont(font)
                    self.receivermessagetime_3.setStyleSheet("background:transparent;\n"
            "color:#929FB1;\n"
            "padding:0;")
                    self.receivermessagetime_3.setObjectName("receivermessagetime_3")
                    self.gridLayout_11.addWidget(self.receivermessagetime_3, 1, 1, 1, 1)
                    self.horizontalLayout_16.addWidget(self.receivermessagebodyFrame_3)
                    self.ui.verticalLayout_11.addWidget(self.receivermessageFrame_3)
                    self.receivermessagetext_3.setText(messagecontent)
                    self.receivermessagetime_3.setText(sender)    



    def create_message_widget(self,current_user,message):
        if (current_user==1):
            sendermessageFrame_2 = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents_3)
            sendermessageFrame_2.setMinimumSize(QtCore.QSize(0, 90))
            sendermessageFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            sendermessageFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            sendermessageFrame_2.setObjectName("sendermessageFrame_2")
            sendermessageFrame_2.setMinimumSize(QtCore.QSize(467, 50))
            sendermessageFrame_2.setMaximumSize(QtCore.QSize(16777215, 90))
            sendermessageFrame_2.setBaseSize(QtCore.QSize(467, 50))
            horizontalLayout_13 = QtWidgets.QHBoxLayout(sendermessageFrame_2)
            horizontalLayout_13.setObjectName("horizontalLayout_13")
            sendermessagebodyFrame_2 = QtWidgets.QFrame(sendermessageFrame_2)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(sendermessagebodyFrame_2.sizePolicy().hasHeightForWidth())
            sendermessagebodyFrame_2.setSizePolicy(sizePolicy)
            sendermessagebodyFrame_2.setMinimumSize(QtCore.QSize(467, 50))
            sendermessagebodyFrame_2.setMaximumSize(QtCore.QSize(16777215, 90))
            sendermessagebodyFrame_2.setBaseSize(QtCore.QSize(467, 50))
            sendermessagebodyFrame_2.setStyleSheet("background-color: #EBFFED;\n"
            "top: 18px;\n"
            "left: 540px;\n"
            "padding: 8px 12px 8px 12px;\n"
            "\n"
            "border-radius: 16px;\n"
            "border-bottom-right-radius: 0px;\n"
            "\n"
            "")
            sendermessagebodyFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            sendermessagebodyFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            sendermessagebodyFrame_2.setObjectName("sendermessagebodyFrame_2")
            gridLayout_8 = QtWidgets.QGridLayout(sendermessagebodyFrame_2)
            gridLayout_8.setContentsMargins(0, 0, 0, 0)
            gridLayout_8.setHorizontalSpacing(0)
            gridLayout_8.setVerticalSpacing(3)
            gridLayout_8.setObjectName("gridLayout_8")
            sendermessagetext_2 = QtWidgets.QLabel(sendermessagebodyFrame_2)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(sendermessagetext_2.sizePolicy().hasHeightForWidth())
            sendermessagetext_2.setSizePolicy(sizePolicy)
            sendermessagetext_2.setMinimumSize(QtCore.QSize(443, 50))
            sendermessagetext_2.setMaximumSize(QtCore.QSize(592, 50))
            font = QtGui.QFont()
            font.setFamily("Open Sans")
            font.setPointSize(12)
            sendermessagetext_2.setFont(font)
            sendermessagetext_2.setStyleSheet("background-color: transparent;\n"
            "color:#181D25;\n"
            "\n"
            "")
            sendermessagetext_2.setWordWrap(True)
            sendermessagetext_2.setObjectName("sendermessagetext_2")
            gridLayout_8.addWidget(sendermessagetext_2, 0, 0, 1, 1)
            sendermessagetime_2 = QtWidgets.QLabel(sendermessagebodyFrame_2)
            font = QtGui.QFont()
            font.setFamily("Open Sans")
            font.setPointSize(10)
            sendermessagetime_2.setFont(font)
            sendermessagetime_2.setStyleSheet("background:transparent;\n"
            "color:#929FB1;\n"
            "padding:0;")
            sendermessagetime_2.setObjectName("sendermessagetime_2")
            gridLayout_8.addWidget(sendermessagetime_2, 1, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
            horizontalLayout_13.addWidget(sendermessagebodyFrame_2, 0, QtCore.Qt.AlignRight)
            senderpic_2 = QtWidgets.QLabel(sendermessageFrame_2)
            senderpic_2.setMinimumSize(QtCore.QSize(56, 56))
            senderpic_2.setMaximumSize(QtCore.QSize(56, 56))
            senderpic_2.setText("")
            senderpic_2.setPixmap(QtGui.QPixmap(":/icons/icons/avatar (1).png"))
            senderpic_2.setObjectName("senderpic_2")
            sendermessagetext_2.setText(str(message))
            sendermessagetime_2.setText("19:45")
            self.horizontalLayout_13.addWidget(self.senderpic_2)
                
            return sendermessageFrame_2
        else:
            receivermessageFrame_2 = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents_3)
            receivermessageFrame_2.setMinimumSize(QtCore.QSize(550, 90))
            receivermessageFrame_2.setMaximumSize(QtCore.QSize(443, 90))
            receivermessageFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            receivermessageFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            receivermessageFrame_2.setObjectName("receivermessageFrame_2")
            horizontalLayout_14 = QtWidgets.QHBoxLayout(receivermessageFrame_2)
            horizontalLayout_14.setObjectName("horizontalLayout_14")
            senderpic_4 = QtWidgets.QLabel(receivermessageFrame_2)
            senderpic_4.setMinimumSize(QtCore.QSize(56, 56))
            senderpic_4.setMaximumSize(QtCore.QSize(56, 56))
            senderpic_4.setText("")
            senderpic_4.setPixmap(QtGui.QPixmap(":/icons/icons/avatar (1).png"))
            senderpic_4.setObjectName("senderpic_4")
            horizontalLayout_14.addWidget(senderpic_4)
            receivermessagebodyFrame_2 = QtWidgets.QFrame(receivermessageFrame_2)
            receivermessagebodyFrame_2.setMinimumSize(QtCore.QSize(0, 0))
            receivermessagebodyFrame_2.setMaximumSize(QtCore.QSize(592, 90))
            receivermessagebodyFrame_2.setStyleSheet("background-color: #FFFFFF;\n"
            "top: 618px;\n"
            "left: 86px;\n"
            "padding: 8px 12px 8px 12px;\n"
            "\n"
            "border-radius: 16px;\n"
            "border-bottom-left-radius: 0px;\n"
            "")
            receivermessagebodyFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            receivermessagebodyFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
            receivermessagebodyFrame_2.setObjectName("receivermessagebodyFrame_2")
            gridLayout_9 = QtWidgets.QGridLayout(receivermessagebodyFrame_2)
            gridLayout_9.setContentsMargins(0, 0, 0, 0)
            gridLayout_9.setHorizontalSpacing(0)
            gridLayout_9.setVerticalSpacing(3)
            gridLayout_9.setObjectName("gridLayout_9")
            receivermessagetime_2 = QtWidgets.QLabel(receivermessagebodyFrame_2)
            receivermessagetime_2.setMaximumSize(QtCore.QSize(16777215, 10))
            font = QtGui.QFont()
            font.setFamily("Open Sans")
            font.setPointSize(10)
            receivermessagetime_2.setFont(font)
            receivermessagetime_2.setStyleSheet("background:transparent;\n"
            "color:#929FB1;\n"
            "padding:0;")
            receivermessagetime_2.setObjectName("receivermessagetime_2")
            gridLayout_9.addWidget(receivermessagetime_2, 1, 1, 1, 1)
            receivermessagetext_2 = QtWidgets.QLabel(receivermessagebodyFrame_2)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(receivermessagetext_2.sizePolicy().hasHeightForWidth())
            receivermessagetext_2.setSizePolicy(sizePolicy)
            receivermessagetext_2.setMinimumSize(QtCore.QSize(443, 50))
            receivermessagetext_2.setMaximumSize(QtCore.QSize(592, 90))
            font = QtGui.QFont()
            font.setFamily("Open Sans")
            font.setPointSize(12)
            receivermessagetext_2.setFont(font)
            receivermessagetext_2.setStyleSheet("background-color: transparent;\n"
            "color:#181D25;\n"
            "")
            receivermessagetext_2.setWordWrap(True)
            receivermessagetext_2.setObjectName("receivermessagetext_2")
            gridLayout_9.addWidget(receivermessagetext_2, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
            receivermessagetext_2.setText(str(message))
            receivermessagetime_2.setText("19:45")
            self.horizontalLayout_14.addWidget(self.receivermessagebodyFrame_2)

            return receivermessageFrame_2  

    def append_message_to_ui(self,layout,widget):
        #promo layout = self.ui.verticalLayout_8.addWidget(self.sendermessageFrame_2)
        #group layout = self.ui.verticalLayout_9.addWidget(self.receivermessageFrame)
        #lobby layout = self.horizontalLayout_13.addWidget(self.senderpic_2)
        layout.addWidget(widget)
        

           
    

    def goToLoginPage(self):
        widget.setCurrentIndex(widget.currentIndex()-1)
        widget.setMaximumSize(1000, 832)    
        widget.adjustSize()
        widget.resize(1000, 832)          

          


class CreateStudentpage(QMainWindow, Ui_CreateStudent):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_CreateStudent()
        self.ui.setupUi(self)
        self.resize(self.minimumSizeHint())
        self.ui.signup_button.clicked.connect(self.create_student)

    def create_student(self):
        firstname = self.ui.firstname.text()
        lastname = self.ui.lastname.text()
        email = self.ui.email.text()
        username = self.ui.username.text()
        password = self.ui.password.text()
        password = encode_password(password)
        promo = self.ui.promo.text()
        groupe = self.ui.groupe.text()
        query = f'insert into users values (null,"{firstname}","{lastname}","{password}","student","{email}","{username}","{promo}","{groupe}",null) '  
        sql.execute_query(query,(),connection)
        collection = get_collection("promos",db)
        query = {"promo":promo}
        update_query = {'$push':{'members':username}}
        collection.update_one(query,update_query)

        collection = get_collection("groups",db)
        query = {"group":groupe}
        update_query = {'$push':{'memebers':username}}
        collection.update_one(query,update_query)

        collection = get_collection("all",db)
        query = {"all":"all"}
        update_query = {'$push':{'member':username}}
        collection.update_one(query,update_query)

class LoginPage(QMainWindow, Ui_Login):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.resize(self.minimumSizeHint())
        self.ui.signinButton.clicked.connect(self.goToMainScreen)
        
    def goToMainScreen(self):
        email= self.ui.email.text()

        password = self.ui.password.text()
        
        user,auth, error = authenticate(email,password)
    
        if auth:
            if user[4]=="student":
                widget.setCurrentIndex(widget.currentIndex()+1)
                
                widget.setMaximumSize(1800, 1000)    
                widget.adjustSize()
                widget.resize(1368,1000)
                widget.setProperty("user", user)
                print(user)
            else:
                widget.setCurrentIndex(widget.currentIndex()+2)
                widget.adjustSize()
                widget.resize(680,935)

        else:
            print("user not found")

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    login_window = LoginPage()
    main_app_window = MyMainWindow()
    student_creation = CreateStudentpage()

    widget.addWidget(login_window)
    widget.addWidget(main_app_window)
    widget.addWidget(student_creation)
    widget.setProperty("user", ())
    
    

    widget.setMinimumSize(1000, 832)
    widget.setFixedSize(1000,832)
    widget.show()

    #get list of messages from the data base and isnert them in the ui

    message = "hello"
    #received messages    
    # main_app_window.ui.promoButton.clicked.connect(lambda: main_app_window.add_received_message_to_ui(message))
    # main_app_window.ui.groupeButton.clicked.connect(lambda: main_app_window.add_received_message_to_ui(message))
    # main_app_window.ui.lobbybutton.clicked.connect(lambda: main_app_window.add_received_message_to_ui(message))

    #messages sent by user
   
    sys.exit(app.exec_())