from PIL import Image
from time import sleep
import numpy as np
import cv2
import sys
import time

class ParkingDetection:
    def __init__(self):
        def self.meanValue = 0       

    def loadImage(self, imageLocation):
        return cv2.imread(imageLocation, cv2.IMREAD_UNCHANGED)
    
    def getImageDifference(self, image1, image2)
        return image2 - image1
    
    def getAverage(self, x1, x2, y1, y2, image3)
        total = 0

        for i in range(x1, x2):
            for j in range(y1, y2):
                total += image3[i,j]

        average = total / ((x1*x2) + (y1*y2))
        return average

   def isParkingSpotTaken(imageLocation1, imageLocation2):
       image1 = self.loadImage(imageLocation1)
       image2 = self.loadImage(imageLocation2)
       image3 = getImageDifference(image1, image2)