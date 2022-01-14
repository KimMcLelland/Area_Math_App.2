import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget

from random import choice



# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #defining the different elements of the app
        prompt1 = QLabel("Building height:")
        input1 = QLineEdit()
        prompt2 = QLabel("Building width:")
        input2 = QLineEdit()
        prompt3 = QLabel("Building depth:")
        input3 = QLineEdit()
        prompt4 = QLabel("number of floors:")
        input4 = QLineEdit()
        prompt5 = QLabel("number of doors:")
        input5 = QLineEdit()
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
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setWindowTitle("Area Math")

        self.setMinimumSize(QSize(400, 300))

        self.setCentralWidget(container)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()