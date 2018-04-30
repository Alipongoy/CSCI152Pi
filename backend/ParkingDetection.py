from ParkingSpace import ParkingSpace
from PIL import Image
import numpy as np
import cv2
import json
import pdb

class ParkingDetection:
    def __init__(self):
        # self._sensitivity = 0.50
        # This determines how sensitive the parking spot detections are
        self.sensitivityLightValue = 50
        self.dataToRead = 'data.json'
        self.parkingSpaceList = self._generateParkingSpaceList()
    
    def _generateParkingSpaceList(self):
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
        return cv2.imread(imageLocation, cv2.IMREAD_UNCHANGED)
    
    def getImageDifference(self, image1, image2):
        return image2 - image1
    
    def _convertImageToGreyscale(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    def _resizeImage(self, img):
        return cv2.resize(img, (720, 540))

    def checkParking(self, imageLocation1):
        image1 = self.loadImage(imageLocation1)
        image1Resized = self._resizeImage(image1)

        imageTest = self.loadImage("./parking_lot_images/empty_lot.jpg")
        imageTest = self._resizeImage(imageTest)

        imageMask = self.loadImage(imageLocation1)
        imageMask = self._resizeImage(imageMask)
	
	#For while loop indent till bottom at sleep(3)
	'''while True:
		#camera = PiCamera()
		camera.start_preview(fullscreen=False, window=(100,20,640,480))
		sleep(2)
        	camera.capture(imageLocation2)
		#camera.close()
        	camera.stop_preview()'''

        edgeImage = cv2.Canny(image1, 0, 400, 3)
        edgeImage = self._resizeImage(edgeImage)

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

        # This displays the image 
        cv2.imshow("edgeImage", edgeImage)

	#time stamp
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        print "\n"
	#sleep(3)

