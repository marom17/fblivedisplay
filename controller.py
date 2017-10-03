"""
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: updater.py
__Description__: Update all systems

"""

from threading import Thread
import time
from control_clock import Clock
from control_studioStatus import OnlineStatus
from control_axiaOnair import AxiaOnair
from control_musicPorgress import MusicProgress
from control_newSong import NewSong

class Controller(Thread):
    
    def __init__(self, ui):
        Thread.__init__(self)
        
        self.ui = ui
        self.running = True
        self.clock = Clock(self)
        self.online = OnlineStatus(self)
        self.onair = AxiaOnair(self)
        self.musicprogress = MusicProgress(self.ui.music)
        self.newSong = NewSong(self.musicprogress)
        
    def run(self):
        print "Update Start"
        self.clock.start()
        self.online.start()
        self.onair.start()
        self.musicprogress.start()
        self.newSong.start()
        
        while(self.running):    
            time.sleep(0.5)
        
        self.clock.join()
        self.online.join()
        self.onair.join()
        self.newSong.join()
        self.musicprogress.join()
            
    def stop(self):
        print "Update stop"
        self.running = False
        self.clock.stop()
        self.online.stop()
        self.onair.stop()
        self.newSong.stop()
        self.musicprogress.stop()
        
    def updateClock(self, newTime):
        try:
            self.ui.clock.updateClock(newTime)
        except:
            print "Error"
        
    def updateOnline(self, newStatus):
        try:
            if(newStatus):
                if(newStatus[1]):
                    self.ui.online.updateOnline("Online", "green")
                else:
                    self.ui.online.updateOnline("Offline", "red")
            else:
                self.ui.online.updateOnline("Error", "yellow")
        except:
            print "Error"
            
    def updateOnair(self, newStatus):
        try:
            if(newStatus != 2):
                if(newStatus == 0):
                    self.ui.onair.updateOnair("OffAir", "black")
                    # self.ui.updateOnaire("OffAir","black")
                elif(newStatus == 1):
                    self.ui.onair.updateOnair("OnAir", "red")
                        # self.ui.updateOnaire("OnAir","red")
                else:
                    self.ui.onair.updateOnair("Error", "yellow")
                    # self.ui.updateOnaire("Error","yellow")
            else:
                self.ui.onair.updateOnair("Error\nNo connection", "yellow")
                # self.ui.updateOnaire("Error\nNo connection","yellow")
        except:
            print "Error"
