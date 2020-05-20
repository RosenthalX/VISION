import cv2
import numpy as np

#Array de identidades
identidades = ["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12","A13","A14","A15","A16","A17","A18","A19","A20","B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","B12","B13","B14","B15","B16","B17","B18","B19","B20"
"C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","C16","C17","C18","C19","C20","D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","D11","D12","D13","D14","D15","D16","D17","D18","D19","D20"]
cont_id = 0

#Carga y tamaño de la imagen
img = cv2.imread("./simplepark.jpg")
img = cv2.resize(img,(800,600))

#Creacion de imagenes a diferentes formatos
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#tresholding y gaussian
kernel = (3,3)
img_gauss = cv2.GaussianBlur(img_gray,kernel,3)
_,img_thresh = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)

#Encuentro de contornos y esquinas
conts,_ = cv2.findContours(img_thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(len(conts))
for cont in conts[:]:
    epsilon = 0.03 * cv2.arcLength(cont,True)
    esquinas = cv2.approxPolyDP(cont,epsilon,True)
    #print(len(esquinas))
    M = cv2.moments(cont)
    cX = int(M["m10"]/(M["m00"]+0.0001))
    cY = int(M["m01"]/(M["m00"]+0.0001))
    if(len(esquinas)==4 and cv2.contourArea(cont) > 500):
        cv2.drawContours(img,[cont],-1,(0,255,0),1)
        cv2.putText(img,identidades[cont_id]+": "+str(cv2.contourArea(cont)),(cX-10,cY-0),cv2.FONT_HERSHEY_SIMPLEX,0.6,(50,12,255),2)
        cont_id += 1
        print(identidades[cont_id]+": "+str(cv2.contourArea(cont)))
        

        eA = esquinas[0][0]
        eB = esquinas[1][0]
        eC = esquinas[2][0]
        eD = esquinas[3][0]
        cols,rows,ch = img.shape

        img = cv2.circle(img,(eA[0],eA[1]),3,(0,0,255),cv2.FILLED)
        img = cv2.circle(img,(eB[0],eB[1]),3,(0,255,0),cv2.FILLED)
        img = cv2.circle(img,(eC[0],eC[1]),3,(255,0,0),cv2.FILLED)
        img = cv2.circle(img,(eD[0],eD[1]),3,(255,255,0),cv2.FILLED)

        pts1 = np.float32([[eA[0],eA[1]],[eD[0],eD[1]],[eC[0],eC[1]],[eB[0],eB[1]]])
        pts2 = np.float32([[0,0],[cols,0],[0,rows],[rows,cols]])

        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        output = cv2.warpPerspective(img,matrix,(rows,cols))



        x,y,w,h = cv2.boundingRect(cont)
        img_copy = img.copy()
        cv2.imshow("Crop",output)
        cv2.waitKey(0)


img_final = img




cv2.imshow("Imagen",img_final)
cv2.waitKey(0)