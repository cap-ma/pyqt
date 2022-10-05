from PyQt5.QtWidgets import QApplication,QMessageBox
from PyQt5.QtSql import QSqlDatabase,QSqlQuery

def createConnections(databasename):
    connection=QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databasename)

    if not connection.open():
        QMessageBox.warning(None,"RP contact",f"DATABASE ERRROR :{connection.lastError().text()}",)
        return False
    _createInStoreTable()
    return True
    


def _createInStoreTable():
    createTableQuery=QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS inproducts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            nom VARCHAR(40) NOT NULL,
            soni VARCHAR(50) NOT NULL, 
            narx VARCHAR(40) NOT NULL,
            qoshimcha VARCHAR(200),
            kelgannarsa DATETIME default current_timestamp
        )
        """
    )
