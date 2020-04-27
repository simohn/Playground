# !/usr/bin/env python

from Master import Master
import time

def main():
    
    m = Master()
    
    while True:
        m.work()
        time.sleep(0.1)
        

if __name__ == "__main__":
    main()