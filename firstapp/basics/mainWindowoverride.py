import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5.QtCore import QSize,Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MyApp")
        button=QPushButton("press it")
        self.setFixedSize(QSize(500,600))
        self.setCentralWidget(button)

app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()
