"""
__Author__: Romain Maillard
__Date__: 29.09.2017
__Name__: control_newSong.py
__Description__: Get the actual music, display it and control time and bar

"""

import time
import config
from threading import Thread
import xml.etree.ElementTree as ET
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class NewSongHandler(FileSystemEventHandler):
    def __init__(self,songcontrol):
        FileSystemEventHandler.__init__(self)
        self.songcontrol = songcontrol
        
    def on_modified(self, event):
        if("newSong.xml" in event.src_path):
            self.songcontrol.readXml()

class NewSong(Thread):
    
    def __init__(self,controlprogress):
        Thread.__init__(self)
        
        self.running = True
        self.controlprogress = controlprogress
        
    def run(self):
        self.readXml()
        event_handler = NewSongHandler(self)
        observer = Observer()
        observer.schedule(event_handler, path='.', recursive=False)
        observer.start()
        while(self.running):
           
            time.sleep(1)
            
        observer.stop()
        observer.join()
    
    def stop(self):
        self.running = False
        
    def readXml(self):
        try:
            tree = ET.parse(config.winmediafile)
            title = tree.findtext("title")
            artist = tree.findtext("artist")
            intro = int(tree.findtext("intro"))
            duration = int(tree.findtext("duration"))
            self.controlprogress.newSong(intro,duration,title,artist)
        except IOError:
            print "No xml file found"