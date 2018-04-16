from PIL import Image
from time import sleep
import numpy as np
import cv2
import sys
import time
import pdb
import json
'''
pts = np.array([[205,710],[50,750],[265,750],[420,675]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img3_2,[pts],True,(255,0,0),3)
'''

'''**********************************
*PARKING SPACE RECTANGLE COORDINATES*
**********************************'''
#Layout: Each element in list is a sparking space
#	 Each element in a sublist is [x1,y1,x2,y2] => (x1,y1) (x2,y2) [1170]
rectangle_lot = [[475,675,610,750],[705,660,910,750],[1000,675,1170,750]]

with open('data.json') as json_data:
	x = json.load(json_data)

# pdb.set_trace()
'''The Parking Spaces (not to be confused with the above
   (the above is just to draw the rectangular boxes for visuals)'''

#parking_lot = [[500,500,500,900],[400,300,600,400],[1000,400,1020,500]]
#Parking lot spaces as shown in image from left to right
parking_lot = [[680,480,745,605],[665,710,745,905],[680,1005,745,1165]]


#Load images
img1 =cv2.imread("parking_lot_images/empty_lot.jpg", cv2.IMREAD_UNCHANGED)
img2 = cv2.imread("parking_lot_images/lot_1car.jpg", cv2.IMREAD_UNCHANGED)

#Save image to display the parking lot with rectangles
img3_2 = img2
#Save to compare when there are two cars instead of one
img3_3 = img2


#Perform image subtraction
img3 = img2-img1

#convert image to grayscale in order to calculate avg pixel value
img3 = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)

#create rectangles for each parking space in image that has no grayscale
for space in rectangle_lot:
        cv2.rectangle(img3_2,(space[0],space[1]),(space[2],space[3]),(255,0,0),3)

#find average pixel value (works only with grayscale)
#Holds total sum of all pixels
total = [0,0,0]
total_index = 0
at=1
#Add up all pixels in parking space
for space in parking_lot:
	for i in range(space[0],space[2]):
        	for j in range(space[1],space[3]):
                	total[total_index] += img3[i,j]
                        # use this to map out parking lot: img3[i,j] = 1000
	total_index = total_index + 1

#mean = total / (width * height)

#Holds each average for each parking space
average = [0,0,0]

#Calculate average pixel value for each space in parking lot
for i in range(len(total)):
	average[i] = total[i] / ( (rectangle_lot[i][2]) * (rectangle_lot[i][3]) )


#Determine if a spot is taken or not
for i in range(len(average)):
	print "This is the average: " + str(average[i])
	if average[i] ==  0:
        	print (i, " is not taken")
	else:
		print (i , " is taken")


img3_2 = cv2.resize(img3_2, (760, 520))
cv2.imshow('original',img3_2)

#Draw rectangles for 1st subtracted image, resize, and display it
for space in rectangle_lot:
        cv2.rectangle(img3,(space[0],space[1]),(space[2],space[3]),(255,0,0),3)
img3 = cv2.resize(img3, (760, 520))
cv2.imshow('subtraction1',img3)

'''
#2nd subtraction
img4 =cv2.imread("/home/pi/Documents/lot_2carsright.jpg", cv2.IMREAD_UNCHANGED)
img5 = img4-img3_3
img6 = cv2.cvtColor(img6,cv2.COLOR_BGR2GRAY)

width = 875
height = 750

total = 0
for i in range(725,width):
        for j in range(675,height):
                total = img3[i,j]

mean = total / (width * height)

if mean ==  0:
        print "taken"
else:
	print "empty"

cv2.rectangle(img6,(715,660),(900,750),(255,0,0),3)
img6 = cv2.resize(img6, (760, 520))
#cv2.rectangle(img6,(373,293),(500,393),(255,0,0),2)
cv2.imshow('image',img6)
'''
cv2.waitKey(0)
