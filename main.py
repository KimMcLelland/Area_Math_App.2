import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QSpinBox

from random import choice



# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #defining the different elements of the app
        prompt1 = QLabel("Building height:")
        input1 = QSpinBox()
        prompt2 = QLabel("Building width:")
        input2 = QSpinBox()
        prompt3 = QLabel("Building depth:")
        input3 = QSpinBox()
        prompt4 = QLabel("number of floors:")
        input4 = QSpinBox()
        prompt5 = QLabel("number of doors:")
        input5 = QSpinBox()
        prompt6 = QLabel("number of windows:")
        input6 = QSpinBox()
        prompt7 = QLabel("size of windows:")
        input7 = QSpinBox()
        multiplylabel =  QLabel("X")
        input8 = QSpinBox()
        self.button = QPushButton("Calculate")
        
        #the app layout
        layout = QVBoxLayout()
        layout.addWidget(prompt1)
        layout.addWidget(input1)
        layout.addWidget(prompt2)
        layout.addWidget(input2)
        layout.addWidget(prompt3)
        layout.addWidget(input3)
        layout.addWidget(prompt4)
        layout.addWidget(input4)
        layout.addWidget(prompt5)
        layout.addWidget(input5)
        layout.addWidget(prompt6)
        layout.addWidget(input6)
        layout.addWidget(prompt7)
        layout.addWidget(input7)
        layout.addWidget(multiplylabel)
        layout.addWidget(input8)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setWindowTitle("Area Math")

        self.setMinimumSize(QSize(400, 500))

        self.setCentralWidget(container)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()