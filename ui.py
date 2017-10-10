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
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QFrame, QMainWindow,\
    QSplashScreen, QApplication
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class UI(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        splash = QPixmap("splash.png")
        splashscreen = QSplashScreen(splash)
        splashscreen.show()
        self.setWindowTitle("FB Live Display")
        self.setWindowIcon(QIcon('fbld.ico'))
        if(not config.settingFullscreen):
            size = config.settingScreen.split('x')
            self.resize(int(size[0]),int(size[1]))
            self.setFixedSize(int(size[0]),int(size[1]))
        else:
            rec = QApplication.desktop().screenGeometry()
            print(rec)
            self.resize(rec.width(),rec.height())
            self.setFixedSize(rec.width(),rec.height())
            
        self.drawTop()
        self.drawBottom()
        
        if(not config.settingFullscreen):
            self.show()
        else:
            self.showFullScreen()
        
        splashscreen.finish(self)
    
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
        self.frameTop.resize(self.width(),self.height()/3)
        self.frameTop.move(0,0)
        self.frameTop.setStyleSheet("background-color:black;")
        self.frameTop.setMinimumSize(self.width(),self.height()/3)
        
        #set top layout
        self.topLayout = QHBoxLayout()
        self.topLayout.setSpacing(0)
        self.topLayout.setContentsMargins(0, 0, 0, 0)
        
        #init top UI
        self.uiclock = UI_Clock(self.frameTop)
        self.uionair = UI_Onair(self.frameTop)
        self.uionline = UI_Online(self.frameTop)
        
        #assign top UI to layout
        self.topLayout.addWidget(self.uiclock)
        self.topLayout.addWidget(self.uionair)
        self.topLayout.addWidget(self.uionline)
        
        self.frameTop.setLayout(self.topLayout)
        self.frameTop.show()
        
    '''
    Draw the bottom frame
    '''
    def drawBottom(self):
        self.frameBottom = QFrame(self)
        self.frameBottom.resize(self.width(),2*self.height()/3)
        self.frameBottom.move(0,self.height()/3)
        self.frameBottom.setStyleSheet("background-color:black;")
        self.frameBottom.setMinimumSize(self.width(),self.height()/3)
        
        self.uimusic = UI_Music(self.frameBottom)
        
        
        self.frameBottom.show()
        