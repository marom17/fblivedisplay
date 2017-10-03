"""
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: ui.py
__Description__: User interface

"""

from Tkinter import *
from threading import Thread
from ui_clock import UI_Clock
from ui_onair import UI_Onair
from ui_online import UI_Online
from ui_music import UI_Music
import config

class UI(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        self.mainWindow = Tk()
        if(not config.settingFullscreen):
            self.mainWindow.geometry("500x500")
        else:
            self.mainWindow.attributes("-fullscreen", True) 
        self.mainWindow.configure(background='black')
        self.mainWindow.title("FB Live Display")
        self.mainWindow.resizable(False, False) 
        
        
        self.mainWindow.bind("<Key>",self.keyPressed)     
        
        
    def run(self):
        print "Start UI"
        #self.drawFrame()
        self.mainWindow.update_idletasks()
        self.mainWindow.update()
        self.drawFrame()
        self.mainWindow.mainloop()
    
    def keyPressed(self,event):
        try:
            if (ord(event.char)==27):
                self.mainWindow.quit()
            elif (ord(event.char) == 105):
                toplevel = Toplevel()
                message = Label(toplevel,text="Coucou")
                message.pack()
        except:
            print "Error"
        
    def drawFrame(self):
        self.drawTopFrame()
        self.drawBottomFrame()
        
    def drawTopFrame(self):
        self.frameTop = Frame(self.mainWindow,bg="black")
        self.frameTop.pack(side="top",fill='both')
        
        self.clock = UI_Clock(self.mainWindow.winfo_height()/3,self.frameTop)
        self.clock.drawClock()
        
        self.onair = UI_Onair(self.mainWindow.winfo_height()/3,self.frameTop)
        self.onair.drawOnair()
        
        self.online = UI_Online(self.mainWindow.winfo_height()/3,self.frameTop)
        self.online.drawOnline()
        
        
    def drawBottomFrame(self):        
        self.frameBottom = Frame(self.mainWindow,bg="black")
        self.frameBottom.pack(side="top",fill='both',expand=True)
        
        self.music = UI_Music(self.mainWindow.winfo_width(),self.mainWindow.winfo_height(),self.frameBottom)
        self.music.drawMusic()
        
        