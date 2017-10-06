"""
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: startLiveDisplay.py
__Description__: Load configuration, start UI

"""

import config
import time
from Queue import Queue

from controller import Controller
from ui import UI
print "Start LiveDisplay"

updateQueue = Queue()
#create and start the usre interface
userInterface = UI(updateQueue)
userInterface.drawMainWindow()
#start the controllers
updateManager = Controller(userInterface,updateQueue)

updateManager.start()
userInterface.startMainLoop()
updateManager.stop()
updateManager.join()

print "Stop LiveDisplay"

