from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
import sys
import rustUI


class CropsModel(QtCore.QAbstractListModel):
    def __init__(self, *args, crops=None, **kwargs):
        super(CropsModel, self).__init__(*args, **kwargs)
        self.crops = crops or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            crop = self.crops[index.row()]
            return crop

    def rowCount(self, index):
        return len(self.crops)


# Application Gui Loader
class App(QtWidgets.QFrame, rustUI.Ui_Frame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.setupUi(self)
        self.addCropButton.clicked.connect(self.addCrop)
        self.model = CropsModel(crops=["AGFHGAGH", "ASGFKJHDS"])
        self.cropList.setModel(self.model)

    def addCrop(self):
        print("testing")


app = QtWidgets.QApplication(sys.argv)
window = App()
window.show()
app.exec()
