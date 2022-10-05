from re import L
from PyQt5.QtWidgets import QMainWindow,QApplication,QComboBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget=QComboBox()
        widget.addItems(["1","2","3"])
        widget.currentIndexChanged.connect(self.indexchanged)
        widget.currentTextChanged.connect(self.textchanged)

        self.setCentralWidget(widget)
    def indexchanged(self,i):
        print(i)
    def textchanged(self,s):
        print(s)
app=QApplication([])
window=MainWindow()
window.show()

app.exec_()
