import sys 
from PyQt5.QtWidgets import QApplication

from .views import MainWindow
from .database import createConnections




def main():

    app=QApplication(sys.argv)
    if not createConnections('contacts.sqlite'):
        sys.exit(1)


    window=MainWindow()
    window.show()
    sys.exit(app.exec())
