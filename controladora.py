import api_feed as api 
import cv2
import numpy as np

x=3
c=0
while(c<=x):
    #api.feed("p16.jpg",clearColor=True,powerClear=120.0,ver=False,sizeX=500,sizeY=300,maxColor=80,clear=True,extraY=0,minArea=850.0)
    c += 1
#api.ver_img(221)
#api.borrarUltimo()
#api.plotCont()
#imagen = api.clearImg("p15.jpg",porcent=25,extraY=20)


api.feed_predict()
placa = api.predict("p17.jpg",dobleMorph=True,minArea=100.0,clear=True,maxColor=59,clearColor=True,powerClear=150.0)
print(placa)


#imagen =  cv2.imread("./imagen/p28.jpg")
#imagen = cv2.resize(imagen,(300,200))
#api.clear(imagen,errorT=65.0)
