"""
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: ui.py
__Description__: User interface

"""

from Tkinter import *
from ui_clock import UI_Clock
from ui_onair import UI_Onair
from ui_online import UI_Online
from ui_music import UI_Music
import config
import sys
import Queue

class UI():
    '''
    Class UI
    functions:
        - run()
        - keyPressed(event)
        - drawFrame()
        - drawTopFrame()
        - drawottomFrame()
    '''
    def __init__(self,updateQueue):
        self.updateQueue = updateQueue
        self.mainWindow = Tk()
        self.running = True
        #check if we active fullscreen
        if(not config.settingFullscreen):
            self.mainWindow.geometry(config.settingScreen)
        else:
            self.mainWindow.attributes("-fullscreen", True) 
        self.mainWindow.configure(background='black')
        self.mainWindow.title("FB Live Display")
        #desactivate the resize
        self.mainWindow.resizable(False, False) 
        
        
        self.mainWindow.bind("<Key>",self.keyPressed)
        
    '''
    Check ui update
    '''
    def getUpdate(self):
        if(self.running):
            try:
                while True:
                    UIupdate = self.updateQueue.get(block=False)
                    if("clock" in UIupdate[0]):
                        self.clock.updateClock(UIupdate[1])
                    elif("onair" in UIupdate[0]):
                        self.onair.updateOnair(UIupdate[1], UIupdate[2])
                        print "onair"
                    elif("online" in UIupdate[0]):
                        print "online"
                    elif("newSong"):
                        print "newSonf"
                    elif("progress"):
                        print "progress"
            except Queue.Empty:
                pass;
            self.mainWindow.after(300,self.getUpdate)
    '''
    Draw the main window
    '''
    def drawMainWindow(self):
        print "Start UI"
        #self.drawFrame()
        self.mainWindow.update_idletasks()
        self.mainWindow.update()
        self.drawFrame()
        
    '''
    Start the big loop
    '''
    def startMainLoop(self):
        try:
            self.mainWindow.after(0, self.getUpdate)
            self.mainWindow.mainloop()
            self.running = False
        except:
            print "Unexpected error:", sys.exc_info()[0]
    '''
    Monitor the key that are pressed
    '''
    def keyPressed(self,event):
        try:
            #escape quit the application
            if (ord(event.char)==27):
                self.mainWindow.quit()
            #i display on message
            elif (ord(event.char) == 105):
                toplevel = Toplevel()
                message = Label(toplevel,text="Coucou")
                message.pack()
        except:
            print "Error"
    
    '''
    Draw the window
    '''
    def drawFrame(self):
        self.drawTopFrame()
        self.drawBottomFrame()
        
    '''
    Draw the top part of the window
    '''
    def drawTopFrame(self):
        self.frameTop = Frame(self.mainWindow,bg="black")
        self.frameTop.pack(side="top",fill='both')
        
        self.clock = UI_Clock(self.mainWindow.winfo_height()/3,self.frameTop)
        self.clock.drawClock()
        
        self.onair = UI_Onair(self.mainWindow.winfo_height()/3,self.frameTop)
        self.onair.drawOnair()
        
        self.online = UI_Online(self.mainWindow.winfo_height()/3,self.frameTop)
        self.online.drawOnline()
        
    '''
    Draw the bottom part of the window
    '''   
    def drawBottomFrame(self):        
        self.frameBottom = Frame(self.mainWindow,bg="black")
        self.frameBottom.pack(side="top",fill='both',expand=True)
        
        self.music = UI_Music(self.mainWindow.winfo_width(),self.mainWindow.winfo_height(),self.frameBottom)
        self.music.drawMusic()
        
        