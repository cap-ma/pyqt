from PyQt5.QtWidgets import QStackedLayout,QApplication,QWidget,QMainWindow

from layout.layouts import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout=QStackedLayout()
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("black"))
        layout.setCurrentIndex(1)

        widget=QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app=QApplication([])
window=MainWindow()
window.show()
app.exec_()
