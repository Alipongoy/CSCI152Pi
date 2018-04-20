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
        self._sensitivity = 0.50
        # This determines how sensitive the parking spot detections are
        self.sensitivityLightValue = int(round(self._sensitivity * 255))
    
    def _generateParkingSpaceList(self):
        dictionaryList = []
        returnList = []
        
        # Change the data.json to appropriate file to read
        with open('data.json') as json_data:
            dictionaryList = json.load(json_data)

        for dictionaryObject in dictionaryList:
            parkingSpace = ParkingSpace(dictionaryObject["x1"], dictionaryObject["y1"], dictionaryObject["x2"], dictionaryObject["y2"], dictionaryObject["lot"], dictionaryObject["row"], dictionaryObject["spot"])
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
        imageCopy = self.loadImage(imageLocation1)
        image2 = self.loadImage(imageLocation2)
        image3 = self.getImageDifference(image1, image2)
        greyscaledImage = self._convertImageToGreyscale(image3)

        for parkingSpace in self.parkingSpaceList:
            parkingSpace.createRectangleOnImage(image1)
            parkingSpace.createRectangleOnImage(image2)
            parkingSpace.createRectangleOnImage(greyscaledImage)

        # Should call is parkingSpot taken in every ParkingSpace element

        x = cv2.resize(image1, (720, 540))
        y = cv2.resize(image2, (720, 540))
        z = cv2.resize(greyscaledImage, (720, 540))
        # Top left, top right, bottom right, bottom left
        pts = np.array([[252,336], [355,338], [317,393], [152,393]], np.int32)
        # I have no idea what is actually happening here
        pts = pts.reshape((-1,1,2))
        # Attempts to fill image of polygon into x
        # for xCoord in range(152, 355):
        #     newY = int(round((xCoord * slope) + 338))
        #     for yCoord in range(338, newY):
        #         x[yCoord, xCoord] = (255, 255, 0)
        # slope = (float(338-393)/float(355-252))
        # print "This is the slope: " + str(slope)
        # total = 0
        # for xCoord in range(152 + 10, 252 - 10):
        #     total += 1
        #     newY = int(round((total * slope))) + 393
        #     for yCoord in range(392 + 10, newY - 10, -1):
        #         x[yCoord, xCoord] = (0, 255, 0)

        # for xCoord in range(252 + 10, 317 - 10):
        #     for yCoord in range(336 + 10, 393 - 10):
        #         x[yCoord, xCoord] = (0, 255, 0)

        # total = 0
        # difference = 335 - 317
        # slope = (float(338-393)/float(355-317))
        # yIntercept = int(393 - (slope * 317))
        # for xCoord in range(317 + 10, 355 - 10):
        #     newY = int(round((xCoord * slope))) + yIntercept
        #     for yCoord in range(338 + 10, newY - 10, 1):
        #         # pdb.set_trace()
        #         x[yCoord, xCoord] = (0, 255, 0)
        
        cv2.polylines(image1,[pts],True,(0,255,255))
        cv2.fillPoly(image1, [pts], (0, 255, 255))
        cv2.imshow("yee", x)


        for parkingSpace in self.parkingSpaceList:
            parkingSpace.drawMaskOnImage(imageCopy)
            parkingSpace.isSingleSpotTaken(greyscaledImage, self.sensitivityLightValue, imageCopy)

        z = cv2.resize(greyscaledImage, (720, 540))
        cv2.imshow('greyscaledImage', z)
        imageCopy = cv2.resize(imageCopy, (720, 540))
        cv2.imshow('imageCopy', imageCopy)

parkingDetection = ParkingDetection()
parkingDetection.isParkingSpotTaken("./parking_lot_images/empty_lot.jpg", "./parking_lot_images/lot_2carsright.jpg")

cv2.waitKey(0)