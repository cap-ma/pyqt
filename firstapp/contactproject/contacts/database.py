from PyQt5.QtWidgets import QApplication,QMessageBox
from PyQt5.QtSql import QSqlDatabase,QSqlQuery

def createConnections(databasename):
    connection=QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databasename)

    if not connection.open():
        QMessageBox.warning(None,"RP contact",f"DATABASE ERRROR :{connection.lastError().text()}",)
        return False
    _createContacsTable()
    return True
    

    return True
def _createContacsTable():
    createTableQuery=QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS contacts(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL

        )
        """
    )
