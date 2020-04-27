# !/usr/bin/env python

from UDP import UDPHandler
from Roboter import Roboter

class Master:
    
    def __init__(self):
        self.UDP = UDPHandler()
        self.Roboter = Roboter()
    
    def work(self):
        
        if self.UDP.messageReceived():
            msg = self.UDP.getMessage()
            if msg[0:4] == "Goto":
                pos = list(map(float,msg[5:].split(',')))
                print("Goto " + str(pos))
                self.Roboter.writePosition(pos[0],pos[1],pos[2])
            else:
                print("Invalid command")