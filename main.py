import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtCore import QObject, QEvent, Qt

from Chatapp import *
from loginPage import*
from CreateStudent import *







from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi
# from healthCare.ui import Ui_MainWindow
from pymongo.server_api import  ServerApi
from pymongo.mongo_client import MongoClient
import threading
import motor.motor_asyncio
import  Callbacks


# Import the generated class
class MongoDBWatcher(threading.Thread):
    def __init__(self, gui_handler):
        super().__init__()
        self.gui_handler = gui_handler
        self.stop_event = threading.Event()
        self.mongo =MongoClient("mongodb+srv://MOUL_BALON:luqbmQXfJfW7lwJY@cluster0b.ucohiqk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0B",server_api=ServerApi('1'))


    def run(self):
        db = self.mongo['bddd']
        collection = db['your_collection_name']

        with collection.watch(full_document='updateLookup') as stream:
            while not self.stop_event.is_set():
                try:
                    change = stream.next()
                    updated_value = change.get('fullDocument', {}).get('field_to_update')
                    if updated_value is not None:
                        self.gui_handler.update_gui(updated_value)
                except StopIteration:
                    # Handle end of stream or other errors
                    break
                except Exception as e:
                    print(f"Error in MongoDB change watcher: {e}")

    def stop(self):
        self.stop_event.set()

        
class MyMainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(self.minimumSizeHint())
        self.ui.widget_4.hide()
        
        #Chats navigation
        self.ui.promoButton.clicked.connect(lambda: self.ui.chats_stackedwidget.setCurrentWidget(self.ui.promopage))
        self.ui.groupeButton.clicked.connect(lambda: self.ui.chats_stackedwidget.setCurrentWidget(self.ui.grouppage))
        self.ui.lobbybutton.clicked.connect(lambda: self.ui.chats_stackedwidget.setCurrentWidget(self.ui.lobbypage))

        #chat details page navigation
        
        self.ui.imageButtton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.mediapage))
        self.ui.fileButton.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.filespage))
        self.ui.sendmessageButton.clicked.connect(self.add_chat_message_sender)


        #send message
        #self.ui.sendmessageButton.clicked.connect()
        #upload file in message
        #self.ui.uploadfileButton.clicked.connect()
        #upload profile pic
        #self.ui.pushButton_5.clicked.connect()
        #logout
        #self.ui.logout.clicked.connect()
        #search in caht
        #self.ui.addimageButton.clicked.connect()
    
    def copy_frame(self):
        # Create a new instance of the frame
        new_frame = QFrame()
        new_frame_layout = QVBoxLayout(new_frame)

        # Copy contents of original_frame to new_frame
        for i in range(self.original_frame_layout.count()):
            widget = self.original_frame_layout.itemAt(i).widget()
            new_widget = QLabel(widget.text())
            new_frame_layout.addWidget(new_widget)

    def add_chat_message_sender(self):
        self.first_frame = self.ui.scrollArea.findChildren(QFrame)[0]

        self.clone_layout = QVBoxLayout()

        # Copy contents of the first frame to the clone layout
        for child_widget in self.first_frame.children():
            # Create a copy of the child widget
            if isinstance(child_widget, QPushButton):  # Example widget type
                cloned_widget = QPushButton(child_widget.text(), self)
                self.clone_layout.addWidget(cloned_widget)

          


class CreateStudentpage(QMainWindow, Ui_CreateStudent):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_CreateStudent()
        self.ui.setupUi(self)
        self.resize(self.minimumSizeHint())   

class LoginPage(QMainWindow, Ui_Login):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.resize(self.minimumSizeHint())
        self.ui.signinButton.clicked.connect(self.goToMainScreen)
    def goToMainScreen(self):
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setMaximumSize(1800, 1000)    
        widget.adjustSize()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    login_window = LoginPage()
    main_app_window = MyMainWindow()
    widget.addWidget(login_window)
    widget.addWidget(main_app_window)
    
    widget.setMinimumSize(1000, 832)
    widget.setFixedSize(1000,832)
    widget.show()
   
    sys.exit(app.exec_())