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
        self.artist = QLabel("Artist")
        self.artist.setStyleSheet("color:white;background-color:green;")
        self.artist.setFont(self.musicFont)
        self.artist.setAlignment(Qt.AlignCenter)
        self.artist.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Fixed)
        
        #title
        self.title = QLabel("Title")
        self.title.setStyleSheet("color:white;background-color:green;")
        self.title.setFont(self.musicFont)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Fixed)
        #time
        self.time = QLabel("01:12")
        self.time.setStyleSheet("color:white;background-color:green;")
        self.time.setFont(self.musicFont)
        self.time.setAlignment(Qt.AlignCenter)
        self.time.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Fixed)
        
                
        #bar
        self.progressbar = QProgressBar()
        self.progressbar.setTextVisible(False)
        self.progressbar.setAlignment(Qt.AlignCenter)
        self.progressbar.setMaximumWidth(self.width()-10)
        self.progressbar.setValue(0)
        self.progressbar.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        
        #layout
        self.musicLayout = QVBoxLayout()
        self.musicLayout.setAlignment(Qt.AlignVCenter)
        self.musicLayout.setAlignment(self.artist,Qt.AlignCenter)
        self.musicLayout.setAlignment(self.title,Qt.AlignCenter)
        self.musicLayout.setAlignment(self.time,Qt.AlignCenter)
        #self.musicLayout.setAlignment(self.progressbar,Qt.AlignCenter)
        self.musicLayout.setSpacing(10)
        self.musicLayout.setContentsMargins(0, 0, 0, 0)
        #self.musicLayout.setSizeConstraint(QLayout.SetFixedSize)
        
                
        self.musicLayout.addWidget(self.artist)
        self.musicLayout.addWidget(self.title)
        self.musicLayout.addWidget(self.time)
        self.musicLayout.addWidget(self.progressbar)
        self.artist.show()
        self.title.show()
        self.time.show()
        self.progressbar.show()
        
        self.setLayout(self.musicLayout)
               
    '''
    Update the music name
    ''' 
    def updateMusic(self,data):
        #string = data[0].upper()+"/"+data[1]
        self.artist.setText(data[0].upper())
        self.title.setText(data[1])
        '''self.artist.set(data[0].upper())
        self.title.set(data[1])'''
        
    '''
    Update the time remaning
    '''
    def updateTime(self,time):
        self.time.setText(time)
        'self.startTime.set(time)'
       
    '''
    Update the progress bar
    ''' 
    def updateBar(self,value,color):
        '''try:
            self.progress.set(value)
            self.progressBar["style"] = color
        except:
            print("Error")'''
        self.progressbar.setValue(value)