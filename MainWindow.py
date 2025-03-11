from PyQt6.QtCore import pyqtSlot, QFile, QIODevice, QTextStream, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QMenuBar, QFileDialog, QMessageBox, QProgressBar, QStatusBar

from CentralWidget import CentralWidget


class MainWindow(QMainWindow):
    new_line = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        central_widget = CentralWidget(self)
        self.new_line.connect(central_widget.append_values)

        self.setCentralWidget(central_widget)

        self.setWindowTitle("Abschlussprüfung 2024/25")
        self.setBaseSize(800, 600)
        self.resize(800, 600)

        status_bar = QStatusBar()

        self.__progress_bar = QProgressBar()

        status_bar.addWidget(self.__progress_bar)

        self.setStatusBar(status_bar)

        # Requirement 2.1

    @pyqtSlot()
    def open_file(self):
        # Requirement 2.2
        pass

        # Requirement 2.3

        # Requirement 2.4

        # Requirement 2.5

            # length = len(lines) - 1
            #
            # self.__progress_bar.setRange(0, length)
            #
            # for i in range(length):
            #     self.new_line.emit(lines[i])
            #
            #     self.__progress_bar.setValue(i + 1)
