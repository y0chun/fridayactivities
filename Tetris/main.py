from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
import sys, random

class Tetris(MainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()  
