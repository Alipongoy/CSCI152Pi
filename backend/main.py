# Classes created
from Camera import Camera
from ParkingDetection import ParkingDetection
# Other libraries needed
from time import sleep
import cv2
import urllib2, urllib
import json
import pdb


def pushToBackEnd(pathToPushTo):
    with open('../backend/data.json') as json_data:
        mydata = json.load(json_data)

    req = urllib2.Request(pathToPushTo)
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(mydata))
    print response.read().decode("iso-8859-1")
    print "Successfully pushedToBackEnd!"


def main():
    try:
        camera = Camera()
        parkingDetection = ParkingDetection()

        camera.openCamera()
        nameOfImage = "mainImage.jpg"

        while True:
            fullImagePath = camera.takePicture(nameOfImage)
            parkingDetection.checkParking(fullImagePath)
            pushToBackEnd("http://ab-kc.tk/parking/push.php")
            # This ensures that its not taking pictures every cycle
            time.sleep(30)
            # Remove bottom code in production
            # cv2.waitKey(0)

    except KeyboardInterrupt:
        print "Program will now quit."
        return

main()