from ctypes import alignment
from PySide6 import QtCore, QtWidgets, QtGui
import sys
import random 
from PySide6.QtCore import Slot
from fetchingspotify import fetchingthealbum 

class InfinitePlayer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.WelcomeToInfinite = ["hello there! welcome to the infinite player !"]
        self.button = QtWidgets.QPushButton("Just a placeholder button ! ")
        self.button2 = QtWidgets.QComboBox()
        self.text = QtWidgets.QLabel("Infinity Player", alignment=QtCore.Qt.AlignCenter)
    

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)
        self.button.clicked.connect(fetchingthealbum)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = InfinitePlayer()
    widget.setStyleSheet("""
        background-color: #262626;
        color: #FFFFFF;
        font-family: Titillium;
        font-size: 18px;
        """)
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
