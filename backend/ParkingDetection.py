from ParkingSpace import ParkingSpace
from PIL import Image
import time
import numpy as np
import cv2
import json
import pdb

class ParkingDetection:
    def __init__(self):
        """ This is a constructor function for a ParkingDetection class.

        Attributes
        ----------
        self.sensitivityLightValue : int
            This determines what the bottom threshold value should be when reading in a value
        self.dataToRead : str
            This is a string leading to the JSON object
        self.parkingSpaceList = [ParkingSpace objects]
            A list of parking space objects
        """
        self.sensitivityLightValue = 30
        self.dataToRead = 'data.json'
        self.parkingSpaceList = self._generateParkingSpaceList()

    def _generateParkingSpaceList(self):
        """ Generates a list containing parkingSpace objects

        Returns
        -------
        [ParkingSpace]
            Returns a list of ParkingSpace objects.
        """
        dictionaryList = []
        returnList = []

        # Change the data.json to appropriate file to read
        with open(self.dataToRead) as json_data:
            dictionaryList = json.load(json_data)

        for dictionaryObject in dictionaryList:
            parkingSpace = ParkingSpace(dictionaryObject)
            returnList.append(parkingSpace)

        return returnList

    def loadImage(self, imageLocation):
        """ Loads an image.

        Parameters
        ----------
        imageLocation: str
            A string location of the image to load.

        Returns
        -------
        numpy.ndarray
            Returns an image.
        """
        return cv2.imread(imageLocation, cv2.IMREAD_UNCHANGED)

    def getImageDifference(self, image1, image2):
        """ Returns the subtraction of image2 and image1. Not being used.

        Parameters
        ----------
        image1: numpy.ndarray
            A string location of the image to load.
        image2: numpy.ndarray
            A string location of the image to load.

        Returns
        -------
        numpy.ndarray
            Returns an image.
        """
        return image2 - image1

    def _convertImageToGreyscale(self, img):
        """ converts an image to a greyscaled image.

        Parameters
        ----------
        img: numpy.ndarray
            This is the original image you want to convert to greyscale.

        Returns
        -------
        numpy.ndarray
            Returns a greyscaled version of the image.
        """
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def _resizeImage(self, img):
        """ Resizes an image to 720x540

        Parameters
        ----------
        img: numpy.nparray
            This is the image you want to rescale

        Returns
        -------
        numpy.nparray
            Returns the scaled version of the image.
        """
        return cv2.resize(img, (720, 540))

    def checkParking(self, imageLocation1):
        """ Checks if parking spot is available, and rewrites the data.json if a parking spot is available.

        How It Works!
        -------------
        Step 1: Loads an image
        Step 2: Loads a seperate image mask and resizes it
        Step 3: Creates an edgeImage using the Canny function and resizes it
        Step 4: For each parkingSpace, a mask is drawn in the image mask.
        Step 5: The average light value for each parking spot is determined by the mask.
        Step 6: Sets the property of parkingSpace.isOpen based on if the average light value is brighter than the threshold value

        Parameters
        ----------
        imageLocation1: str
            A string of the image location.

        """
        image1 = self.loadImage(imageLocation1)
        image1Resized = self._resizeImage(image1)

        imageMask = self.loadImage(imageLocation1)
        imageMask = self._resizeImage(imageMask)

        edgeImage = cv2.Canny(image1, 0, 400, 3)
        edgeImage = self._resizeImage(edgeImage)

        sampleEdge = cv2.Canny(image1, 0, 400, 3)
        sampleEdge = self._resizeImage(sampleEdge)

        # These are the thresholds of what white values to capture
        lowerWhite = np.array([80, 80, 80])
        higherWhite = np.array([255, 255, 255])

        for parkingSpace in self.parkingSpaceList:
            # This draws the polygons on the image.
            parkingSpace.createPolygonOnImage(edgeImage)
            parkingSpace.createPolygonOnImage(image1)
            # This draws the yellow mask to the images.
            parkingSpace.drawMaskOnImage(imageMask)

        with open(self.dataToRead, 'r+') as jsonFile:
            data = json.load(jsonFile)
            # This is the main logic for finding if a parking spot has changed
            for parkingSpace in self.parkingSpaceList:
                parkingSpace.setParkingTaken(edgeImage, self.sensitivityLightValue, imageMask)
                data = parkingSpace.updateData(data)
            jsonFile.seek(0)  # rewind
            json.dump(data, jsonFile, indent=4)
            jsonFile.truncate()

        # This displays the igmage. Remove in production.
        cv2.imshow("image1Resized", image1Resized)
        cv2.imshow("imageMask", imageMask)
        cv2.imshow("edgeImage", edgeImage)
        cv2.imshow("sampleEdge", sampleEdge)

x = ParkingDetection()
x.checkParking("parking_lot_images/mainImage.jpg")
cv2.waitKey(0)
