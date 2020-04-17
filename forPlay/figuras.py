import cv2

imagen = cv2.imread("./../imagen/figuras.jpg")

def getVertices(c):
    arc = cv2.arcLength(c,True)
    poli = cv2.approxPolyDP(c,0.01*arc,True)
    return poli

gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gris,200,255,cv2.THRESH_BINARY)
conts,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(conts))
for cont in conts:
    #print("Vertices de esta figura"+str(getVertices(cont)))
    img = imagen.copy()
    img = cv2.drawContours(img,[cont],0,(0,255,122),cv2.LINE_AA)
    for minicont in getVertices(cont):
        img = cv2.circle(img,(minicont[0,0],minicont[0,1]),5,(255,0,0),-1)

    cv2.imshow("Imagen",img)
    cv2.waitKey(0)



cv2.imshow("figura",imagen)
cv2.imshow("thresh",thresh)
cv2.waitKey(0)