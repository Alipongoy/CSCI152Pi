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
            parkingSpace = ParkingSpace(dictionaryObject)
            returnList.append(parkingSpace)
        
        return returnList

    def loadImage(self, imageLocation):
        return cv2.imread(imageLocation, cv2.IMREAD_UNCHANGED)
    
    def getImageDifference(self, image1, image2):
        return image2 - image1
    
    def _convertImageToGreyscale(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    def _resizeImage(self, img):
        return cv2.resize(img, (720, 540))

    def isChangeInParking(self, imageLocation1, imageLocation2):
        image1 = self.loadImage(imageLocation1)
        image1Copy = self._resizeImage(image1)

        imageMask = self.loadImage(imageLocation1)
        imageMask = self._resizeImage(imageMask)

        image2 = self.loadImage(imageLocation2)
        image2Copy = self._resizeImage(image2)
        imageDifference = self.getImageDifference(image1, image2)
        imageDifferenceCopy = self._resizeImage(imageDifference)

        greyscaledImage = self._convertImageToGreyscale(imageDifference)
        greyscaledImage = self._resizeImage(greyscaledImage)

        for parkingSpace in self.parkingSpaceList:
            # This draws the polygons on the image.
            parkingSpace.createPolygonOnImage(greyscaledImage)
            parkingSpace.createPolygonOnImage(image2)
            # This draws the yellow mask to the images.
            parkingSpace.drawMaskOnImage(imageMask)

        with open('data.json', 'r+') as jsonFile:
            data = json.load(jsonFile)
            # This is the main logic for finding if a parking spot has changed
            for parkingSpace in self.parkingSpaceList:
                isChangeInParking = parkingSpace.isChangeInParking(greyscaledImage, self.sensitivityLightValue, imageMask)
                if (isChangeInParking):
                    data = parkingSpace.updateDataAndIsSpotTaken(data)
            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile)
            jsonFile.truncate()

        cv2.imshow("greyscaledImage", greyscaledImage)
        cv2.imshow("imageMask", imageMask)
        cv2.imshow("image2Copy", image2Copy)
        cv2.imshow("image1Copy", image1Copy)
        cv2.imshow("imageDifferenceCopy", imageDifferenceCopy)

parkingDetection = ParkingDetection()
parkingDetection.isChangeInParking("./parking_lot_images/empty_lot.jpg", "./parking_lot_images/lot_2carsright.jpg")

cv2.waitKey(0)