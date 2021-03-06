from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
import sys
import json
import re
import rustUI


class CropsModel(QtCore.QAbstractListModel):
    def __init__(self, *args, crops=None, **kwargs):
        super(CropsModel, self).__init__(*args, **kwargs)
        self.crops = crops or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            text = self.crops[index.row()]
            return text

    def rowCount(self, index):
        return len(self.crops)


# Application Gui Loader
class App(QtWidgets.QFrame, rustUI.Ui_Frame):
    def __init__(self):
        QtWidgets.QFrame.__init__(self)
        self.setupUi(self)
        self.addCropButton.clicked.connect(self.addCrop)
        self.cropInput.returnPressed.connect(self.addCrop)
        self.clearButton.clicked.connect(self.clearCrop)
        self.model = CropsModel(crops=[])
        self.cropList.setModel(self.model)
        self.load()

    def addCrop(self):
        text = self.cropInput.text().upper()

        if re.search("[YGHWXyghwx]{6}", text):  # Prevents adding empty strings
            # Access the cropList via model
            self.model.crops.append(text)
            # Refresh list view
            self.model.layoutChanged.emit()
            # Clear input
            self.cropInput.setText("")
            self.save()
        else:
            errorDialog = QtWidgets.QErrorMessage()
            errorDialog.showMessage("Invalid Crop")
            errorDialog.exec()

    def clearCrop(self):
        indexes = self.cropList.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.model.crops[index.row()]
            self.model.layoutChanged.emit()
            self.cropList.clearSelection()
            self.save()

    def load(self):
        try:
            with open('data.json', 'r') as f:
                self.model.crops = json.load(f)
        except Exception:
            pass

    def save(self):
        with open('data.json', 'w') as f:
            data = json.dump(self.model.crops, f)


app = QtWidgets.QApplication(sys.argv)
window = App()
window.show()
app.exec()
