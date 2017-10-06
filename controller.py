"""
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: updater.py
__Description__: Update all systems
@todo: put updateClock, updateOnline and updateOnair in sub controllers
"""

from threading import Thread
import time
from control_clock import Clock
from control_studioStatus import OnlineStatus
from control_axiaOnair import AxiaOnair
from control_musicPorgress import MusicProgress
from control_newSong import NewSong

class Controller(Thread):
    '''
    Class Controller
    functions:
        - run()
        - stop()
        - updateClock(newTime)
        - updateOnline(newStatus)
        - updateOnair(newStatus)
    '''
    def __init__(self, ui, updateQueue):
        Thread.__init__(self)
        self.updateQueue = updateQueue
        self.ui = ui
        self.running = True
        #initialize all controllers
        self.clock = Clock(self)
        self.online = OnlineStatus(self)
        self.onair = AxiaOnair(self)
        self.musicprogress = MusicProgress(self.ui.music)
        self.newSong = NewSong(self.musicprogress)
        
    '''
    Start all the controllers
    '''
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
            
    '''
    Stop all the controllers
    '''
    def stop(self):
        print "Update stop"
        self.running = False
        self.clock.stop()
        self.online.stop()
        self.onair.stop()
        self.newSong.stop()
        self.musicprogress.stop()
        
    '''
    Add an update to the updateQueue
    ''' 
    def addUpdate(self,update):
        self.updateQueue.put(update)
        
    '''
    Update the online status
    '''  
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
       
    '''
    Update the Onair status
    '''     
    def updateOnair(self, newStatus):
        try:
            updateData = ["onair"]
            if(newStatus != 2):
                if(newStatus == 0):
                    updateData.append("OffAir")
                    updateData.append("black")
                    self.addUpdate(updateData)
                elif(newStatus == 1):
                    updateData.append("OnAir")
                    updateData.append("red")
                    self.addUpdate(updateData)
                else:
                    updateData.append("Error")
                    updateData.append("yellow")
                    self.addUpdate(updateData)
            else:
                updateData.append("Error\nNo connection")
                updateData.append("yellow")
                self.addUpdate(updateData)
        except:
            print "Error"
