import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap, QIcon

import br

class BrApp(QtWidgets.QMainWindow,br.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Image Display Window")
        self.setWindowIcon(QtGui.QIcon('br.png'))

        self.show()

    def main():
        app = QtWidgets.QApplication(sys.argv)
        GUI = BrApp()
        sys.exit(app.exec_())

if  __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BrApp()
    sys.exit(app.exec_())
