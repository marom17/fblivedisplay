"""
__Author__: Romain Maillard
__Date__: 29.09.2017
__Name__: ui_onair.py
__Description__: Onair UI

"""

from signals import eventSignals
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QFrame, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
#from tkinter import *

class UI_Onair(QFrame):
    '''
    Class UI_Onair
    functions:
        - drawOnair()
        - updateOnair(newStatus,bg)
    '''
    def __init__(self,parent):
        super().__init__()
        
        self.setParent(parent)
        self.resize(parent.width(),parent.width()/3)
        self.setStyleSheet("background-color:orange;")
        self.setMaximumSize(parent.width()/3+1,parent.height())
        self.setAutoFillBackground(True)
        
        self.drawOnair()
        
        self.show()
        
        eventSignals.onair.connect(self.updateOnair)
        
    '''
    Draw the frame
    '''
    def drawOnair(self):
        
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
    def updateOnair(self,newStatus,bg):
        background = "background-color:"+bg+";"
        self.text.setText(newStatus)
        self.setStyleSheet(background)
        