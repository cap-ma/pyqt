from PyQt5.QtWidgets import QApplication , QMainWindow,QCheckBox

from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget=QCheckBox("tryfjnhc")
        widget.setCheckState(Qt.Unchecked)
        widget.stateChanged.connect(self.show_state)
        self.setCentralWidget(widget)
        
    def show_state(self,s):
        print(s==Qt.Checked)
        print(s)


app=QApplication([])
window=MainWindow()
window.show()
app.exec_()



