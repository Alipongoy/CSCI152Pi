from Camera import Camera
from time import sleep
from ParkingDetection import ParkingDetection
import cv2

def main():
    try:
        camera = Camera()
        parkingDetection = ParkingDetection()

        camera.openCamera()
        nameOfImage = "mainImage.jpg"

        while True:

            fullImagePath = camera.takePicture(nameOfImage)

            parkingDetection.checkParking(fullImagePath)
            cv2.waitKey(0)

    except KeyboardInterrupt:
        print "Program will now quit."
        return

main()
