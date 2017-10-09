"""
__Author__: Romain Maillard
__Date__: 29.09.2017
__Name__: ui_music.py
__Description__: Music UI

"""

from signals import eventSignals
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QFrame, QWidget, QProgressBar,\
    QLayout, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class UI_Music(QFrame):
    '''
    Class UI_Music
    functions:
        - drawMusic
        - updateMusic(data)
        - updateTime(time)
        - updateBar(value,color)
    '''
    def __init__(self,parent):
        
        super().__init__()
        
        #Clock UI design
        self.setParent(parent)
        self.resize(parent.width(),parent.height())
        self.setStyleSheet("background-color:black;")
        self.setMaximumSize(parent.width(),parent.height())
        self.setAutoFillBackground(True)
        
        self.drawMusic()
        
        eventSignals.newSong.connect(self.updateMusic)
        eventSignals.updateTime.connect(self.updateTime)
        eventSignals.updateBar.connect(self.updateBar)
        self.show()
        
             
    '''
    Draw the frame
    '''   
    def drawMusic(self):
        
        self.musicFont = QFont("Times New Roman")
        self.musicFont.setPixelSize(self.height()/10)

        #artist
        self.artist = QLabel("",self)
        self.artist.setStyleSheet("color:white;")
        self.artist.setFont(self.musicFont)
        self.artist.setAlignment(Qt.AlignLeft)
        self.artist.setMaximumWidth(self.width())
        self.artist.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        
        #title
        self.title = QLabel("",self)
        self.title.setStyleSheet("color:white;")
        self.title.setFont(self.musicFont)
        self.title.setAlignment(Qt.AlignLeft)
        self.title.setMaximumWidth(self.width())
        self.title.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        
        #time
        self.time = QLabel("",self)
        self.time.setStyleSheet("color:white;")
        self.time.setFont(self.musicFont)
        self.time.setAlignment(Qt.AlignLeft)
        self.time.setMaximumWidth(self.width())
        self.time.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        
                
        #bar
        self.progressbar = QProgressBar(self)
        self.progressbar.setTextVisible(False)
        self.progressbar.setMinimumWidth(self.width()-10)
        self.progressbar.setMaximumWidth(self.width()-10)
        self.progressbar.setValue(0)
        self.progressbar.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        
        #layout
        self.musicLayout = QVBoxLayout()
        self.musicLayout.setAlignment(Qt.AlignCenter)
        self.musicLayout.setSpacing(10)
        self.musicLayout.setContentsMargins(0, 0, 0, 0)
        
                
        self.musicLayout.addWidget(self.artist)
        self.musicLayout.addWidget(self.title)
        self.musicLayout.addWidget(self.time)
        self.musicLayout.addWidget(self.progressbar)
        
        self.musicLayout.setAlignment(self.artist,Qt.AlignHCenter)
        self.musicLayout.setAlignment(self.title,Qt.AlignHCenter)
        self.musicLayout.setAlignment(self.time,Qt.AlignHCenter)
        self.musicLayout.setAlignment(self.progressbar,Qt.AlignCenter)
        
        self.artist.show()
        self.title.show()
        self.time.show()
        self.progressbar.show()
        
        self.setLayout(self.musicLayout)
               
    '''
    Update the music name
    ''' 
    def updateMusic(self,data):
        self.artist.setText(data[0].upper())
        self.title.setText(data[1])
        
    '''
    Update the time remaning
    '''
    def updateTime(self,time):
        self.time.setText(time)
       
    '''
    Update the progress bar
    ''' 
    def updateBar(self,value,color):
        if('intro' in color):
            color = "blue"
        elif('begin' in color):
            color = "green"
        elif('nend' in color):
            color = "orange"
        elif('end'):
            color = "red"
        else:
            color = "yellow"
            
        colorString = "::chunk{background-color:"+color+"}"
        self.progressbar.setValue(value)
        self.progressbar.setStyleSheet(colorString)