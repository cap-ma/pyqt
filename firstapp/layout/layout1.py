from re import L
from PyQt5.QtWidgets import QApplication,QMainWindow,QHBoxLayout,QWidget,QVBoxLayout,QLabel
from PyQt5.QtCore import Qt

from layouts import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout1=QHBoxLayout()
        layout2=QVBoxLayout()
        layout3=QVBoxLayout()

        layout1.setContentsMargins(0,0,0,0)
        #layout1.setSpacing(15)
        layout2.addWidget(Color('red'))
        layout2.addWidget(Color("green"))
        layout2.addWidget(Color("blue"))
        layout1.addLayout(layout2)
        layout1.addWidget(Color('green'))
        layout3.addWidget(Color('black'))
        layout3.addWidget(Color('purple'))
        layout1.addLayout(layout3)

        widget=QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


app=QApplication([])
window=MainWindow()
window.show()

app.exec_()
