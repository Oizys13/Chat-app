import sys
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
        super(MyMainWindow,self).__init__()
        loadUi("healthCare.ui",self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())