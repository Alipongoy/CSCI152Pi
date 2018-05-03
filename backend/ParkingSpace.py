import numpy as np
import cv2
import pdb

class ParkingSpace:
    def __init__(self, parkingDictionary):
        """ This is a constructor function for a ParkingSpace class.

        Parameters
        ----------
        parkingDictionary : dict
            This is a dictionary which should contain the following keys:
            {
                topLeft: [x_coordinate, y_coordinate],
                topRight: [x_coordinate, y_coordinate],
                bottomLeft: [x_coordinate, y_coordinate],
                bottomRight: [x_coordinate, y_coordinate],
                lot: int,
                genID: int,
                space: int,
                isOpen: bool
            }
        
        Attributes
        ----------
        self.topLeft : [int xCoordinate, int yCoordinate]
        self.topRight : [int xCoordinate, int yCoordinate]
        self.bottomLeft : [int xCoordinate, int yCoordinate]
        self.bottomRight : [int xCoordinate, int yCoordinate]
        self.lot : int
        self.genID : int
        self.space : int
        self.isOpen : bool
        """

        pointCoordinateKeysToCheck = ["topLeft", "topRight", "bottomRight", "bottomLeft"]
        coordinateKeysToCheck = ["x1", "x2", "y1", "y2"]
        # This checks if the data.json follows an 8 point system
        is8Point = all(key in parkingDictionary for key in pointCoordinateKeysToCheck)
        isCoordinates = all(key in parkingDictionary for key in coordinateKeysToCheck)
        # If it follows an 8 point coordinate system, then the coordinates get set regularly
        if (is8Point):
            self.topLeft = parkingDictionary["topLeft"]
            self.topRight = parkingDictionary["topRight"]
            self.bottomRight = parkingDictionary["bottomRight"]
            self.bottomLeft = parkingDictionary["bottomLeft"]
        # If not, then the coordinates get set programatically
        elif (isCoordinates):
            self.topLeft = (parkingDictionary["x1"], parkingDictionary["y1"])
            self.topRight = (parkingDictionary["x2"], parkingDictionary["y1"])
            self.bottomRight = (parkingDictionary["x2"], parkingDictionary["y2"])
            self.bottomLeft = (parkingDictionary["x1"], parkingDictionary["y2"])
        else:
            print "Error, data is not submitted properly."

        self.lot = parkingDictionary["lot"]
        self.genID = parkingDictionary["genID"]
        self.space = parkingDictionary["space"]

        self.width = abs(self.topLeft[0] - self.topRight[0])
        self.height = abs(self.topLeft[1] - self.bottomLeft[1])

        self.ptsArray = np.array([[self.topLeft[0],self.topLeft[1]], [self.topRight[0],self.topRight[1]], [self.bottomRight[0],self.bottomRight[1]], [self.bottomLeft[0],self.bottomLeft[1]]], np.int32)
        self.ptsArray = self.ptsArray.reshape((-1,1,2))

        self.isOpen = parkingDictionary["isOpen"]
    
    def createPolygonOnImage(self, imageToDrawTo, color=None):
        """ Draws a polygon outline to image.

        Parameters
        ----------

        imageToDrawTo : numpy.ndarray
            This is the image you want to draw the polygon into

        color: int (optional)
            Can specify a color with this parameter 
        """

        if color is None:
            color = 255
        cv2.polylines(imageToDrawTo,[self.ptsArray],True, (color, 0, 0), 3)
    
    def drawMaskOnImage(self, imageToDrawTo):
        """ Draws a mask, which is composed of an outline and a filling, to imageToDrawTo

        The color mask being drawn is yellow. DO NOT change the values

        Parameters
        ----------
        imageToDrawTo : numpy.ndarray
            This is the image you want to draw the mask into
        """
        # Do not change last argument!!!
        cv2.polylines(imageToDrawTo, [self.ptsArray], True, (0, 255, 255))
        cv2.fillPoly(imageToDrawTo, [self.ptsArray], (0, 255, 255))

    def fillPolygonOnImage(self, imageToDrawTo, valueToDraw):
        """ Fills a polygon shape into the imageToDrawTo.

        This function is used when drawing the average light values onto a Canny Image.

        Parameters
        ----------

        imageToDrawTo : numpy.ndarray
            This is the image you want to draw the polygon into

        color: value
            Can specify a color with this parameter 
        """
        cv2.polylines(imageToDrawTo,[self.ptsArray], True, valueToDraw)
        cv2.fillPoly(imageToDrawTo, [self.ptsArray], valueToDraw)
    
    def getPolygonAverage(self, imageToGetAverageOf, imageMask):
        """ Gets the average light value of a polygon.

        Parameters
        ----------
        
        imageToGetAverageOf: numpy.ndarray
            This is the image which you want to find the average values of 
        imageMask: numpy.ndarray
            This is an imageMask. This should have been passed to self.drawMaskOnImage() first, so the mask can be created. 

        Returns
        -------
        int
            Returns the average light value of an imageMask over teh imageToGetAverageOf.
        """
        # Refactor this to 8 Point system
        totalLightValue = 0
        yellowPixel = 0
        highestX = max(self.topLeft[0], self.bottomLeft[0], self.bottomRight[0], self.topRight[0])
        lowestX = min(self.topLeft[0], self.bottomLeft[0], self.bottomRight[0], self.topRight[0])

        highestY = max(self.topLeft[1], self.bottomLeft[1], self.bottomRight[1], self.topRight[1])
        lowestY = min(self.topLeft[1], self.bottomLeft[1], self.bottomRight[1], self.topRight[1])

        for x in range(lowestX, highestX):
            for y in range(lowestY, highestY):
                if imageMask[y,x][1] == 255 and imageMask[y,x][2] == 255:
                    totalLightValue += imageToGetAverageOf[y,x]
                    yellowPixel += 1
        
        return totalLightValue / yellowPixel
    
    def updateData(self,data):
        """ Updates the the property 'isOpen' to either True or False based on conditions.

        This function is used to write back data into the data.json file.

        Parameters
        ----------
        
        data: dict
            This is a dictionary that should contain a single dictionary from the data.json file

        Returns
        -------
        data: dict
            The function will return the same dictionary, only now with 'isOpen' changed.
        """
        for singleData in data:
            if (singleData["lot"] == self.lot and singleData["genID"] == self.genID and singleData["space"] == self.space):
                # This toggles the isSpotTaken
                if self.isOpen == True:
                    singleData["isOpen"] = True
                else:
                    singleData["isOpen"] = False
                index = data.index(singleData)
                data[index] = singleData
        return data

    def setParkingTaken(self, edgeImage, sensitivityLightValue, imageMask):
        """ Sets the property self.isOpen to either True or False depending if parking spot is taken or not

        Parameters
        ----------
        
        edgeImage: numpy.ndarray
            This is an image that should be an Canny edge image.
        sensitivityLightValue: int
            Represents the lowest threshold for an image to contain a parking spot or not.
            For example, if sensitivityLightValue = 50, then any average higher than 50 will be considered as a taken parking spot.
        imageMask: numpy.ndarray
            This is an image which should be a mask Image.
            
        """
        polygonAverage = self.getPolygonAverage(edgeImage, imageMask)
        print "This is the polygonAverage: ", polygonAverage
        self.fillPolygonOnImage(edgeImage, polygonAverage)

        if (sensitivityLightValue < polygonAverage):
            print "This is lot: ", str(self.lot)
            print "This is space: ", str(self.space)
            print "This spot is taken."
            self.isOpen = True
        else:
            print "This spot isn't taken."
            self.isOpen = False
