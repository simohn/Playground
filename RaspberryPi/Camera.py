# Code written by Simon Schauppenlehner
# Last change: 22.06.2019

from picamera import PiCamera
from picamera.array import PiRGBArray
import numpy as np
import time


def motion_detector():

    camera = PiCamera()
    camera.resolution = (1088, 720)
    #camera.rotation = 180

    camera_array = PiRGBArray(camera)

    print("[INFO] warming up...")
    time.sleep(1)

    camera.capture(camera_array, format="bgr")
    
    print(camera_array.array.shape)
    print(camera_array.array.dtype)
    
    camera_array.truncate(0)


if __name__ == "__main__":
    motion_detector()

