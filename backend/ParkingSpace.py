from time import sleep
import cv2
import sys
import time
import pdb

class ParkingSpace:
    def __init__(self, x1, y1, x2, y2):
        self.y1 = y1
        self.x1 = x1
        self.y2 = y2
        self.x2 = x2

        self.width = abs(self.x2 - self.x1)
        self.height = abs(self.y2 - self.y1)

        self.isSpotTaken = False

    def createRectangleOnImage(self, imageToDrawTo, color=None):
        if color is None:
            255
        cv2.rectangle(imageToDrawTo,(self.x1,self.y1),(self.x2,self.y2),(color,0,0),3)
    
    def fillRectangleOnImage(self, imageToDrawTo, valueToDraw):
        for x in range(self.x1, self.x2):
            for y in range(self.y1, self.y2):
                imageToDrawTo[y,x] = valueToDraw

    def getAverage(self, imageToGetAverageOf):
        totalLightValue = 0

        # pdb.set_trace()

        for x in range(self.x1, self.x2):
            for y in range(self.y1, self.y2):
                totalLightValue += imageToGetAverageOf[y,x]
        
        return totalLightValue / (self.width * self.height)               

    def isSingleSpotTaken(self, greyedImage, sensitivityLightValue):
       # TODO:
       # 1) Feed in only greyscaled image
        average = self.getAverage(greyedImage)
        print "This is the average: ", average
        self.fillRectangleOnImage(greyedImage, average)

        if (sensitivityLightValue > average):
            print "This spot is taken."
            return True
        else:
            print "This spot is not taken."
            return False
        pass
