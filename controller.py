"""
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: updater.py
__Description__: Update all systems
@todo: put updateClock, updateOnline and updateOnair in sub controllers
"""

import time
from signals import eventSignals
from control_clock import Clock
from control_studioStatus import OnlineStatus
from control_axiaOnair import AxiaOnair
from control_musicPorgress import MusicProgress
from control_newSong import NewSong
from PyQt5.QtCore import QThread

class Controller(QThread):
    '''
    Class Controller
    functions:
        - run()
        - stop()
        - updateClock(newTime)
        - updateOnline(newStatus)
        - updateOnair(newStatus)
    '''
    def __init__(self, ui):
        super().__init__()
        
        self.ui = ui
        self.running = True
        #initialize all controllers
        self.clock = Clock(self)
        self.online = OnlineStatus(self)
        self.onair = AxiaOnair(self)
        self.musicprogress = MusicProgress()
        self.newSong = NewSong(self.musicprogress)
        
    '''
    Start all the controllers
    '''
    def run(self):
        print("Update Start")
        self.clock.start()
        self.online.start()
        self.onair.start()
        self.musicprogress.start()
        self.newSong.start()
        
        while(self.running):    
            time.sleep(0.5)
        
        self.clock.wait()
        self.online.wait()
        self.onair.wait()
        self.newSong.wait()
        self.musicprogress.wait()
            
    '''
    Stop all the controllers
    '''
    def stop(self):
        print("Update stop")
        self.running = False
        self.clock.stop()
        self.online.stop()
        self.onair.stop()
        self.newSong.stop()
        self.musicprogress.stop()
        
    '''
    Update the clock
    '''
    def updateClock(self, newTime):
        try:
            self.ui.clock.updateClock(newTime)
        except:
            print("Error")
      
    '''
    Update the online status
    '''  
    def updateOnline(self, newStatus):
        try:
            if(newStatus):
                if(newStatus[1]):
                    eventSignals.online.emit("Online", "lime")
                    #self.ui.online.updateOnline("Online", "green")
                else:
                    eventSignals.online.emit("Offline", "red")
                    #self.ui.online.updateOnline("Offline", "red")
            else:
                eventSignals.online.emit("Error", "yellow")
                #self.ui.online.updateOnline("Error", "yellow")
        except:
            print("Error")
       
    '''
    Update the Onair status
    '''     
    def updateOnair(self, newStatus):
        try:
            if(newStatus != 2):
                if(newStatus == 0):
                    eventSignals.onair.emit("OffAir", "black")
                elif(newStatus == 1):
                    eventSignals.onair.emit("OnAir", "red")
                else:
                    eventSignals.onair.emit("Error", "yellow")
            else:
                eventSignals.onair.emit("Error\nNo connection", "yellow")
        except:
            print("Error")
