from PIL import Image
import numpy as np
import cv2
import sys
import time

#To hold the coordidate points (x,y)
points = [[0 for x in range(2)]for y in range (3)]
point = []
#print "Starting from the first parking space, enter 3 points top-left, bottom-left, and top-right"
#point = raw_input("Points: ")
#pointsNeeded = ['first', 'second', 'third', 'fourth']
'''
for i in range(4):
	print "Enter x-coordinate of the", pointsNeeded[i], "point"
	point = raw_input("x-coordinate: ")
        print "Enter y-coordinate of the", pointsNeeded[i], "point"
	point = raw_input("y-coordinate: ")
'''
'''
for i in range(len(point)):
	for j in range(len(point[i])):
		print("a")
		print(i, j)
		print(point[i][j])
		#time.sleep(1)
'''
img1=cv2.imread("/home/pi/Documents/imgA.jpg")
#cropped the image
#croppedImg = img1[100:450, 200:700]
#cv2.imshow('cropped',croppedImg)
#resize image so it doesn't take up the whole screen
img1 = cv2.resize(img1, (760, 520))
'''creates a rectangle from given coordinates
top-left and bottom-right points'''
point = [58,193,88,215]
for i in range(3):
	#cv2.rectangle(img1,(58,193),(88,215),(255,0,0),2)
	cv2.rectangle(img1,(58,193),(88,215),(255,0,0),2)
#convert image to grayscale
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
'''another way of creating rectangle but this way uses
multiple lines given four coordinate points'''
#[[59,193],[33,215],[87,215],[113,193]] -- 54w 22l
'''
pts = np.array([[59,193],[33,215],[87,215],[113,193]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img1,[pts],True,(255,0,0))
'''
cv2.imshow('image',img1)
cv2.waitKey(0)
 

