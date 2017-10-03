"""
__Author__: Romain Maillard
__Date__: 29.09.2017
__Name__: ui_music.py
__Description__: Music UI

"""

from Tkinter import *
import ttk

class UI_Music():
    '''
    Class UI_Music
    functions:
        - drawMusic
        - updateMusic(data)
        - updateTime(time)
        - updateBar(value,color)
    '''
    def __init__(self,width,height,parent):
        self.frameMusic = Frame(parent,bg="black",width=width,height=(2*height/3))
        self.frameInfos = Frame(self.frameMusic,bg="black",width=width,height=(2*height/3))
        self.title = StringVar()
        self.title.set("")
        self.startTime = StringVar()
        self.startTime.set("")
        self.progress = IntVar()
        self.progress.set(0)
        
        #Configure Bar colors
        self.barIntro = ttk.Style()
        self.barIntro.theme_use('winnative')
        self.barIntro.configure("intro.Horizontal.TProgressbar", foreground='blue', background='blue')
        
        self.barMusicBegin = ttk.Style()
        self.barMusicBegin.theme_use('winnative')
        self.barMusicBegin.configure("begin.Horizontal.TProgressbar", foreground='green', background='green')
        
        self.barMusicNearlyEnd = ttk.Style()
        self.barMusicNearlyEnd.theme_use('winnative')
        self.barMusicNearlyEnd.configure("nend.Horizontal.TProgressbar", foreground='orange', background='orange')
        
        self.barMusicEnd = ttk.Style()
        self.barMusicEnd.theme_use('winnative')
        self.barMusicEnd.configure("end.Horizontal.TProgressbar", foreground='red', background='red')
        
        #configure object
        self.progressBar = ttk.Progressbar(self.frameInfos,orient=HORIZONTAL,length=(width-100),mode='determinate',variable=self.progress)
        self.champ_title = Label(self.frameInfos,textvariable=self.title,bg="black",fg="white",font=("Times New Roman",30),wraplength=(width-5),height=1,anchor="nw")
        self.champ_time = Label(self.frameInfos,textvariable=self.startTime,bg="black",fg="white",font=("Times New Roman",30))
     
    '''
    Draw the frame
    '''   
    def drawMusic(self):
        
        #self.frameMusic.pack_propagate(False)
        self.frameMusic.pack(expand=True)
        
        self.frameInfos.place(relx=.5, rely=.5, anchor="c")
        self.frameInfos.pack()
        #.champ_title.place(relx=.5, rely=.5, anchor="c")
        self.champ_title.pack()
        #self.progressBar.place(relx=.5, rely=.5, anchor="c")
        self.champ_time.pack()
        
        self.progressBar["style"]="begin.Horizontal.TProgressbar"
        #self.progressBar["value"]=50
        self.progressBar.pack()
       
    '''
    Update the music name
    ''' 
    def updateMusic(self,data):
        string = data[0].upper()+"/"+data[1]
        self.title.set(string)
        
    '''
    Update the time remaning
    '''
    def updateTime(self,time):
        self.startTime.set(time)
       
    '''
    Update the progress bar
    ''' 
    def updateBar(self,value,color):
        try:
            self.progress.set(value)
            self.progressBar["style"] = color
        except:
            print "Error"