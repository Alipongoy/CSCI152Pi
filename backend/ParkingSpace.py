from time import sleep
import numpy as np
import cv2
import sys
import time
import pdb

class ParkingSpace:
    def __init__(self, x1, y1, x2, y2, lot, row, space):
        self.y1 = y1
        self.x1 = x1
        self.y2 = y2
        self.x2 = x2
        self.lot = lot
        self.row = row
        self.space = space

        self.width = abs(self.x2 - self.x1)
        self.height = abs(self.y2 - self.y1)

        self.isSpotTaken = False

    def createRectangleOnImage(self, imageToDrawTo, color=None):
        if color is None:
            color = 255
        cv2.rectangle(imageToDrawTo,(self.x1,self.y1),(self.x2,self.y2),(color,0,0),3)
    
    def fillRectangleOnImage(self, imageToDrawTo, valueToDraw):
        for x in range(self.x1, self.x2):
            for y in range(self.y1, self.y2):
                imageToDrawTo[y,x] = valueToDraw
    
    def drawMaskOnImage(self, imageToDrawTo):
        pts = np.array([[self.x1,self.y1], [self.x2,self.y1], [self.x2,self.y2], [self.x1,self.y2]], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(imageToDrawTo, [pts], True, (0, 255, 255))
        cv2.fillPoly(imageToDrawTo, [pts], (0, 255, 255))

    def fillPolygonOnImage(self, imageToDrawTo, valueToDraw):
        pts = np.array([[self.x1,self.y1], [self.x2,self.y1], [self.x2,self.y2], [self.x1,self.y2]], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(imageToDrawTo,[pts],True, valueToDraw)
        cv2.fillPoly(imageToDrawTo, [pts], valueToDraw)



    def getAverage(self, imageToGetAverageOf):
        totalLightValue = 0

        # pdb.set_trace()

        for x in range(self.x1, self.x2):
            for y in range(self.y1, self.y2):
                totalLightValue += imageToGetAverageOf[y,x]
        
        return totalLightValue / (self.width * self.height)               
    
    def getPolygonAverage(self, imageToGetAverageOf, imageMask):
        totalLightValue = 0
        yellowPixel = 0
        highestX = max(self.x1, self.x2)
        lowestX = min(self.x1, self.x2)

        highestY = max(self.y1, self.y2)
        lowestY = min(self.y1, self.y2)

        for x in range(lowestX, highestX):
            for y in range(lowestY, highestY):
                yellowPixel += 1
                if imageMask[y,x][1] == 255 and imageMask[y,x][2] == 255:
                    totalLightValue += imageToGetAverageOf[y,x]
        
        return totalLightValue / yellowPixel

    def isSingleSpotTaken(self, greyedImage, sensitivityLightValue, x = None):
       # TODO:
       # 1) Feed in only greyscaled image
        average = self.getAverage(greyedImage)
        polygonAverage = self.getPolygonAverage(greyedImage, x)
        print "This is the average: ", average
        print "This is the polygonAverage: ", polygonAverage
        self.fillPolygonOnImage(greyedImage, average)
        # self.fillRectangleOnImage(greyedImage, average)

        if (sensitivityLightValue > average):
            print "This spot is taken."
            return True
        else:
            print "This spot is not taken."
            return False
        pass
