"""
__Author__: Romain Maillard
__Date__: 29.09.2017
__Name__: control_newSong.py
__Description__: Get the actual music, display it and control time and bar

"""

import time
import config
import xml.etree.ElementTree as ET
#import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PyQt5.QtCore import QThread

class NewSongHandler(FileSystemEventHandler):
    def __init__(self,songcontrol):
        FileSystemEventHandler.__init__(self)
        self.songcontrol = songcontrol
        
    def on_modified(self, event):
        #check if the modification is made on the xml file
        if(config.winmediafile in event.src_path):
            time.sleep(0.2)
            self.songcontrol.readXml()

class NewSong(QThread):
    '''
    Class NewSong
    functions:
        - run()
        - stop()
        - readXml()
    '''
    
    def __init__(self,controlprogress):
        super().__init__()
        
        self.running = True
        self.controlprogress = controlprogress
        
    '''
    Create the file modification observer
    '''
    def run(self):
        self.readXml()
        event_handler = NewSongHandler(self)
        observer = Observer()
        observer.schedule(event_handler, path='.', recursive=False)
        observer.start()
        
        #running loop
        while(self.running):
            time.sleep(1)
            
        observer.stop()
        observer.join()
    
    '''
    Stop the loop
    '''
    def stop(self):
        self.running = False
       
    '''
    Parse the xml file to extract the informations
    ''' 
    def readXml(self):
        try:
            #print(config.winmediafile)
            #tree = ET.parse(config.winmediafile)
            tree = ET.parse('newSong.xml')
            title = tree.findtext("title")
            artist = tree.findtext("artist")
            intro = int(tree.findtext("intro"))
            duration = int(tree.findtext("duration"))
            self.controlprogress.newSong(intro,duration,title,artist)
        except IOError:
            print("No xml file found")