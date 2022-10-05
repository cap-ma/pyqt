from tkinter import Widget
from PyQt5.QtWidgets import QApplication , QMainWindow ,QLineEdit

from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget=QLineEdit()
        widget.setMaxLength(5)
        widget.setPlaceholderText("Enter text")

       

        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection)

        self.setCentralWidget(widget)
    
    def selection(self):
        print("selection")
        print(self.centralWidget().selectedText())
    def text_changed(self,s):
        print("TEXT CHANGED  "  +s)
    def text_edited(self,s):
        print("TExt editedd  "+s)
    def return_pressed(self):
        print("return")
        self.centralWidget().setText("hjogn")


    






app=QApplication([])
window=MainWindow()

window.show()

app.exec_()
