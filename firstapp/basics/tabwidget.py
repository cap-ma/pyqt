from PyQt5.QtWidgets import QApplication,QMainWindow,QTabWidget,QPushButton

from layout.layouts import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        tabs=QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        for n,color in enumerate(['red',"green","blue"]):
            tabs.addTab(Color(color),"l"+color)

        self.setCentralWidget(tabs)
app=QApplication([])
window=MainWindow()
window.show()

app.exec_()