import os
import time

# Insert in console
# /opt/vc/bin/vcgencmd measure_temp

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

while True:
        print(measure_temp())
        time.sleep(1)