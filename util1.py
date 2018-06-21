import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QGraphicsView
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QRectF, pyqtSignal, QT_VERSION_STR
from PyQt5.QtGui import QImage, QPixmap, QPainterPath
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QFileDialog

import mockup1

class MockupApp(QtWidgets.QMainWindow,mockup1.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Bloomfield Robotics")
        self.setWindowIcon(QtGui.QIcon('br.png'))
        self.scene = QGraphicsScene()
        self.scene.addPixmap(QPixmap("/Users/lilysmith/trichomes.jpeg"))
        self.graphicsView.setScene(self.scene)
        self.view = QGraphicsView(self.scene)
        self.view.resize(self.scene.width(), self.scene.height())

        self.show()

    def main():
        app = QtWidgets.QApplication(sys.argv)
        GUI = MockupApp()
        sys.exit(app.exec_())

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MockupApp()
    sys.exit(app.exec_())
