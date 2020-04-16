import api_feed as api 
import cv2

x=3
c=0
while(c<=x):
    api.feed("p19.jpg",ver=False,sizeX=500,sizeY=300,maxColor=80,clear=True,extraY=12,minArea=850.0)
    c += 1
#api.ver_img(221)
#api.borrarUltimo()
api.plotCont()
#imagen = api.clearImg("p15.jpg",porcent=25,extraY=20)
