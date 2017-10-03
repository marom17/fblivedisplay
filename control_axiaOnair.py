"""
__Author__: Romain Maillard
__Date__: 27.09.2017
__Name__: control_axiaOnair.py
__Description__: Check if the micros are open

"""

import socket
import config
from threading import Thread
import time

class AxiaOnair(Thread):
    
    '''
    Class AxiaOnair
    functions:
        - run()
        - stop()
    '''
    def __init__(self,controller):
        Thread.__init__(self)
        self.controller = controller
        self.socket = None
        self.running = True
        
    '''
    Monitor the status of the gpo of the microphone
    '''
    def run(self):
        
        while(self.running):
            #creat the socket with a timeout of 3 seconds
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(3)
            try:
                self.socket.connect((config.axiahost, config.axiaport))
            except :
                self.socket.close()
                #Error message on UI
                self.controller.updateOnair(3)
                break;
                
            try:
                #check the GPO and send the result
                self.socket.sendall("GPO "+config.axiagpio+"\r\n")
                data = self.socket.recv(2048)
                if not data: break
                stringdata = data.decode('utf-8')
                
                gpo = "GPO " + config.axiagpio
                if gpo in stringdata:
                    if("lhhhh" in stringdata):
                        #micros are on
                        self.controller.updateOnair(1)
                    if("hhhhh" in stringdata):
                        #micro are off
                        self.controller.updateOnair(0)   
            except:
                self.controller.updateOnair(3)
            self.socket.close()
            time.sleep(0.5)
    '''
    Stop the loop
    '''
    def stop(self):
        self.running = False