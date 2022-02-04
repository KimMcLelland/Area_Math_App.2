import sys


from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QSpinBox

#from random import choice



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


        walls = QLabel("Walls: ")
        font = walls.font()
        font.setBold(True)
        walls.setFont(font)
        wallsLength = QLabel("0")
        multiply = QLabel(" X ")
        wallsHeight = QLabel("0")
        multiply2 = QLabel(" X ")
        wallsDepth = QLabel("0")

        floors1 = QLabel("Floors: ")
        floors1.setFont(font)
        floors2 = QLabel("0")

        doors1 = QLabel("Doors: ")
        doors1.setFont(font)
        doors2 = QLabel("0")

        windows1 = QLabel("Windows: ")
        windows1.setFont(font)
        windows2 = QLabel("0")
        openBracket = QLabel(" (")
        windowHeight = QLabel("0")
        multiply3 = QLabel(" X ")
        windowLength = QLabel("0")
        closeBracket =QLabel(" )")

        button = QPushButton("Calculate")
        result = QLabel("")

        prompt1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        prompt2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        prompt3.setAlignment(Qt.AlignmentFlag.AlignLeft)
        prompt4.setAlignment(Qt.AlignmentFlag.AlignLeft)
        prompt5.setAlignment(Qt.AlignmentFlag.AlignLeft)
        prompt6.setAlignment(Qt.AlignmentFlag.AlignLeft)
        prompt7.setAlignment(Qt.AlignmentFlag.AlignLeft)
        multiplylabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        
        #the app layout
        layout = QVBoxLayout()

        question1 = QHBoxLayout()
        question1.addWidget(prompt1)
        question1.addWidget(input1)
        
        

        question2 = QHBoxLayout()
        question2.addWidget(prompt2)
        question2.addWidget(input2)

        question3 = QHBoxLayout()
        question3.addWidget(prompt3)
        question3.addWidget(input3)

        question4 = QHBoxLayout()
        question4.addWidget(prompt4)
        question4.addWidget(input4)

        question5 = QHBoxLayout()
        question5.addWidget(prompt5)
        question5.addWidget(input5)

        question6 = QHBoxLayout()
        question6.addWidget(prompt6)
        question6.addWidget(input6)

        question7 = QHBoxLayout()
        question7.addWidget(prompt7)
        windowsAnswer = QHBoxLayout()
        question7.addLayout(windowsAnswer)
        windowsAnswer.addWidget(input7)
        windowsAnswer.addWidget(multiplylabel)
        windowsAnswer.addWidget(input8)

        Summary = QHBoxLayout()
        Summary.addWidget(walls)
        Summary.addWidget(wallsLength)
        Summary.addWidget(multiply)
        Summary.addWidget(wallsDepth)
        Summary.addWidget(multiply2)
        Summary.addWidget(wallsHeight)

        Summary.addWidget(doors1)
        Summary.addWidget(doors2)

        Summary.addWidget(floors1)
        Summary.addWidget(floors2)

        Summary.addWidget(windows1)
        Summary.addWidget(windows2)
        Summary.addWidget(openBracket)
        Summary.addWidget(windowHeight)
        Summary.addWidget(multiply3)
        Summary.addWidget(windowLength)
        Summary.addWidget(closeBracket)
        
        #nesting layouts
        layout.addLayout(question1)
        layout.addLayout(question2)
        layout.addLayout(question3)
        layout.addLayout(question4)
        layout.addLayout(question5)
        layout.addLayout(question6)
        layout.addLayout(question7)
        layout.addLayout(Summary)

        layout.addWidget(button)
        layout.addWidget(result)

        container = QWidget()
        container.setLayout(layout)

        self.setWindowTitle("Area Math")

        self.setMinimumSize(QSize(400, 500))

        self.setCentralWidget(container)

        #the function of the app
        
        input1.textChanged.connect(wallsHeight.setText)
        input2.textChanged.connect(wallsLength.setText)
        input3.textChanged.connect(wallsDepth.setText)
        input4.textChanged.connect(floors2.setText)
        input5.textChanged.connect(doors2.setText)
        input6.textChanged.connect(windows2.setText)
        input7.textChanged.connect(windowHeight.setText)
        input8.textChanged.connect(windowLength.setText)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()