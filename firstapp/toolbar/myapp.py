from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QToolBar,QLabel,QMainWindow,QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        label=QLabel("helblo")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar=QToolBar('My tool bar')
        self.addToolBar(toolbar)

        button_action=QAction("your button",self)
        button_action.setStatusTip("this is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)

    def onMyToolBarButtonClick(self,s):
        print("click",s)

app=QApplication([])
window=MainWindow()
window.show()
app.exec_()