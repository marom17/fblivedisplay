"""
__Author__: Romain Maillard
__Date__: 29.09.2017
__Name__: control_musicProgress.py
__Description__: Get the actual music, display it and control startTime and bar

"""

import time
from signals import eventSignals
from PyQt5.QtCore import QThread

class MusicProgress(QThread):
    '''
    Class MusicProgress
    functions:
        - run()
        - stop()
        -newSong(intro,duration,title,artist)
        - converTime(seconds)
    '''
    def __init__(self):
        super().__init__()
        
        self.running = True
        self.intro = 0
        self.timesong = 0
        self.startTime = 0
        self.onIntro = False
        
    '''
    Check the time passed, change color of the progress bar and change the time
    '''
    def run(self):

        while(self.running):
            try:
                timepassed = (time.time() - self.startTime)
                
                #check if the time passed is higher that the time song
                if(timepassed <= self.timesong):
                    progress = (timepassed/float(self.timesong))*100
                    #check if we are on the intro
                    if(self.onIntro):
                        if(timepassed >= self.intro):
                            self.onIntro = False
                        progress = (timepassed/float(self.intro))*100
                        eventSignals.updateBar.emit(progress,"intro")
                        eventSignals.updateTime.emit(self.convertTime(self.intro - timepassed))
                    else:
                        
                        #change the color of the progressbar on the progress of the song
                        if(progress<95):
                            eventSignals.updateBar.emit(progress,"begin")
                        elif(progress<97):
                            eventSignals.updateBar.emit(progress,"nend")
                        elif(progress<100):
                            print(progress)
                            eventSignals.updateBar.emit(progress,"end")
                        else:
                            progress = 100
                            eventSignals.updateBar.emit(progress,"intro")
                        eventSignals.updateTime.emit(self.convertTime(self.timesong - timepassed))
                else:
                    progress = 100
                    eventSignals.updateBar.emit(progress,"intro")
            except:
                print("Error music")
            time.sleep(0.02)
     
    '''
    Stop the while loop of the controler
    '''       
    def stop(self):
        self.running = False
        
    '''
    Parse the new song information
    '''
    def newSong(self,intro,duration,title,artist):
        self.startTime = int(time.time())
        self.intro = intro
        #check if there is an intro to the song
        if(intro > 0):
            self.onIntro = True
        else:
            self.onIntro = False
        self.timesong = duration
        try:
            eventSignals.newSong.emit([artist,title])
            #self.musicUI.updateMusic([artist,title])
        except:
            print("Error new Song")
    
    '''
    Convert the time in secondes to a string xx:xx
    ''' 
    def convertTime(self,seconds):
        minutes = int(seconds/60)
        sec = int(seconds%60)
        string = ""
        
        if(minutes<10):
            string = string + "0" + str(minutes) 
        else:
            string = string + str(minutes)
        string = string + ":"
        if(sec<10):
            string = string + "0" + str(sec) 
        else:
            string = string + str(sec)
        return string
        