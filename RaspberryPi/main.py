# !/usr/bin/env python

from UDP import UDPHandler
import numpy as np
import time

def main():
    udp = UDPHandler()
    
    img = np.zeros([1920,720,3], np.uint8)
    img[1,0] = 245
    
    tick = time.time()
    #udp.writeImg(img)
    udp.writeDataSerialized(img.tolist())
    print("Elapsed: " + str(time.time() - tick))
    
    #udp.writeString("Image")
    
    udp.close()

if __name__ == "__main__":
    main()