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

        prompt1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        prompt2.setAlignment(Qt.AlignmentFlag.AlignLeft)
        prompt3.setAlignment(Qt.AlignmentFlag.AlignLeft)
        prompt4.setAlignment(Qt.AlignmentFlag.AlignLeft)
        prompt5.setAlignment(Qt.AlignmentFlag.AlignLeft)
        prompt6.setAlignment(Qt.AlignmentFlag.AlignLeft)
        prompt7.setAlignment(Qt.AlignmentFlag.AlignLeft)
        multiplylabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        calculate = QPushButton("Calculate")
        calculate.setCheckable(True)

        
        wallText = QLabel("The amount of blocks you need for the walls are: ")
        wallResult = QLabel("")
        floorText = QLabel("The amount of blocks you need for the floors are: ")
        floorResult = QLabel("")
        roofText = QLabel("The amount of blocks you'll likely need for the roof are: ")
        roofResult = QLabel("")
        windowText = QLabel("The amount of panes for windows is: ")
        windowResult = QLabel("")

        
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

        result = QVBoxLayout()

        wallSummary = QHBoxLayout()
        result.addLayout(wallSummary)
        wallSummary.addWidget(wallText)
        wallSummary.addWidget(wallResult)

        floorSummary = QHBoxLayout()
        result.addLayout(floorSummary)
        floorSummary.addWidget(floorText)
        floorSummary.addWidget(floorResult)

        roofSummary = QHBoxLayout()
        result.addLayout(roofSummary)
        roofSummary.addWidget(roofText)
        roofSummary.addWidget(roofResult)

        windowSummary = QHBoxLayout()
        result.addLayout(windowSummary)
        windowSummary.addWidget(windowText)
        windowSummary.addWidget(windowResult)
        
        #nesting layouts
        layout.addLayout(question1)
        layout.addLayout(question2)
        layout.addLayout(question3)
        layout.addLayout(question4)
        layout.addLayout(question5)
        layout.addLayout(question6)
        layout.addLayout(question7)
        layout.addWidget(calculate)
        layout.addLayout(result)

        container = QWidget()
        container.setLayout(layout)

        self.setWindowTitle("Area Math")

        self.setMinimumSize(QSize(400, 500))

        self.setCentralWidget(container)

        #the function of the app
        
        def Button_pressed():
            # gwindow height x window width x number of windows
            windowCalculation = input7.value() * input8.value() * input6.value()

            # number of doors x 2 for wall calculation (doors are 2 blocks high)
            doorCalculation = input5.value() * 2

            # wall width and wall depth are each multiplied by wall height, but also
            # each one is minus 1 because of sharing blocks with the other faces.
            # Times each one by 2 and add them together because there are four walls.
            # Also windows and doors are subtracted from the wall calculation
            # so that we're just counting wall blocks.
            singleFace1 = (input2.value() -1) * input1.value() 
            singleFace2 = (input3.value() - 1) * input1.value()
            wallCalculation = (singleFace1 * 2) + (singleFace2 * 2) - windowCalculation - doorCalculation
            
            # wall width and wall depth are used to calculate the floor area
            # of the building. (minus 2 because it's inside dimensions).
            # This is then used to calculate the floor blocks by multiplying by the amount
            # of floors and also adding the amount of doors (because you need a floor block
            # under a door).
            area = (input2.value() - 2) * (input3.value() - 2)
            floorCalculation = (area * input4.value()) + input5.value()
            # the roof however takes the wall width and wall depth and adds 2 before 
            # multiplying them together.  Adding 2 is because of the lip that most roofs
            # have.
            roofCalculation = (input2.value() + 2) * (input3.value() + 2)

            wallResult.setText(str(wallCalculation))
            floorResult.setText(str(floorCalculation))
            roofResult.setText(str(roofCalculation))
            windowResult.setText(str(windowCalculation))
        

        calculate.clicked.connect(Button_pressed)

        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()