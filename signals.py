"""
__Author__: Romain Maillard
__Date__: 08.10.2017
__Name__: signals.py
__Description__: Handle all the signals of the application

"""
from PyQt5.QtCore import QObject, pyqtSignal

class Signals(QObject):
    
    clock = pyqtSignal([list])
    onair = pyqtSignal(str,str)
    online = pyqtSignal(str,str)
    
    
    
eventSignals = Signals()