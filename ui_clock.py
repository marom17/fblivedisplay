"""
__Author__: Romain Maillard
__Date__: 29.09.2017
__Name__: ui_clock.py
__Description__: Clock UI

"""
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QFrame, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from signals import eventSignals


class UI_Clock(QFrame):
    
    '''
    Class UI_Clock
    function:
        - updateClock(newTime)
    '''
    
    def __init__(self,parent):
        super().__init__()
        
        #Clock UI design
        self.setParent(parent)
        self.resize(parent.width()/3,parent.height())
        print(self.width(),self.height(),parent.width(),parent.height())
        self.setStyleSheet("background-color:black;")
        self.setMaximumSize(parent.width()/3,parent.height())
        self.setAutoFillBackground(True)
        
        #Clock text
        self.topText = QLabel(self)
        self.bottomText = QLabel(self)
        
        self.clockFont = QFont("QuiverItal")
        self.clockFont.setPixelSize(self.height()/3)
        
        self.topText.setMaximumSize(self.height(), self.width())
        self.bottomText.setMaximumSize(self.height(), self.width())
        
        #set font
        self.topText.setFont(self.clockFont)
        self.bottomText.setFont(self.clockFont)
        
        #set layout        
        self.textLayout = QVBoxLayout()
        self.textLayout.setAlignment(Qt.AlignCenter)
        self.textLayout.setSpacing(10)
        self.textLayout.setContentsMargins(0, 0, 0, 0)
        self.textLayout.addWidget(self.topText)
        self.textLayout.addWidget(self.bottomText)
        self.setLayout(self.textLayout)
        
        #set alignement
        self.topText.setAlignment(Qt.AlignCenter)
        self.bottomText.setAlignment(Qt.AlignCenter)
        
        self.topText.setStyleSheet("color:red;")
        self.bottomText.setStyleSheet("color:red;")
        
        self.topText.setText("12:30")
        self.bottomText.setText("25")
        
        self.topText.show()
        self.bottomText.show()
        
        eventSignals.clock.connect(self.updateClock)
        self.show()
    
    '''
    Update the clock
    '''
    def updateClock(self,newTime):
        self.topText.setText(newTime[0])
        self.bottomText.setText(newTime[1])