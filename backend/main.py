from Camera import Camera
from time import sleep 
from ParkingDetection import ParkingDetection

def main():
    try: 
        while True:
            camera = Camera()
            parkingDetection = ParkingDetection()

            nameOfImage = "mainImage.jpg"
            fullImagePath = camera.takePicture(nameOfImage)

            parkingDetection.checkParking(fullImagePath)

    except KeyboardInterrupt:
        print "Keyboard was pressed."
        return