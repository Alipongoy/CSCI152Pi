#from PIL import Image
#from picamera import PiCamera
from time import sleep
#import cv2
import sys
import os
import pdb

class Camera:
    def __init__(self):
        #self.camera = PiCamera()
        self.__locationToSaveTo = ("/home/pi/Documents/")

    
    def _warmUp(self, timeLength):
        sleep(timeLength)

    def _doesLocationExist(self, filename):
        return os.path.isfile(filename)
    
    def _generateImageLocation(self):
        counter = 0
        fullString = self.__locationToSaveTo + "img" + str(counter) + "jpg"
        while (self._doesLocationExist(fullString)):
            counter += 1
            fullString = self.__locationToSaveTo + "img" + str(counter) + "jpg"
        return fullString

    def setSaveLocation(self, locationToSaveTo):
        self.__locationToSaveTo = locationToSaveTo

    def takePicture(self, imageName):
        pdb.set_trace()
        self.camera.start_preview(fullscreen=False, window=(100,20,640,480))
        self._warmUp(3)

        imageLocation = self.__locationToSaveTo + imageName
        self.camera.capture(imageLocation)

        print "File is saved to:" + imageLocation

        self.camera.stop_preview()

x = Camera()
pdb.set_trace()
