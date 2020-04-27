# !/usr/bin/env python

import socket
import numpy as np
import json

class UDPHandler:
    
    def __init__(self):
        self.host = "192.168.1.217"
        self.port = 6789
        # # UDP-Socket oeffnen
        self.addr = (self.host, self.port)
        self.UDPSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.buffersize = 32768

    def writeImg(self, img):
        data_bytes = img.tobytes()
        self.UDPSock.sendto(data_bytes, self.addr)

    def writeDataSerialized(self, data):
        serialized = json.dumps(data)
        data_bytes = bytes(serialized, 'UTF-8')
        
        print("Packages: " + str(len(data_bytes)/self.buffersize))
        
        i = 0
        while True:  
            
            if i+self.buffersize > len(data_bytes):
                self.UDPSock.sendto(data_bytes[i:], self.addr)
                break
            else:
                self.UDPSock.sendto(data_bytes[i:i+self.buffersize], self.addr)
        
            i = i + self.buffersize
            
    def writeString(self, data):
        data_bytes = data.encode('utf-8')
        self.UDPSock.sendto(data_bytes, self.addr)

    def close(self):
        self.UDPSock.close()
    