import cv2
import numpy as np
import collections
import matplotlib.pyplot as plt


def feed(imagen,ver=False,maxColor=40,kernel=2,sizeX=330,sizeY=180,morph=True):
    img = cv2.imread("./imagen/"+imagen)
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
        if(area > 500.0):
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