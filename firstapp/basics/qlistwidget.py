from re import L
from PyQt5.QtWidgets import QMainWindow,QApplication,QListWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget=QListWidget()
        widget.addItems(["1","2","3"])
        widget.currentItemChanged.connect(self.itemchanged)
        widget.currentTextChanged.connect(self.textchanged)

        self.setCentralWidget(widget)
    def itemchanged(self,i):
        print(i)
    def textchanged(self,s):
        print(s)
app=QApplication([])
window=MainWindow()
window.show()

app.exec_()
