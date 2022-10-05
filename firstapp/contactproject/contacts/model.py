from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt
class ContactsModel:
    def __init__(self):
        self.model=self._createModel()
    @staticmethod
    def _createModel():
        tableModel=QSqlTableModel()
        tableModel.setTable('contacts')
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers=("ID","NAME","Jiob","Email")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel


    def addContact(self, data):
        """Add a contact to the database."""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column + 1), field)
        self.model.submitAll()
        self.model.select()