
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel,QCheckBox,QComboBox,QDateEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget=QLabel("jojo")
        widget.setPixmap(QPixmap("2.jpg"))
        widget.setScaledContents(True)
        self.setCentralWidget(widget)


app=QApplication([])
h=MainWindow()

h.show()
app.exec_()