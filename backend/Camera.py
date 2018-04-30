from PIL import Image
from picamera import PiCamera
from time import sleep
import os
import pdb

class Camera:
    def __init__(self):
        self.camera = PiCamera()
        self.__locationToSaveTo = ("parking_lot_images/")
        # self.__locationToSaveTo = ("/home/pi/Documents/")

    def _warmUp(self, timeLength):
        sleep(timeLength)

    def setSaveLocation(self, locationToSaveTo):
        self.__locationToSaveTo = locationToSaveTo

    def openCamera(self):
        try:
            self.camera.start_preview(fullscreen=False, window=(100,20,640,480))

        except KeyboardInterrupt:
            print "Camera will now close."
            self.camera.stop_preview()

    def takePicture(self, imageName):
        pdb.set_trace()
        self.camera.start_preview(fullscreen=False, window=(100,20,640,480))
        self._warmUp(3)

        fullImagePath = self.__locationToSaveTo + imageName
        self.camera.capture(fullImagePath)

        print "File is saved to:" + fullImagePath

        self.camera.stop_preview()

        return fullImagePath