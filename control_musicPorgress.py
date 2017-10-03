"""
__Author__: Romain Maillard
__Date__: 29.09.2017
__Name__: control_musicProgress.py
__Description__: Get the actual music, display it and control passedtime and bar

"""

import time
from threading import Thread

class MusicProgress(Thread):
    
    def __init__(self,musicUI):
        Thread.__init__(self)
        
        self.running = True
        self.musicUI = musicUI
        self.intro = 0
        self.timesong = 0
        self.passedtime = 0
        self.onIntro = False
        
    def run(self):
        
        #time.sleep(1)
        #self.newSong(5,10)
        while(self.running):
            timepassed = (int(time.time()) - self.passedtime)
            if(timepassed <= self.timesong):
                progress = int((timepassed/float(self.timesong))*100)
                if(self.onIntro):
                    if(timepassed >= self.intro):
                        self.onIntro = False
                    progress = int((timepassed/float(self.intro))*100) 
                    self.musicUI.updateBar(progress,"intro.Horizontal.TProgressbar")
                    self.musicUI.updateTime(self.convertTime(self.intro - timepassed))
                else:
                    
                    if(progress<70):
                        self.musicUI.updateBar(progress,"begin.Horizontal.TProgressbar")
                    elif(progress<85):
                        self.musicUI.updateBar(progress,"nend.Horizontal.TProgressbar")
                    elif(progress<100):
                        self.musicUI.updateBar(progress,"end.Horizontal.TProgressbar")
                    else:
                        self.musicUI.updateBar(progress,"intro.Horizontal.TProgressbar")
                    self.musicUI.updateTime(self.convertTime(self.timesong - timepassed))
            time.sleep(0.5)
            
    def stop(self):
        self.running = False
        
    def newSong(self,intro,duration,title,artist):
        self.passedtime = int(time.time())
        self.intro = intro
        if(intro > 0):
            self.onIntro = True
        else:
            self.onIntro = False
        self.timesong = duration
        self.musicUI.updateMusic([artist,title])
        
    def convertTime(self,seconds):
        min = int(seconds/60)
        sec = int(seconds%60)
        string = ""
        
        if(min<10):
            string = string + "0" + str(min) 
        else:
            string = string + str(min)
        string = string + ":"
        if(sec<10):
            string = string + "0" + str(sec) 
        else:
            string = string + str(sec)
        return string
        