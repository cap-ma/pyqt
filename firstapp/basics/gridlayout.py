from layout.layouts import Color
from PyQt5.QtWidgets import QApplication, QGridLayout,QLabel,QMainWindow,QWidget

class MainWIndow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout=QGridLayout()

        layout.addWidget(Color("red"),0,0)
        layout.addWidget(Color('blue'),2,1)
        layout.addWidget(Color("yellow"),3,3)

        widget=QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app=QApplication([])
window=MainWIndow()
window.show()
app.exec_()

