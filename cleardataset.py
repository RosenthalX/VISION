import cv2
import numpy as np

try:
    dataset = list(np.load("dataset_placas.npy"))
    labels = list(np.load("labels_placas.npy"))
except Exception as msn:
    dataset = []
    labels = []
    print("Excepcion al abrir el archivo")

for i,data in enumerate(dataset):
    print(data.shape)
    data2 = data.copy()
    data2 = cv2.GaussianBlur(data2,(3,3),3)
    _,data2 = cv2.threshold(data2,127,255,cv2.THRESH_BINARY)
    data2 = cv2.bitwise_not(data2)
    dataset[i] = data2
    
#for i,data in enumerate(dataset):
    #data = cv2.resize(data,(500,500))
    #cv2.imshow("Letra "+str(labels[i]),data)
    #key = cv2.waitKey(0) & 0xFF
    #cv2.destroyAllWindows()
    #if key == ord('q'):
     #   break

np.save("dataset_placas_thresh",dataset)
print("Longitud de datos: "+str(len(dataset))+" -- Longitud de labels: "+str(len(labels)))