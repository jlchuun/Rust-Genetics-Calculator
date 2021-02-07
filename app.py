from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys


def main():
    app = QApplication(sys.argv)
    wind = QMainWindow()
    wind.setGeometry(200, 200, 300, 300)
    wind.setWindowTitle("Rust Genetics Calculator")
    wind.show()
    sys.exit(app.exec_())

main()