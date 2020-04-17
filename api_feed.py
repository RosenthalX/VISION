import cv2
import numpy as np
import collections
import matplotlib.pyplot as plt


def feed(imagen,powerClear=100.0,ver=False,maxColor=40,kernel=2,sizeX=330,sizeY=180,morph=True,clear=False,extraY=10,clearColor=False,minArea=800.0):
    img = cv2.imread("./imagen/"+imagen)
    if(clear):
        img = clearImg(imagen,porcent=25,extraY=extraY)

    if(clearColor):
        img = clearMat(img,errorT=powerClear)
        
    img = cv2.resize(img,(sizeX,sizeY))
    black = np.zeros((sizeY,sizeX,3),np.uint8)
    blue = np.ones((sizeY,sizeX,3),np.uint8)
    blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
    white = blue.copy()
    img2 = img.copy()
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    kernel = np.ones((kernel,kernel),np.uint8)
    save = True

    try:
        dataset = list(np.load("dataset_placas.npy"))
        labels = list(np.load("labels_placas.npy"))
    except:
        dataset = []
        labels = []



    KEYS = [ord('A'),ord('B'),ord('C'),ord('D'),ord('E'),ord('F'),ord('G'),ord('H'),ord('I'),ord('J'),
    ord('K'),ord('L'),ord('M'),ord('N'),ord('O'),ord('P'),ord('Q'),ord('R'),ord('S'),ord('T'),ord('U'),
    ord('V'),ord('W'),ord('X'),ord('Y'),ord('Z'),ord('1'),ord('2'),ord('3'),ord('4'),ord('5'),ord('6'),
    ord('7'),ord('8'),ord('9'),ord('0')]




    blue[:,:,0]=250
    blue[:,:,1]=100
    blue[:,:,2]=100

    white[:,:,0]=0
    white[:,:,1]=100
    white[:,:,2]=100    
    #CONFIGURACION DE NEGROS.
    mask = cv2.inRange(img_gray,np.array([0]),np.array([maxColor]))
    #mask = cv2.inRange(img_hsv,np.array([0,0,0]),np.array([360,100,maxColor]))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, (3,3))

    if(morph):
        erosion = cv2.erode(mask,kernel,iterations=1)
        dilation = cv2.dilate(erosion,kernel,iterations=1)
        dilation_not = cv2.bitwise_not(dilation)
    else:
        print("skip morph")
        erosion = mask.copy()
        dilation = mask.copy()
        dilation_not = cv2.bitwise_not(dilation)



    bitwising = cv2.bitwise_or(img2,blue,mask=dilation)


    contours,_ = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    def getX(cont):
        x,_,_,_ = cv2.boundingRect(cont)
        return x

    contours.sort(key=getX,reverse=False)

    for cont in contours:
        x,y,w,h = cv2.boundingRect(cont)
        img = cv2.drawContours(img,[cont],0,(0,255,133),thickness=3,lineType=cv2.LINE_AA)
        crop = img2[y:y+h,x:x+w]
        crop = cv2.resize(crop,(500,500))
        area = cv2.contourArea(cont)
        if(area > minArea):
            cv2.imshow("Crop area:"+str(area),crop)
            key = (cv2.waitKey(0) & 0xFF)
            if(key in KEYS):
                print("Se guardo al registro. ",str(chr(key)))
                peke = cv2.resize(crop,(32,32))
                peke = cv2.cvtColor(peke,cv2.COLOR_BGR2GRAY)
                print(peke.shape)
                dataset.append(peke)
                labels.append(str(chr(key)))
                #cv2.imshow("resizada",peke)
                #cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif(key == ord('q')):
                save = False
                break
            else:
                cv2.destroyAllWindows()
                print("Se ignoro el registro.")
    cv2.destroyAllWindows()
    print("ESPACIOS EN BLANCO")
    print(" ")
    print(labels)
    print("La longitus de labels es de ",str(len(labels)))
    print("Las imagenes guardadas son :",str(len(dataset))," y el shape es "+str(np.array(dataset).shape))

    #for index,label in enumerate(labels):
        #cv2.imshow("Imagen de "+str(label),cv2.resize(dataset[index],(300,300)))

    if save:
        np.save("labels_placas",np.array(labels))
        np.save("dataset_placas",np.array(dataset))
        print("Nuevo Dataset Guardado")
    else:
        print("Guardado de dataset abortado shape actual "+str(np.array(labels).shape))

    if(ver):
        cv2.imshow("Placa 1", img)
        #cv2.imshow("Gris", img2)
        cv2.imshow("mask",mask)
        cv2.imshow("erosion",erosion)
        cv2.imshow("dilation",dilation)
        #cv2.imshow("bitwise",bitwising)
        cv2.imshow("white",white)
        cv2.waitKey(0)

def ver_img(numero=20):
    try:
        dataset = list(np.load("dataset_placas.npy"))
        labels = list(np.load("labels_placas.npy"))
        cv2.imshow("LETRA "+str(labels[numero]),cv2.resize(dataset[numero],(600,600)))
        cv2.waitKey(0)
    except:
        print("No hay base de datos.")

def plotCont(plotter=False):
    labels = np.load("labels_placas.npy")
    valores = collections.Counter(labels)
    plt.bar(valores.keys(),valores.values())
    plt.yticks(np.arange(0,30))
    plt.ylabel("Registros por caracter")
    plt.xlabel("Caracteres disponibles")
    plt.title("Almacenamiento actual letras")
    plt.legend(loc="upper right")
    plt.show()


def clearImg(imagen,sizeX=330,sizeY=180,porcent=10,thresh=False,white=False,extraX=0,extraY=0,minArea=800):
    
    img = cv2.imread("./imagen/"+imagen)
    img = cv2.resize(img,(sizeX,sizeY))
    
    def change(i):
        pass
    
    
    img2 = img.copy()
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    porcent = int(100/porcent)
    print(img2.shape)
    print("porcent: "+str(porcent))
    #mask = cv2.inRange(img,min,max)

    x10 = int(sizeX/porcent)
    y10 = int(sizeY/porcent)


    zero = np.zeros((img2.shape),np.uint8)
    filling = 255

    zero[0:y10,0:sizeX] = [255]
    zero[sizeY-y10:sizeY,0:sizeX] = [255]


    zero_mask = zero.copy()
    zero = cv2.bitwise_not(zero)

    crop = img[y10:sizeY-y10-extraY,0:sizeX]
    zero = cv2.bitwise_and(img,img,mask=zero)
    
    print(zero.shape)
    return crop
        














def borrarUltimo():

    dataset = list(np.load("dataset_placas.npy"))
    labels = list(np.load("labels_placas.npy"))

    dataset = dataset[:-1]
    labels = labels[:-1]

    print("La longitus de labels es de ",str(len(labels)))
    print("Las imagenes guardadas son :",str(len(dataset))," y el shape es "+str(np.array(dataset).shape))
       
    np.save("labels_placas",np.array(labels))
    np.save("dataset_placas",np.array(dataset))

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score





model = SVC(kernel="linear",C=50.0,gamma="auto",probability=True,tol=0.002)


def feed_predict():
    dataset = np.load("dataset_placas.npy")
    labels = np.load("labels_placas.npy")
    
    dataset = dataset.reshape(dataset.shape[0],1024)

    xtrain,xtest,ytrain,ytest = train_test_split(dataset,labels,train_size=0.2,random_state=30,stratify=labels)

    model.fit(xtrain,ytrain)
    xtest_predict = model.predict(xtest)
    print("La presicion el model es de: "+str(accuracy_score(ytest,xtest_predict)))
    










def predict(imagen,powerClear=100.0,ver=False,dobleMorph=False,maxColor=40,kernel=2,sizeX=330,sizeY=180,morph=True,clear=False,extraY=10,minArea=800.0,meanArea=73,clearColor=False):

    img = cv2.imread("./imagen/"+imagen)
    if(clear):
        img = clearImg(imagen,porcent=25,extraY=extraY)
        
    if(clearColor):
        img = clearMat(img,errorT=powerClear)
    img = cv2.resize(img,(sizeX,sizeY))
    black = np.zeros((sizeY,sizeX,3),np.uint8)
    blue = np.ones((sizeY,sizeX,3),np.uint8)
    blue = cv2.cvtColor(blue,cv2.COLOR_BGR2HSV)
    white = blue.copy()
    img2 = img.copy()
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    kernel = np.ones((kernel,kernel),np.uint8)
    save = True

    blue[:,:,0]=250
    blue[:,:,1]=100
    blue[:,:,2]=100

    white[:,:,0]=0
    white[:,:,1]=100
    white[:,:,2]=100    

    #CONFIGURACION DE NEGROS.
    mask = cv2.inRange(img_gray,np.array([0]),np.array([maxColor]))
    #mask = cv2.inRange(img_hsv,np.array([0,0,0]),np.array([360,100,maxColor]))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, (6,6))


    #erosion = cv2.erode(mask,kernel,iterations=1)
    #dilation = cv2.dilate(erosion,kernel,iterations=1)
    #dilation_not = cv2.bitwise_not(dilation)

    #print("skip morph")
    erosion = mask.copy()
    dilation = mask.copy()
    dilation_not = cv2.bitwise_not(dilation)



    bitwising = cv2.bitwise_or(img2,blue,mask=dilation)
    if(dobleMorph):
        dilation = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, (6,6))
    cv2.imshow("dilation",dilation)
    cv2.waitKey(0)
    contours,_ = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    def getX(cont):
        x,_,_,_ = cv2.boundingRect(cont)
        return x

    contours.sort(key=getX,reverse=False)

    predicciones=[]

    for cont in contours:
        x,y,w,h = cv2.boundingRect(cont)
        crop = img2[y:y+h,x:x+w]
        crop = cv2.resize(crop,(500,500))
        area = cv2.contourArea(cont)
        if(area > minArea):
            peke = cv2.resize(crop,(32,32))
            peke = cv2.cvtColor(peke,cv2.COLOR_BGR2GRAY)
            xpeke = peke.reshape(1,1024)
            predic = model.predict(xpeke)
            print("Para "+list(predic)[0]+" se tiene un mean de "+str(np.mean(xpeke)))
            predicciones.append({"prediccion":list(predic)[0],"Area":area,"Mean":np.mean(xpeke)})
            #cv2.imshow("LETRA: "+str(list(predic)[0]),crop)
            #cv2.waitKey(0)

    def prediccionesA(predic):
        return predic["Mean"]

    prediccion2 = predicciones.copy()
    predicciones.sort(key=prediccionesA) 

    remover = 0
    #while(len(prediccion2)>7):
     #   print("len de predicciones 2"+str(len(prediccion2)))
      #  for dato in prediccion2:
       #     if dato == predicciones[remover]:
        #        prediccion2.remove(dato)
         #       remover += 1

    for dato in prediccion2:
        if dato["Mean"]<meanArea:
            prediccion2.remove(dato) 
        

    arr = ""
    for letra in prediccion2:
        arr += str(letra["prediccion"])
    return arr




def clearMat(img,errorT=25.0):
    x,y,z = img.shape
    for i in range(0,x):
        for j in range(0,y):
            b,g,r = img[i,j]
            arr = np.array([b,g,r])
            error = abs((arr-arr.mean())).sum()
            if(error > errorT):
                img[i,j] = [255,255,255]

    return img