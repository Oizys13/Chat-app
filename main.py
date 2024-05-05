import re
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QPushButton, QWidget, QLabel
import PyQt5.QtWidgets as QtWidgets
from PyQt5.QtCore import QObject, QEvent, Qt
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui

# from healthCare.ui import Ui_MainWindow
from pymongo.server_api import  ServerApi
from pymongo.mongo_client import MongoClient
import threading
import motor.motor_asyncio
from Callbacks import *
from PyQt5.QtWidgets import QApplication,QMainWindow


from datetime import datetime
import resources_rc

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'





# Import the generated class
class MongoDBWatcher(threading.Thread):

    def __init__(self, gui_handler):
        super().__init__()
        self.gui_handler = gui_handler
        self.current_channel = self.gui_handler.current_channel
        self.stop_event = threading.Event()
        print('i am here')
        # self.mongo =MongoClient("mongodb+srv://MOUL_BALON:luqbmQXfJfW7lwJY@cluster0b.ucohiqk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0B",server_api=ServerApi('1'))

    def run(self):
        print('is this message visible?')
        db = mongo['bddd']
        collection = db['chatrooms']

        with collection.watch(full_document='updateLookup') as stream:
            while not self.stop_event.is_set():
                try:
                    change = stream.next()
                    # print('change : ',change)
                    updated_value = change
                    if updated_value is not None:
                        self.gui_handler.update_gui(updated_value)
                except StopIteration:
                    # Handle end of stream or other errors
                    break
                except Exception as e:
                    print(f"Error in MongoDB change watcher: {e}")

            return

    def stop(self):
        self.stop_event.set()



class MyMainWindow(QMainWindow):


    def __init__(self):
        super(MyMainWindow,self).__init__()
        # loadUi("healthCare.ui",self)
        self.current_page = None
        self.current_user = None
        self.login_error = None
        self.create_error = None

        self.watcher = None
        # self.watcher = MongoDBWatcher(self)

        self.current_channel = None


        self.login_page = loadUi('ChatloginPage.ui')
        self.login_page.signinButton.clicked.connect(self.handleSignIn)


        self.create_student_page = loadUi('CreateStudent.ui')
        self.create_student_page.signup_button.clicked.connect(self.handleCreateStudent)



        self.chat_app = loadUi('Chatapp.ui')
        # Channel Navigation
        self.chat_app.promoButton.clicked.connect(lambda: self.handleChannelChange('promo'))
        self.chat_app.groupeButton.clicked.connect(lambda:self.handleChannelChange('groupe') )
        self.chat_app.lobbybutton.clicked.connect(lambda:self.handleChannelChange('lobby') )

        self.chat_app.sendmessageButton.clicked.connect(lambda: self.handleSendMessage())



        self.show_login_page()

    def handleChannelChange(self,newChannel):
        if(self.current_channel==newChannel):
            return


        # kill current watcher
        # self.watcher.daemon=True
        self.watcher.stop()
        temp = self.watcher
        del(temp)
        print('active threads  : ',threading.active_count())
        # if self.watcher.is_alive():
        #     print("Thread terminated forcibly.")
        # else:
        #     print("Thread terminated successfully.")
        # create new one with the updated channel
        self.watcher = MongoDBWatcher(gui_handler=self)
        self.watcher.start()
        self.current_channel = newChannel
        if (newChannel == 'promo'):
            self.chat_app.chats_stackedwidget.setCurrentWidget(self.chat_app.promopage)

        elif (newChannel == 'groupe'):
            self.chat_app.chats_stackedwidget.setCurrentWidget(self.chat_app.grouppage)

        elif (newChannel == 'lobby'):
            self.chat_app.chats_stackedwidget.setCurrentWidget(self.chat_app.lobbypage)

    def handleSendMessage(self):
        if(self.current_user==None):
            self.show_login_page()

        # we get the input from the field
        message = self.chat_app.messageinput.toPlainText()
        if(message == None or len(message)<1):
            return
        message_data = {
            'userID':self.current_user[0],
            'type':'text',
            'content':message,
            'timestamp':datetime.utcnow()
        }
        current_promo = '*' if self.current_channel == 'lobby' else self.current_user[7]
        current_groupe = '*' if self.current_channel != 'groupe' else self.current_user[8]
        # sendMessage(self.current_user,current_promo,current_groupe,message_data)

        res = threading.Thread(target=sendMessage, args=[self.current_user,current_promo,current_groupe,message_data ])
        print(res.start())
        self.chat_app.messageinput.setText('')

    def handleCreateStudent(self):
        print('wassap')
        # if(self.current_user == None): return
        first_name = self.create_student_page.firstname.text()
        last_name = self.create_student_page.lastname.text()
        username = self.create_student_page.username.text()

        email = self.create_student_page.email.text()
        password = self.create_student_page.password.text()

        # promo = self.create_student_page.promo.text()
        # groupe = self.create_student_page.groupe.text()

        res = threading.Thread(target=CreateStudent,args=[None,{
            'first_name':first_name,
            'last_name':last_name,
            'username':username,
            'email':email,
            'password':password,
            'promo':'2cs',
            'groupe':'2'
        }])
        print(res.start())
        pass

    def handleSignIn(self):
        email=self.login_page.email.text()
        password = self.login_page.password.text()
        if(re.fullmatch(email_regex,email) and len(password)>4):
            # print("Input Validated")
            print('Checking with DB')
            response = SignIn(email,password)
            print(response)
            if(response['data']!=None):
                self.current_user = response['data']
                if(self.current_user[4]=='student'):
                    self.current_channel = 'promo'
                    self.show_chat_app()
                elif(self.current_user[4]=='admin'):
                    self.show_create_student_page()

        self.login_page.password.setText('')
        pass

    def set_page(self, page):
        if self.current_page:
            self.current_page.hide()
        self.current_page = page
        self.setCentralWidget(page)
        page.show()

    def show_login_page(self):

        self.set_page(self.login_page)

    def show_create_student_page(self):
        if(self.current_user ==None):
            self.show_login_page()
        if(self.current_user[4]!='admin'):
            self.show_chat_app()
        self.set_page(self.create_student_page)



    def show_chat_app(self):
        if(self.current_user ==None):
            self.show_login_page()
        if(self.current_user[4]!='student'):
            self.show_create_student_page()
        print('current user :',self.current_user)


        # now we know we are a student trying to get messages
        #  first we get the messages list
        # then we itterate over them messages and append to the grid conditionally
        #
        if(self.current_channel==None) : self.current_channel = 'promo'
        self.watcher = MongoDBWatcher(self)
        self.watcher.start()
        self.set_page(self.chat_app)

    def create_message_widget(self, current_user, message,channel):
        current_scroll_area = None
        if (channel=='lobby') : current_scroll_area = self.chat_app.scrollAreaWidgetContents_2
        if (current_user[0]==message['userID']):
            sendermessageFrame_2 = QtWidgets.QFrame(current_scroll_area)
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
            gridLayout_8.addWidget(sendermessagetime_2, 1, 0, 1, 1, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
            horizontalLayout_13.addWidget(sendermessagebodyFrame_2, 0, QtCore.Qt.AlignRight)
            senderpic_2 = QtWidgets.QLabel(sendermessageFrame_2)
            senderpic_2.setMinimumSize(QtCore.QSize(56, 56))
            senderpic_2.setMaximumSize(QtCore.QSize(56, 56))
            senderpic_2.setText("")
            senderpic_2.setPixmap(QtGui.QPixmap(":/icons/icons/avatar (1).png"))
            senderpic_2.setObjectName("senderpic_2")
            sendermessagetext_2.setText(str(message['content']))
            sendermessagetime_2.setText("19:45")
            horizontalLayout_13.addWidget(senderpic_2)

            return sendermessageFrame_2
        else:
            receivermessageFrame_2 = QtWidgets.QFrame()
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
            gridLayout_9.addWidget(receivermessagetext_2, 0, 0, 1, 1, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            receivermessagetext_2.setText(str(message['content']))
            receivermessagetime_2.setText("19:45")
            horizontalLayout_14.addWidget(receivermessagebodyFrame_2)

            return receivermessageFrame_2

    def append_message_to_ui(self,layout,widget):
        #promo layout = self.ui.verticalLayout_4.addWidget(self.sendermessageFrame_2)
        #group layout = self.ui.verticalLayout_10.addWidget(self.receivermessageFrame)
        #lobby layout = self.verticalLayout_12.addWidget(self.senderpic_2)
        layout.addWidget(widget)


    def update_gui(self,updated_value):
        print('updating gui')
        # print('updated_value: ',updated_value['fullDocument'])
        updated_messages_promo = updated_value['fullDocument']['promo']
        updated_messages_groupe = updated_value['fullDocument']['groupe']
        updated_messages_messages = updated_value['fullDocument']['messages']
        # print(updated_messages_promo)
        # print(updated_messages_groupe)
        print('new messages :',updated_messages_messages)
        if not (updated_messages_promo in ['*',self.current_user[7]] and updated_messages_groupe in ['*',self.current_user[8]]) : return


        print("Current User is concerned with the message")
        #  now we know the current user is concerned with the change
        if (updated_messages_promo == '*'):
            # we are in lobby
            while self.chat_app.gridLayout_11.count():
                widget = self.chat_app.gridLayout_11.takeAt(0).widget()
                if widget:
                    widget.deleteLater()

            for message in updated_messages_messages :
                new_widget = self.create_message_widget(self.current_user,message,'lobby')
                # print(new_widget)

                self.append_message_to_ui(self.chat_app.gridLayout_11,new_widget)

            print(self.chat_app.gridLayout_11)
            self.repaint()

            pass

        elif (updated_messages_groupe == '*'):
            # we are in promo
            pass
        else :
            # we are in groupe
            pass

        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())