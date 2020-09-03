# This Python file uses the following encoding: utf-8
import os
import sys

import PySide2
from PySide2.QtCore import QFile
from PySide2.QtGui import QImage, QKeySequence
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QShortcut

from Ui_mainwindow import Ui_mainWindow

PySide2.QtCore.Qt.Key

class mainWindow(QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        
        self.dir_path = '/home/duc/Desktop/ML_WorkSpace/ocr/train'
        with open(os.path.join(self.dir_path, 'labels.txt'), 'r') as f:
            self.anno_list = [line.replace('\n','').split('\t') for line in f]

        self.index = 0
        self.updateFrame()
        
        self.ui.nextButton.clicked.connect(self.nextFn)
        self.ui.saveButton.clicked.connect(self.saveFn)
        self.ui.backButton.clicked.connect(self.backFn)
        self.ui.delButton.clicked.connect(self.delFn)
        self.ui.gotoButton.clicked.connect(self.gotoFn)

        shortcut = QShortcut(QKeySequence('Shift+Ctrl+Z'), self.ui.nextButton)

    def updateFrame(self):
        if abs(self.index) >= len(self.anno_list):
            self.index = 0

        self.ui.frame.setPixmap(
            PySide2.QtGui.QPixmap(os.path.join(self.dir_path, 
                                self.anno_list[self.index][0]))
        )
        self.ui.labelBox.setText(self.anno_list[self.index][1])
        self.ui.idxBox.setText(str(self.index))
        # print(self.anno_list[self.index])

    def checkEdit(self):
        if self.ui.labelBox.text() != self.anno_list[self.index][1]:
            self.anno_list[self.index][1] = self.ui.labelBox.text()

    def nextFn(self):
        self.checkEdit()
        self.index += 1
        self.updateFrame()
    
    def backFn(self):
        self.checkEdit()
        self.index -= 1
        self.updateFrame()
    
    def saveFn(self):
        self.ui.saveButton.setText('Saving.........Plz wait')
        with open(os.path.join(self.dir_path, 'labels.txt'), 'w') as f:
            for line in self.anno_list:
                f.write('\t'.join(line)+'\n')
        
        self.ui.saveButton.setText('Saving successfull, click agian to save')

    def delFn(self):
        os.remove(os.path.join(self.dir_path, self.anno_list[self.index][0]))
        del(self.anno_list[self.index])
        self.updateFrame()
    
    def gotoFn(self):
        self.index = int(self.ui.idxBox.text())
        self.updateFrame()





if __name__ == "__main__":
    app = QApplication([])
    widget = mainWindow()
    widget.show()
    sys.exit(app.exec_())
