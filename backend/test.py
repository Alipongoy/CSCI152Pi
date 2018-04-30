import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("./parking_lot_images/lot_2carsright.jpg")
edges1 = cv2.Canny(img,150,300, 3)
edges2 = cv2.Canny(img,100,300, 3)

# plt.subplot(121),plt.imshow(img)
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(121),plt.imshow(edges1)
plt.title('Edge Image 1'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges2)
plt.title('Edge Image 2'), plt.xticks([]), plt.yticks([])

edges2 = cv2.resize(edges2, (720, 540))
cv2.imshow("greyscaledImage", edges2)

plt.show()
