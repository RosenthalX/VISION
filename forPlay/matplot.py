import matplotlib.pyplot as plt 
import sys
import numpy as np
import cv2
#ejercisio en https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
#practica en https://practice.geeksforgeeks.org/problems/check-if-two-line-segments-intersect/0
#datos python en https://www.tutorialspoint.com/python/python_xml_processing.htm

if __name__ == '__main__':
    print("Main")
    lista = sys.argv
    print(lista)

    arr = np.array([[2,2],[6,8]],np.uint8)
    arr2 = np.array([[5,3],[1,8]],np.uint8)
    print(arr)
    arr=arr.transpose()
    print(arr)

    arr2 = arr2.transpose()

    plt.plot(arr[0],arr[1],c="b")
    plt.plot(arr2[0],arr2[1],c="g")
    plt.yticks(np.arange(0,10))
    plt.xticks(np.arange(0,10))



import pyautogui
while True:
    captura = pyautogui.screenshot()
    captura =(np.array(captura))
    cvcaptura = cv2.resize(captura,(500,600))
    cv2.imshow("Imagen",cvcaptura)
    key = cv2.waitKey(int(3000)) & 0xFF
    if(key==ord("q")):
        break
    cv2.destroyAllWindows()
