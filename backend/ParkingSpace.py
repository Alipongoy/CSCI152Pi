from PIL import Image
from time import sleep
import numpy as np
import cv2
import sys
import time

class ParkingSpace:
    def __init__(self, y1, x1, y2, x2);
        self.y1 = y1
        self.x1 = x1
        self.y2 = y2
        self.x2 = x2
        self.isSpotTaken = False

    def _loadImage(self, imageLocation):
        return cv2.imread(imageLocation, cv2.IMREAD_UNCHANGED)

    def _getImageDifference(self, image1, image2)
        return image2 - image1

    def _convertImageToGreyscale(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

   def isSingleSpotTaken(self, imageLocation1, imageLocation2):
       image1 = self._loadImage(imageLocation1)
       image2 = self._loadImage(imageLocation2)
       image3 = self._getImageDifference(image1, image2)
       imageGreyscale = self._convertImageToGreyscale(image3)
