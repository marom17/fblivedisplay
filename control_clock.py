"""
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: control_clock.py
__Description__: Give the current time

"""

import time
from signals import eventSignals
from PyQt5.QtCore import QThread

class Clock(QThread):
    '''
    Class Clock
    functions:
        - run()
        - update()
        - stop()
    '''
    def __init__(self,controller):
        super().__init__()
        self.running = True
        self.controller = controller
        
    def run(self):
        while self.running:
            #change the time display in the UI
            eventSignals.clock.emit(self.update())
            #self.controller.updateClock(self.update())
            time.sleep(0.5)
            
    '''
    Return the actual local time
    '''
    def update(self):
        actualTime = time.strftime("%H:%M%S",time.localtime())
        return [actualTime[:-2],actualTime[-2:]]
    
    '''
    Stop the loop
    '''
    def stop(self):
        self.running = False