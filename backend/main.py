from Camera import Camera
from time import sleep 
from ParkingDetection import ParkingDetection
import cv2

def main():
    try: 
        while True:
            camera = Camera()
            parkingDetection = ParkingDetection()

            nameOfImage = "mainImage.jpg"
            fullImagePath = camera.takePicture(nameOfImage)

            parkingDetection.checkParking(fullImagePath)
            cv2.waitKey(0)

    except KeyboardInterrupt:
        print "Program will now quit."
        return