# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rust.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(615, 494)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.layoutWidget = QtWidgets.QWidget(Frame)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 50, 271, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cropInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.cropInput.setObjectName("cropInput")
        self.horizontalLayout.addWidget(self.cropInput)
        self.addCropButton = QtWidgets.QPushButton(self.layoutWidget)
        self.addCropButton.setObjectName("addCropButton")
        self.horizontalLayout.addWidget(self.addCropButton)
        self.layoutWidget1 = QtWidgets.QWidget(Frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 160, 191, 291))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cropList = QtWidgets.QListView(self.layoutWidget1)
        self.cropList.setObjectName("cropList")
        self.verticalLayout.addWidget(self.cropList)
        self.clearButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.clearButton.setObjectName("clearButton")
        self.verticalLayout.addWidget(self.clearButton, 0, QtCore.Qt.AlignRight)
        self.resultCropList = QtWidgets.QListView(Frame)
        self.resultCropList.setGeometry(QtCore.QRect(370, 50, 191, 221))
        self.resultCropList.setObjectName("resultCropList")
        self.resultCrop = QtWidgets.QListView(Frame)
        self.resultCrop.setGeometry(QtCore.QRect(370, 290, 191, 31))
        self.resultCrop.setObjectName("resultCrop")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Rust Genetics Calculator"))
        self.addCropButton.setText(_translate("Frame", "Add Crop"))
        self.clearButton.setText(_translate("Frame", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
