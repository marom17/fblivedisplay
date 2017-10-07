"""
__Author__: Romain Maillard
__Date__: 29.09.2017
__Name__: ui_clock.py
__Description__: Clock UI

"""

from tkinter import *

class UI_Clock():
    '''
    Class UI_Clock
    function:
        - drawClock()
        - updateClock(newTime)
    '''
    
    def __init__(self,height,parent):
        self.timeTop = StringVar()
        self.timeBottom = StringVar()
        self.timeTop.set("")
        self.timeBottom.set("")
        self.frameClock = Frame(parent,bg="black",height=height)
        self.champ_clockTop = Label(self.frameClock, textvariable = self.timeTop,bg="black",fg="red",font=("QuiverItal",50))
        self.champ_clockBottom = Label(self.frameClock, textvariable = self.timeBottom,bg="black",fg="red",font=("QuiverItal",45),justify="center")
        #self.champ_clockTop = Label(self.frameClock, textvariable = self.timeTop,bg="black",fg="red",font=("Digital-7",50))
        #self.champ_clockBottom = Label(self.frameClock, textvariable = self.timeBottom,bg="black",fg="red",font=("Digital-7",45),justify="center")  
        
    '''
    Draw the initial clock
    '''
    def drawClock(self):
        self.frameClock.pack_propagate(False)
        self.frameClock.grid(row=0,column=1)
        self.frameClock.pack(side="left",expand=True,fill='both')    
        self.champ_clockTop.place(relx=.5, rely=.5, anchor="c")
        self.champ_clockTop.pack(expand=True)
        self.champ_clockBottom.pack()
    
    '''
    Update the clock
    '''
    def updateClock(self,newTime):
        self.timeTop.set(newTime[0])
        self.timeBottom.set(newTime[1])