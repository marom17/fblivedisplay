"""
__Author__: Romain Maillard
__Date__: 29.09.2017
__Name__: ui_online.py
__Description__: Online UI

"""
import tkinter
from tkinter import *

class UI_Online():
    '''
    Class UI_Online
    functions:
        - drawOnline()
        - updateOnline(newStatus,bg)
    '''
    def __init__(self,height,parent):
        self.status = StringVar()
        self.status.set("Get Info")
        self.frameOnline = Frame(parent,bg="orange",height=height)
        self.champ_online = Label(self.frameOnline, textvariable = self.status,bg="orange",fg="black",font=("Times New Roman",30))
    
    '''
    Draw the frame
    '''           
    def drawOnline(self):
        
        self.frameOnline.pack_propagate(False)
        #self.frameOnline.grid(row=0,column=3)
        #self.frameOnline.place(rely=0)
        self.frameOnline.pack(side="left",expand=True,fill='both')
        self.champ_online.place(relx=.5, rely=.5, anchor="c")
        self.champ_online.pack(expand=True)
      
    '''
    Update the status
    '''  
    def updateOnline(self,newStatus,bg):
            self.status.set(newStatus)
            self.champ_online["bg"]=bg
            self.frameOnline["bg"]=bg