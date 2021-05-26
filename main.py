# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import random

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.num = random.randint(0, 20)
        self.ui.btn_1.clicked.connect(self.check)


    def check(self):
        user = int(self.ui.tb1.text())

        while True:
            if user > self.num:
                self.ui.tb2.setText('برو پایین')
                break

            elif user < self.num:
                self.ui.tb2.setText('برو بالا')
                break

            else:
                self.ui.tb2.setText('آفرین درست حدس زدی!')
                break



if __name__ == "__main__":
    app = QApplication([])
    widget = Main()
    sys.exit(app.exec_())
