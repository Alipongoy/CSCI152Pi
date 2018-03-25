from PIL import Image
from picamera import PiCamera
from time import sleep
import cv2
import sys

#Testing camera
camera = PiCamera()

#Tests preview gives time to setup
camera.start_preview(fullscreen=False, window=(100,20,640,480))
for i in range(5):
	print(i)
	sleep(1)
camera.stop_preview()

#Take first image
camera.start_preview(fullscreen=False, window=(100,20,640,480))
for i in range(3):
	print(i)
	sleep(1)
print "about to take imageA"
sleep(5)
camera.capture("/home/pi/Documents/imgA.jpg")
print "took imageA"
camera.stop_preview()

#Take second image
camera.start_preview(fullscreen=False, window=(100,20,640,480))
for i in range(3):
	print(i)
	sleep(1)
print "about to take imageB"
sleep(5)
camera.capture("/home/pi/Documents/imgB.jpg")
print "took imageB"
camera.stop_preview()

#Load images
imgA = cv2.imread("/home/pi/Documents/imgA.jpg", cv2.IMREAD_UNCHANGED)
imgB = cv2.imread("/home/pi/Documents/imgB.jpg", cv2.IMREAD_UNCHANGED)

#Image subtraction shows differences between the two
imgC = imgA-imgB

imgC = cv2.resize(imgC, (760, 520))
cv2.imshow('image', imgC)
cv2.waitKey(0)

