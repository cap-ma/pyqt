from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize,Qt
from .models import InProductsModel

import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inproduct=InProductsModel()

        # set the title of main window
        self.setWindowTitle('Sidebar layout - www.luochang.ink')

        # set the size of window
        self.Width = 1400
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)
        self.btn=QPushButton('main menu',self)
        self.btn.setFixedSize(QSize(200,50))


        # add all widgets
        self.btn_1 = QPushButton('In Products', self)
        self.btn_1.setFixedSize(QSize(200,50))
        self.btn_2 = QPushButton('Out Products', self)
        self.btn_2.setFixedSize(QSize(200,50))
        self.btn_3 = QPushButton('InStore ', self)
        self.btn_3.setFixedSize(QSize(200,50))
        self.btn_4 = QPushButton('Calculate Gain', self)
        self.btn_4.setFixedSize(QSize(200,50))

        self.btn_1.clicked.connect(self.button1)
        self.btn_2.clicked.connect(self.button2)
        self.btn_3.clicked.connect(self.button3)
        self.btn_4.clicked.connect(self.button4)

        # add tabs
        self.tab=self.ui()
        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()
        self.tab4 = self.ui4()
        
        self.initUI()


    def initUI(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn)
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addWidget(self.btn_4)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")
        self.inproducts_right_layout=QHBoxLayout()
        self.right_widget.addTab(self.tab, '')
        self.right_widget.addTab(self.tab1,'')
        
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.addTab(self.tab4, '')

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none;}''')

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # ----------------- 
    # buttons
    def button(self):
        self.right_widget.setCurrentIndex(0)

    def button1(self):
        

        self.right_widget.setCurrentIndex(1)

    def button2(self):
        self.right_widget.setCurrentIndex(2)

    def button3(self):
        self.right_widget.setCurrentIndex(3)

    def button4(self):
        self.right_widget.setCurrentIndex(4)

    # ----------------- 
    # pages
    def ui(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 1'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main
    def ui1(self):
        main_layout=QWidget()

        layout=QHBoxLayout()
        layoutForButtons=QVBoxLayout()

        addButton=QPushButton("add")
        addButton.setFixedSize(QSize(50,100))
        addButton.clicked.connect(self.openDialog)
        deleteButton=QPushButton('delete')
        deleteButton.setFixedSize(QSize(50,100))
        layoutForButtons.addWidget(addButton)

        layoutForButtons.addWidget(deleteButton)
        layoutForButtons.addStretch()

        self.table=QTableView()
        self.table.setModel(self.inproduct.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        layout.addWidget(self.table)
        layout.addLayout(layoutForButtons)
        
        main_layout.setLayout(layout)

        
        return main_layout

    def openDialog(self):
        dialog=AddDialog(self)
        if dialog.exec()==QDialog.Accepted:
            self.inproduct.addInProduct(dialog.data)
            self.table.resizeColumnsToContents()


    def ui2(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 3'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui3(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 4'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui4(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 5'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main
class AddDialog(QDialog):
      
    def __init__(self,parent=None):
        """Initializer."""
        super().__init__(parent=parent)
        self.setWindowTitle("Add Contact")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        """Setup the Add Contact dialog's GUI."""
        # Create line edits for data fields
        self.nameField = QLineEdit()
        self.nameField.setObjectName("nom")
        self.numberField = QLineEdit()
        self.numberField.setObjectName("soni")
        self.costField = QLineEdit()
        self.costField.setObjectName("narx")
        self.extraField=QLineEdit()
        self.extraField.setObjectName("qoshimcha")
        self.dateField=QDateEdit()
        self.dateField.setObjectName("kelgannarsa")

        # Lay out the data fields
        layout = QFormLayout()
        layout.addRow("Nomi:", self.nameField)
        layout.addRow("Soni:", self.numberField)
        layout.addRow("Narx:", self.costField)
        layout.addRow("Qoshimcha",self.extraField)
        layout.addRow("Kelgan Sana",self.dateField)
        
        self.layout.addLayout(layout)
        # Add standard buttons to the dialog and connect them
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)

    def accept(self):
        """Accept the data provided through the dialog."""
        self.data = []
        for field in (self.nameField, self.numberField, self.costField, self.extraField, self.dateField):
            if not field.text():
               
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"You must provide a contact's {field.objectName()}",
                )
                self.data = None  # Reset .data
                return

            self.data.append(field.text())

        if not self.data:
            return

        super().accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())