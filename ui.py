"""
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: ui.py
__Description__: User interface

"""
import tkinter
from tkinter import *
from ui_clock import UI_Clock
from ui_onair import UI_Onair
from ui_online import UI_Online
from ui_music import UI_Music
import config
import sys
from controller import Controller

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
    def __init__(self):
        self.mainWindow = Tk()
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
    Draw the main window and all the subview
    '''
    def start(self):
        print("Start UI")
        #self.drawFrame()
        self.mainWindow.update_idletasks()
        self.mainWindow.update()
        self.drawFrame()
        #start the controllers
        self.updateManager = Controller(self)

        self.updateManager.start()
        try:
            self.mainWindow.protocol("WM_DELETE_WINDOW", self.on_closing) 
            self.mainWindow.mainloop()
        except:
            print("Unexpected error:", sys.exc_info()[0])
    
    def drawMainWindow(self):
        print("Start UI")
        #self.drawFrame()
        self.mainWindow.update_idletasks()
        self.mainWindow.update()
        self.drawFrame()
        try:
            self.mainWindow.mainloop()
        except:
            print("Unexpected error:", sys.exc_info()[0])
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
            print("Error")
    
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

    '''
    Stop controller when closing the window
    '''
    def on_closing(self):
        self.updateManager.stop()
        self.updateManager.join()
        self.mainWindow.destroy()
        
        