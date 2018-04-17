from PIL import Image
from time import sleep
from ParkingSpace import ParkingSpace
import numpy as np
import cv2
import sys
import time
import json
import pdb

class ParkingDetection:
    def __init__(self):
        self.meanValue = 0
        self.parkingSpaceList = self._generateParkingSpaceList()
    
    def _generateParkingSpaceList(self):
        dictionaryList = []
        returnList = []
        
        # Change the data.json to appropriate file to read
        with open('data.json') as json_data:
            dictionaryList = json.load(json_data)

        for dictionaryObject in dictionaryList:
            parkingSpace = ParkingSpace(dictionaryObject["y1"], dictionaryObject["x1"], dictionaryObject["y2"], dictionaryObject["x2"])
            returnList.append(parkingSpace)
        
        return returnList

    def loadImage(self, imageLocation):
        return cv2.imread(imageLocation, cv2.IMREAD_UNCHANGED)
    
    def getImageDifference(self, image1, image2):
        return image2 - image1
    
    def getAverage(self, x1, x2, y1, y2, image3):
        total = 0
        for i in range(x1, x2):
            for j in range(y1, y2):
                total += image3[i,j]

        average = total / ((x1*x2) + (y1*y2))
        return average

    def _convertImageToGreyscale(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def isParkingSpotTaken(self, imageLocation1, imageLocation2):
       image1 = self.loadImage(imageLocation1)
       image2 = self.loadImage(imageLocation2)
       image3 = self.getImageDifference(image1, image2)
       greyscaledImage = self._convertImageToGreyscale(image3)


       for parkingSpace in self.parkingSpaceList:
           parkingSpace.createRectangleOnImage(image1)
           parkingSpace.createRectangleOnImage(greyscaledImage)

       image1 = cv2.resize(image1, (760, 520))
       cv2.imshow('original', image1)
       x = cv2.resize(greyscaledImage, (760, 520))
       cv2.imshow('subtraction', cv2.resize(x, (760, 520)))


parkingDetection = ParkingDetection()
parkingDetection.isParkingSpotTaken("./parking_lot_images/empty_lot.jpg", "./parking_lot_images/lot_1car.jpg")

cv2.waitKey(0)