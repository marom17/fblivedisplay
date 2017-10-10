"""
__Author__: Romain Maillard
__Date__: 29.09.2017
__Name__: ui_online.py
__Description__: Online UI

"""

from signals import eventSignals
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QFrame, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class UI_Online(QFrame):
    '''
    Class UI_Online
    functions:
        - drawOnline()
        - updateOnline(newStatus,bg)
    '''
    def __init__(self,parent):
        super().__init__()
        
        self.setParent(parent)
        self.resize(parent.width()/3,parent.height())
        self.setStyleSheet("background-color:orange;")
        self.setMaximumSize(parent.width()/3+1,parent.height())
        self.setAutoFillBackground(True)
        
        self.drawOnline()
        
        eventSignals.online.connect(self.updateOnline)
        self.show()
    
    '''
    Draw the frame
    '''           
    def drawOnline(self):
        
        self.text = QLabel("Get Info",self)
        self.text.setAlignment(Qt.AlignCenter)
        self.textFont = QFont("Times New Roman")
        self.textFont.setPixelSize(self.height()/3-10)
        self.text.setFont(self.textFont)
        
        #layout
        self.textLayout = QVBoxLayout()
        self.textLayout.setAlignment(Qt.AlignCenter)
        
        self.textLayout.addWidget(self.text)
        
        self.text.show()
        self.setLayout(self.textLayout)
      
    '''
    Update the status
    '''  
    def updateOnline(self,newStatus,bg):
        background = "background-color:"+bg+";"
        self.text.setText(newStatus)
        self.setStyleSheet(background)