import cv2
import numpy as np 


black = np.ones([600,500,3],np.uint8)
white = (black * (2**8-1)).astype(np.uint8)
blue = (black * (255,0,0)).astype(np.uint8)



cv2.imshow("blue",blue)
cv2.imshow("black",black)
cv2.imshow("white",white)
cv2.waitKey(0)


