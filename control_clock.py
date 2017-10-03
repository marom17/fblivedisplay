"""
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: control_clock.py
__Description__: Give the current time

"""

import time
from threading import Thread

class Clock(Thread):

    def __init__(self,controller):
        Thread.__init__(self)
        self.running = True
        self.controller = controller
        
    def run(self):
        while self.running:
            self.controller.updateClock(self.update())
            time.sleep(0.5)
            
    def update(self):
        actualTime = time.strftime("%H:%M%S",time.localtime())
        return [actualTime[:-2],actualTime[-2:]]
    
    def stop(self):
        self.running = False