import cv2
import numpy as np

img = cv2.imread("panda.jpg")
gris= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

b,g,r = cv2.split(img)
blue = (img * (1,0,0)).astype(np.uint8)
green = (img * (0,1,0)).astype(np.uint8)
red = (img * (0,0,1)).astype(np.uint8)
azurojo = (img * (1,0.1,0.45)).astype(np.uint8)
azure = cv2.merge((b,g,r,gris))

cv2.imshow("blue",blue)
cv2.imshow("green",green)
cv2.imshow("red",red)
cv2.imshow("Axur",azure)

cv2.imwrite("azure.png",azure)
cv2.waitKey(0)