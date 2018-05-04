import unittest
from ParkingDetection import ParkingDetection
import json
import cv2

#python -m unittest test_ParkingDetection.py
park = ParkingDetection()
class TestParkingDetection(unittest.TestCase):
    '''Black-box test cases start'''
    # check if parking spaces were properly extracted based on original file
    # check space based on that we can assumen the rest objects are correct
    def test_GenerateParkingSpaceList(self):
        print "Created parking space list"
        
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
            index = index + 1
    
    # test if image did load
    def test_loadImage(self):
        print "Loaded image"
        
        image = park.loadImage('parking_lot_images/empty_lot.jpg')
        self.assertGreater(len(image), 50)
    
    # test image subtraction: first set of pixels are black to save time
    def test_getImageDifference(self):
        print "Subtracted images"

        testImage1 = cv2.imread('./parking_lot_images/empty_lot.jpg', cv2.IMREAD_UNCHANGED)
        testImage2 = cv2.imread('./parking_lot_images/empty_lot.jpg', cv2.IMREAD_UNCHANGED)
        imageDiff = park.getImageDifference(testImage1, testImage2)
        
        for pix in imageDiff[0][0]:
            self.assertEqual(pix, 0)

    # formula used by OpenCV: 0.299*R+0.587*G+0.114*B
    def test_ConvertImageToGreyscales(self):
        print "Converted image to greyscale"

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
        
        image = park.loadImage('parking_lot_images/empty_lot.jpg')
        resizedImg = park._resizeImage(image)
        self.assertEqual(len(resizedImg), 540)
    
        '''Black-box test cases end'''


if __name__ == '__main__':
    unittest.main()

