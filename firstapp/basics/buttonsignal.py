from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("hello")
        self.button=QPushButton("press me")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.buttonclicked)
       

        self.setCentralWidget(self.button)

    def buttonclicked(self):
        self.button.setText("you are clciked")
        self.button.setEnabled(True)
        self.setWindowTitle("changed title")
            
    
app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()

