import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Coffee(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect('coffee.sqlite')
        self.run()

    def run(self):
        query = "SELECT * FROM coffee_beans"
        result = self.connection.cursor().execute(query).fetchall()
        for i, data in enumerate(result):
            self.tableWidget.setRowCount(i + 1)
            for j, elem in enumerate(data):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec_())
