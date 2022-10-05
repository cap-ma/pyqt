from PyQt5.QtWidgets import QApplication,QMainWindow,QSpinBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget=QSpinBox()
        widget.setMinimum(1)
        widget.setMaximum(10)
        widget.setSingleStep(3)
        widget.valueChanged.connect(self.value_changed_int)
        widget.valueChanged[str].connect(self.value_changed)

        self.setCentralWidget(widget)
    def value_changed_int(self,i):
        print("int ",i)
    def value_changed(self,s):
        print(s)
app=QApplication([])
window=MainWindow()
window.show()
app.exec_()

