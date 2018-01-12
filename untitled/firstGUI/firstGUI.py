import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class OurGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 GUI App')
        self.statusBar().showMessage('Status Bar Text')

        menubar = self.menuBar()

        # This is the file menubar

        file_menu = menubar.addMenu('File')
        new_action = QAction('New', self)
        file_menu.addAction(new_action)
        new_action.setStatusTip('New File')
        new_action = QAction('Open', self)
        file_menu.addAction(new_action)
        new_action.setStatusTip('Open File(s)')
        exit_action = QAction('Exit', self)
        exit_action.setStatusTip('Click to exit the application')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        #This is the edit menubar

        file_menu = menubar.addMenu('Edit')
        new_action = QAction('File', self)
        file_menu.addAction(new_action)
        new_action.setStatusTip('Edit File')

        self.resize(500,400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = OurGUI()
    gui.show()
    sys.exit(app.exec_())
