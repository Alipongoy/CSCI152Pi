from PIL import Image
from picamera import PiCamera
from time import sleep
import cv2
import sys
import os

class Camera:
    def __init__(self):
        self.camera = PiCamera()
    
    def _warmUp(self, timeLength):
        sleep(timeLength)

    def _doesLocationExist(self, filename):
        return os.path.isfile(filename)
    
    def takePicture(self):
        self.camera.start_preview(fullscreen=False, window=(100,20,640,480))
        self._warmUp(3)

        locationToSaveTo = ("/home/pi/Documents/")
        imageString = "imgA.jpg"

        self.camera.capture(locationToSaveTo + imageString)

        print "File is saved to:" + locationToSaveTo + imageString

        self.camera.stop_preview()
        
        
