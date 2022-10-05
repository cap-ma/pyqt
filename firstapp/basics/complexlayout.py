from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QStackedLayout,QVBoxLayout,QPushButton,QLabel,QHBoxLayout
from layout.layouts import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        pageLayout=QVBoxLayout()
        buttonLayout=QHBoxLayout()
        self.stackedLayout=QStackedLayout()

        pageLayout.addLayout(buttonLayout)
        pageLayout.addLayout(self.stackedLayout)

        btn=QPushButton("red")
        btn.pressed.connect(self.activate)
        buttonLayout.addWidget(btn)
        self.stackedLayout.addWidget(Color('red'))
        

        btn1=QPushButton("green")
        btn1.pressed.connect(self.activategreen)
        buttonLayout.addWidget(btn1)
        self.stackedLayout.addWidget(Color("green"))
        

        btn2=QPushButton("black")
        btn2.pressed.connect(self.activateblack)
        buttonLayout.addWidget(btn2)
        
        self.stackedLayout.addWidget(Color("black"))

        widget=QWidget()

        widget.setLayout(pageLayout)
        self.setCentralWidget(widget)

    def activate(self):
        
        self.stackedLayout.setCurrentIndex(0)
    def activategreen(self):
       
       self.stackedLayout.setCurrentIndex(1)
    def activateblack(self):
        
        self.stackedLayout.setCurrentIndex(2)

app=QApplication([])
window=MainWindow()
window.show()
app.exec_()




