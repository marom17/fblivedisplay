"""
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: ui.py
__Description__: User interface

"""
from ui_clock import UI_Clock
from ui_onair import UI_Onair
from ui_online import UI_Online
from ui_music import UI_Music
import config
import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFrame
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class UI(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("FB Live Display")
        self.setWindowIcon(QIcon('fbld.ico'))
        if(not config.settingFullscreen):
            size = config.settingScreen.split('x')
            self.resize(int(size[0]),int(size[1]))
            self.setFixedSize(int(size[0]),int(size[1]))
            
        self.drawTop()
        self.drawBottom()
        
        if(not config.settingFullscreen):
            self.show()
        else:
            self.showFullScreen()
    
    '''
    Exit the program with escape key
    '''
    def keyPressEvent(self, event):
        
        if(event.key() == Qt.Key_Escape):
            self.close()
        
    '''
    Draw the top frame
    '''    
    def drawTop(self):
        #draw top frame
        self.frameTop = QFrame(self)
        self.frameTop.resize(self.width(),self.width()/3)
        self.frameTop.move(0,0)
        self.frameTop.setStyleSheet("background-color:white;")
        
        
        #set top layout
        self.topLayout = QHBoxLayout()
        self.topLayout.setSpacing(0)
        self.topLayout.setContentsMargins(0, 0, 0, 0)
        
        #init top UI
        self.uiclock = UI_Clock(self.frameTop)
        self.uionair = UI_Onair(self.frameTop)
        
        #assign top UI to layout
        self.topLayout.addWidget(self.uiclock)
        self.topLayout.addWidget(self.uionair)
        
        self.frameTop.setLayout(self.topLayout)
        self.frameTop.show()
        
    '''
    Draw the bottom frame
    '''
    def drawBottom(self):
        return
        