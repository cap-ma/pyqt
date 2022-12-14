"""from PyQt5.QtCore import Qt,QSize
from PyQt5.QtWidgets import QApplication,QToolBar,QLabel,QMainWindow,QAction

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My App")
    label = QLabel("Hello!")
    label.setAlignment(Qt.AlignCenter)
    self.setCentralWidget(label)
    toolbar = QToolBar("My main toolbar")
    toolbar.setIconSize(QSize(16, 16))
    self.addToolBar(toolbar)
    button_action = QAction(QIcon("bug.png"), "Your button", self)
    button_action.setStatusTip("This is your button")
    button_action.triggered.connect(self.onMyToolBarButtonClick)
    button_action.setCheckable(True)
    toolbar.addAction(button_action)
    self.setStatusBar(QStatusBar(self))
  def onMyToolBarButtonClick(self, s):
  print("click", s)
"""