from PIL import Image
import numpy as np
import cv2
import sys
img1=cv2.imread("/home/pi/Documents/imgA.jpg")
#cropped the image
#croppedImg = img1[100:450, 200:700]
#cv2.imshow('cropped',croppedImg)
#resize image so it doesn't take up the whole screen
img1 = cv2.resize(img1, (760, 520))
'''creates a rectangle from given coordinates
top-left and bottom-right points'''
#cv2.rectangle(img1,(52,188),(100,220),(255,0,0),3)
'''another way of creating rectangle but this way uses
multiple lines given four coordinate points'''
pts = np.array([[52,188],[25,215],[88,215],[115,188]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img1,[pts],True,(255,0,0))
cv2.imshow('image',img1)
cv2.waitKey(0)

