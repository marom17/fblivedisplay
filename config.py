'''
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: config.py
__Description__: Read the configuration file
'''

import ConfigParser

#parse the config file
config = ConfigParser.RawConfigParser()
config.read('livedisplay.conf')

settingFullscreen = config.getint('settings','fullscreen')
settingScreen = config.get('settings','screen')
     
commuthost = config.get('commut','host')
commutport = config.getint('commut','port')   
commuturl = config.get('commut', "url")
commutchan = config.get('commut', "chan")
       
axiahost = config.get('axia', "host")
axiaport = config.getint('axia', "port")
axiagpio = config.get('axia', "gpnum")

winmediahost = config.get('winmedia','host')
winmediaport = config.getint('winmedia','port')
winmediafile = config.get('winmedia','file')
        
        
                
