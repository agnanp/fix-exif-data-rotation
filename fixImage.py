from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import *
from PIL import Image, ExifTags

import sys
import os
import glob
import subprocess
import time


class FimImageThread(QThread):

    countChanged = pyqtSignal(int)
    totalFile = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.inDir = ""

    def run(self):
        try:
            data_path = os.path.join(self.inDir,'*.jpg')
            files = sorted(glob.glob(data_path))
            print(len(files))
            self.totalFile.emit(int(len(files)))
            count = 0
            for file in files:
                count +=1
                print(count)
                self.countChanged.emit(int(count))
                try:
                    image=Image.open(file)
                    for orientation in ExifTags.TAGS.keys():
                        if ExifTags.TAGS[orientation]=='Orientation':
                            break
                    exif=dict(image._getexif().items())

                    if exif[orientation] == 1:
                        print(file)
                        print("or1")
                        subprocess.run(["convert", file, "-orient", "top-left", file])
                    elif exif[orientation] == 2:
                        print(file)
                        print("or2")
                        subprocess.run(["convert", file, "-orient", "top-left", file])
                    elif exif[orientation] == 3:
                        print(file)
                        print("or3")
                        subprocess.run(["convert", file, "-orient", "top-left", file])
                    elif exif[orientation] == 4:
                        print(file)
                        print("or4")
                        subprocess.run(["convert", file, "-orient", "top-left", file])
                    elif exif[orientation] == 5:
                        print(file)
                        print("or5")
                        subprocess.run(["convert", file, "-orient", "top-left", file])
                    elif exif[orientation] == 6:
                        print(file)
                        print("or6")
                        subprocess.run(["convert", file, "-orient", "top-left", file]) #convert *jpg -orient top-left ./out/
                    elif exif[orientation] == 7:
                        print(file)
                        print("or7")
                        subprocess.run(["convert", file, "-orient", "top-left", file])
                    elif exif[orientation] == 8:
                        print(file)
                        print("or8")
                        subprocess.run(["convert", file, "-orient", "top-left", file])
                    image.close()
                except (AttributeError, KeyError, IndexError):
                # cases: image don't have getexif
                    pass
        except:
            pass


class Window(QDialog):
    "docstring for Window.QDialog"
    def __init__(self):
        super().__init__()
        self.title = "Fix Orientation Image"
        self.left = 500
        self.top = 200
        self.width = 600
        self.height = 100
        self.iconName = "icon/icon.png"
        self.fixImg = FimImageThread()
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.show()
        self.initLayout()
        self.CreatLayout()
        vbox = QVBoxLayout()

        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

    def _input_file_dialog(self):
        inputDir = pyqtSignal(object)
        self.inputDirectory = str(QFileDialog.getExistingDirectory())
        self.inputLineEdit.setText('{}'.format(self.inputDirectory))

    def ClickExit(self):
        sys.exit()

    def fixExifImage(self):
        self.fixImg.inDir = self.inputDirectory
        self.fixImg.totalFile.connect(self.setProgressMax)
        self.fixImg.countChanged.connect(self.setProgressVal)
        self.fixImg.start()

    def setProgressMax(self, max):
        self.progressbar.setMaximum(max)

    def setProgressVal(self, val):
        self.progressbar.setValue(val)


    def initLayout(self):
        self.button = QPushButton("Input Directory", self)
        self.button.setIcon(QtGui.QIcon("icon/folder.png"))
        self.button.setIconSize(QtCore.QSize(25,25))
        self.button.setMinimumHeight(30)
        self.button.clicked.connect(self._input_file_dialog)

        self.inputLineEdit = QLineEdit(self)
        self.inputLineEdit.setEnabled(False)
        self.inputLineEdit.setMinimumHeight(30)
        self.inputLineEdit.setObjectName("inputLineEdit")

        self.button1 = QPushButton("Fix Image", self)
        self.button1.setIcon(QtGui.QIcon("icon/data.png"))
        self.button1.setIconSize(QtCore.QSize(25,25))
        self.button1.setMinimumHeight(30)
        self.button1.clicked.connect(self.fixExifImage)

        self.progressbar = QProgressBar()
        self.progressbar.setMinimumHeight(30)

        self.button2 = QPushButton("Exit",self)
        self.button2.setIcon(QtGui.QIcon("icon/close.png"))
        self.button2.setIconSize(QtCore.QSize(25,25))
        self.button2.setMinimumHeight(30)
        self.button2.clicked.connect(self.ClickExit)


    def CreatLayout(self):
        self.groupBox = QGroupBox()
        gridLayout = QGridLayout()

        gridLayout.addWidget(self.button, 0, 0)
        gridLayout.addWidget(self.button1, 1, 0)
        gridLayout.addWidget(self.button2, 2, 0)
        gridLayout.addWidget(self.inputLineEdit, 0, 1)
        gridLayout.addWidget(self.progressbar, 1, 1)

        self.groupBox.setLayout(gridLayout)



if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
