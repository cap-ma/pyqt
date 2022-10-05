
import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog,QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button=QPushButton("press")
        button.clicked.connect(self.butto)

        self.setCentralWidget(button)

    def butto(self):
        dlg=QDialog()
        dlg.setWindowTitle("hell0")
        dlg.exec_()
app=QApplication([])
window=MainWindow()
window.show()
app.exec_()


    
