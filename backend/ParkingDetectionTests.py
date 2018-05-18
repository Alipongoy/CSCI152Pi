import unittest
from ParkingDetection import ParkingDetection
from ParkingSpace import ParkingSpace
import json
import cv2

#python -m coverage report --omit="*/site-packages*"
#python -m unittest test_ParkingDetection.py
class TestParkingDetection(unittest.TestCase):
    '''Black-box test cases start'''
    
    '''check if parking all spaces were properly extracted compare
        against original test data spaces'''
    def test_GenerateParkingSpaceList(self):
        print "Created parking space list"
        
        park = ParkingDetection()

        testList = []
        with open('data.json') as inputFile:
            testData = json.load(inputFile)
        
        testList = park._generateParkingSpaceList
        index = 0
        for item in testData:
            self.assertEqual(item['space'], testList()[index].space)
            self.assertEqual(item['lot'], testList()[index].lot)
            self.assertEqual(item['genID'], testList()[index].genID)
            self.assertEqual(item['isOpen'], testList()[index].isOpen)
            self.assertEqual(item['topLeft'],testList()[index].topLeft)
            self.assertEqual(item['topRight'],testList()[index].topRight)
            self.assertEqual(item['bottomRight'],testList()[index].bottomRight)
            self.assertEqual(item['bottomLeft'],testList()[index].bottomLeft)
            index += 1
    
    # test if image did load by checking length of image is no 0
    def test_loadImage(self):
        print "Loaded image"
        
        park = ParkingDetection()
        
        image = park.loadImage('parking_lot_images/empty_lot.jpg')
        self.assertGreater(len(image), 50)
    
    # test image subtraction: first set of pixels are black to save time
    def test_getImageDifference(self):
        print "Subtracted images"
        
        park = ParkingDetection()

        testImage1 = cv2.imread('./parking_lot_images/empty_lot.jpg', cv2.IMREAD_UNCHANGED)
        testImage2 = cv2.imread('./parking_lot_images/empty_lot.jpg', cv2.IMREAD_UNCHANGED)
        imageDiff = park.getImageDifference(testImage1, testImage2)
        
        for pix in imageDiff[0][0]:
            self.assertEqual(pix, 0)

    # formula used by OpenCV: 0.299*R+0.587*G+0.114*B
    # Check flattened array and compare it against formula
    def test_ConvertImageToGreyscales(self):
        print "Converted image to greyscale"
        
        park = ParkingDetection()

        colorImg = cv2.imread('parking_lot_images/empty_lot.jpg', cv2.IMREAD_UNCHANGED)
        greyImg = park._convertImageToGreyscale(colorImg)
        index = 0
        for i in range(len(colorImg[0])):
            testColor =  colorImg[0][i]
            colorResult = (0.299*testColor[2]) + (0.587*testColor[1]) + (0.114*testColor[0])
            colorResult = int(round(colorResult))
            self.assertEqual(greyImg[0][i], colorResult)

    # test if resize works check agains parameters specified cv2 resize function (default 720, 540)
    def test_resizeImage(self):
        print "Resized image"
        
        park = ParkingDetection()
        
        image = park.loadImage('parking_lot_images/empty_lot.jpg')
        resizedImg = park._resizeImage(image)
        self.assertEqual(len(resizedImg), 540)
        
    #def test_checkParking(self):
        #print "Check parking"
        #park = ParkingDetection()

    '''Black-box test cases end'''


'''Tests for ParkingSpace module'''
class TestParkingSpace(unittest.TestCase):
    '''Black-box test cases start'''
    # return the whole parking list and updates isOpen to false
    def test_updateData(self):
        print "Updating isOpen values for all spaces in parking space list to False"
        testList  = []
        with open('test_dummyData.json') as inputFile:
            testData = json.load(inputFile)
        
        for item in testData:
            parkingSpace = ParkingSpace(item)
            testList.append(parkingSpace)
        
        updatedTestData = testList[0].updateData(testData)
        index = 0
        for item in testData:
            self.assertEqual(item['space'], updatedTestData[index]['space'])
            self.assertEqual(item['lot'], updatedTestData[index]['lot'])
            self.assertEqual(item['genID'], updatedTestData[index]['genID'])
            self.assertEqual(item['topLeft'],updatedTestData[index]['topLeft'])
            self.assertEqual(item['topRight'],updatedTestData[index]['topRight'])
            self.assertEqual(item['bottomRight'],updatedTestData[index]['bottomRight'])
            self.assertEqual(item['bottomLeft'],updatedTestData[index]['bottomLeft'])
            self.assertEqual(item['isOpen'], False)
            index += 1

    # Check if correct average for polygon average is returned
    def test_getPolygonAverage(self):
        print "Get Polygon Average"
        park = ParkingDetection()
            
        image1 = park.loadImage('parking_lot_images/lot_1car.jpg')
        image1Resized = park._resizeImage(image1)
        
        imageMask = park.loadImage('parking_lot_images/lot_1car.jpg')
        imageMask = park._resizeImage(imageMask)
        
        edgeImage = cv2.Canny(image1, 0, 400, 3)
        edgeImage = park._resizeImage(edgeImage)
        
        with open('test_dummyData.json') as inputFile:
            testData = json.load(inputFile)
                
        space = ParkingSpace(testData[0])
        space.createPolygonOnImage(edgeImage)
        polyAv = space.getPolygonAverage(edgeImage, imageMask)
        print "PolyAve = ",polyAv
        self.assertEqual(polyAv,0)

    # White-box
    '''Pass lightsensitivy as 50 and in first if statement space.isOpen value should be set to false since it is not taken'''
    def test_setParkingTaken(self):
        park = ParkingDetection()

        image1 = park.loadImage('parking_lot_images/lot_1car.jpg')
        image1Resized = park._resizeImage(image1)
    
        imageMask = park.loadImage('parking_lot_images/lot_1car.jpg')
        imageMask = park._resizeImage(imageMask)
        
        edgeImage = cv2.Canny(image1, 0, 400, 3)
        edgeImage = park._resizeImage(edgeImage)
        
        with open('test_dummyData.json') as inputFile:
            testData = json.load(inputFile)

        space = ParkingSpace(testData[0])
        space.setParkingTaken(edgeImage,50,imageMask)
        self.assertEqual(space1.isOpen, False)


if __name__ == '__main__':
    unittest.main()
