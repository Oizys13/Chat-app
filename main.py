import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi
from healthCare_ui import Ui_MainWindow  # Import the generated class

class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow,self).__init__()
        loadUi("healthCare.ui",self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())