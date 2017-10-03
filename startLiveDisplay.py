"""
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: startLiveDisplay.py
__Description__: Load configuration, start UI

"""

import config
import time

from controller import Controller
from ui import UI
print "Start LiveDisplay"


userInterface = UI()
userInterface.start()

time.sleep(1)
updateManager = Controller(userInterface)

updateManager.start()

userInterface.join()
updateManager.stop()
updateManager.join()

print "Stop LiveDisplay"

