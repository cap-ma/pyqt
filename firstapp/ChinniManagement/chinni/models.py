from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt
class InProductsModel:
    def __init__(self):
        self.model=self._createModel()
    @staticmethod
    def _createModel():
        tableModel=QSqlTableModel()
        tableModel.setTable('inproducts')
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers=("ID","NOMI","SONI","NARX","QO'SHIMCHA","KELGANSANA")
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        return tableModel


    def addInProduct(self, data):
        """Add a contact to the database."""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            self.model.setData(self.model.index(rows, column + 1), field)
        self.model.submitAll()
        self.model.select()