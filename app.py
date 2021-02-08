from PyQt5 import QtWidgets, uic
from rustUI import Ui_Frame
import sys


app = QtWidgets.QApplication(sys.argv)

window = uic.loadUi("rust.ui")
window.show()
app.exec()