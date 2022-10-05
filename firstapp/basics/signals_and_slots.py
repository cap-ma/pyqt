from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
from PyQt5.QtCore import Qt

import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("hi")
        button=QPushButton("press me")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_clicked)
        button.clicked.connect(self.button_toggled)

        self.setCentralWidget(button)

    def the_button_clicked(self):
        print("clicked")
    def button_toggled(self,checked):
        print("checked",checked)

app=QApplication(sys.argv)
window=MainWindow()
window.show()

app.exec_()