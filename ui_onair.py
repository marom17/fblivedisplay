"""
__Author__: Romain Maillard
__Date__: 29.09.2017
__Name__: ui_onair.py
__Description__: Onair UI

"""

from Tkinter import *

class UI_Onair():
    
    def __init__(self,heigth,parent):
        self.status = StringVar()
        self.status.set("Get Info")
        self.frameOnair = Frame(parent,bg="orange",height=heigth)
        self.champ_onair = Label(self.frameOnair, textvariable=self.status,bg="orange",fg="black",font=("Times New Roman",30))
        
    def drawOnair(self):
        self.frameOnair.pack_propagate(False)
        self.frameOnair.grid(row=0,column=2)
        #self.frameOnair.place(rely=0)
        self.frameOnair.pack(side="left",expand=True,fill='both')
        self.champ_onair.place(relx=.5, rely=.5, anchor="c")
        self.champ_onair.pack(expand=True)
        
    def updateOnair(self,newStatus,bg):
        self.status.set(newStatus)
        self.champ_onair["bg"]=bg
        self.frameOnair["bg"]=bg