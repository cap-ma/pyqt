
from PyQt5.QtWidgets import QApplication,QPushButton,QMainWindow
from random import choice
import sys
mylist=["wsegdf0","sdg","sdg","stwwrb"]
print(choice(mylist)) 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ibrohim")
        self.button=QPushButton("press it")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.clickedbutton)
        self.setCentralWidget(self.button)
    def clickedbutton(self,a):
        print("clicked",a)
        new_window_tittle=choice(mylist)
        print("new window title id {}",new_window_tittle)
        self.setWindowTitle(new_window_tittle)

app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()
