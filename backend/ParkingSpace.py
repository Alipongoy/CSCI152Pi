from time import sleep
import cv2
import sys
import time

class ParkingSpace:
    def __init__(self, x1, y1, x2, y2):
        self.y1 = y1
        self.x1 = x1
        self.y2 = y2
        self.x2 = x2
        self.isSpotTaken = False

    def createRectangleOnImage(self, imageToDrawTo):
        cv2.rectangle(imageToDrawTo,(self.y1,self.x1),(self.y2,self.x2),(255,0,0),3)

    def isSingleSpotTaken(self, greyedImage):
       # TODO:
       # 1) Feed in only greyscaled image
       pass
