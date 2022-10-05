import sys 
from PyQt5.QtWidgets import QApplication

from .views import Window
from .database import createConnections




def main():

    app=QApplication(sys.argv)
    if not createConnections('inProduct.sqlite'):
        sys.exit(1)


    window=Window()
    window.show()
    sys.exit(app.exec())
