import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtCore import QObject, QEvent, Qt

from Chatapp import *
from loginPage import*
from CreateStudent import *





class MyMainWindow(QMainWindow, Ui_MainWindow):
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