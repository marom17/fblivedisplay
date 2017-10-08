"""
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: startLiveDisplay.py
__Description__: Load configuration, start UI

"""

import config
import time
from PyQt5.QtWidgets import QApplication


from controller import Controller
from ui import UI
import sys

app = QApplication(sys.argv)

print("Start LiveDisplay")

#create and start the usre interface
userInterface = UI()
#userInterface.start()

time.sleep(1)
#start the controllers
#updateManager = Controller(userInterface)

#updateManager.start()
#userInterface.join()
#updateManager.stop()
#updateManager.join()


sys.exit(app.exec_())
print("Stop LiveDisplay")

