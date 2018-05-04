import unittest
from ParkingSpace import ParkingSpace
import json

class TestParkingSpace(unittest.TestCase):
    '''Black-box test cases start'''
    # return the whole parking list and updates isOpen fto alse
    def test_updateData(self):
        print "Updating isOpen values in for spaces in parking space list to False"
        testList  = []
        with open('dummyData.json') as inputFile:
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
            index = index + 1

if __name__ == '__main__':
    unittest.main()
