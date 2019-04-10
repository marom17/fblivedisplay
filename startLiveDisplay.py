"""
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: startLiveDisplay.py
__Description__: Load configuration, start UI

"""

import config
import time

from ui import UI
print("Start LiveDisplay")

#create and start the usre interface
userInterface = UI()
userInterface.start()

print("Stop LiveDisplay")

