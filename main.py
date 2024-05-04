import re
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi
# from healthCare.ui import Ui_MainWindow
from pymongo.server_api import  ServerApi
from pymongo.mongo_client import MongoClient
import threading
import motor.motor_asyncio
from Callbacks import *


email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'





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
        super(MyMainWindow,self).__init__()
        # loadUi("healthCare.ui",self)
        self.current_page = None
        self.current_user = None
        self.login_error = None
        self.create_error = None


        self.login_page = loadUi('ChatloginPage.ui')
        self.login_page.signinButton.clicked.connect(self.handleSignIn)


        self.create_student_page = loadUi('CreateStudent.ui')
        self.chat_app = loadUi('Chatapp.ui')



        self.show_login_page()


    def handleSignIn(self):
        email=self.login_page.email.text()
        password = self.login_page.password.text()
        if(re.fullmatch(email_regex,email) and len(password)>4):
            print("Input Validated")
            print('Checking with DB')
            response = SignIn(email,password)
            if(response['data']!=None):
                self.current_user = response['data']

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
        self.set_page(self.create_student_page)

    def show_chat_app(self):
        self.set_page(self.chat_app)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())