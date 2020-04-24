import urllib.request as url_
import zipfile
import pandas as pd
from datetime import datetime,timedelta,date
import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(18,6.4))
def start():
    zipFile = "http://187.191.75.115/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip"
    
    usock = url_.urlopen(zipFile)
    usock = usock.read()

    output = open("covit.zip",'wb')
    output.write(usock)
    output.close()

    zip_file = zipfile.ZipFile("covit.zip")

    obj_name=zip_file.namelist()[0]
    obj = zip_file.read(obj_name)

    output = open(obj_name,'wb')
    output.write(obj)
    output.close()

isStart = False

if(isStart):
    start()
else:
    zip_file = zipfile.ZipFile("covit.zip")
    obj_name=zip_file.namelist()[0]
    obj = zip_file.read(obj_name)

df = pd.read_csv(obj_name,encoding = "ISO-8859-1")
#print(df.keys())}

plt.title("Covid Victoria")

df["FECHA_INGRESO"] = pd.to_datetime(df["FECHA_INGRESO"])
print("Antes de filtrado tamaulipas:"+str(len(df)))


df = df.loc[df["ENTIDAD_NAC"]==28]
print("Filtrado tamaulipas:"+str(len(df)))


df = df.loc[df["MUNICIPIO_RES"]==41]
print("Filtrado victoria:"+str(len(df)))

X = np.arange(date(2020,3,27),date(2020,4,24),timedelta(days=1)).astype(date)
#print(len(df["FECHA_INGRESO"].loc[df["FECHA_INGRESO"] == "2020-04-18"]))
PLOTTERS = []

#positivos 1 , no positivos 2 , pendientes 3
x = np.arange(0,19,1)
y = []
maxi=0

for i,date in enumerate(X):
    casualidades = len(df["FECHA_INGRESO"].loc[df["FECHA_INGRESO"] == date])
    
    #print('index {} para fecha {} casos estimados {}'.format(i,date,casualidades))
    y.append(casualidades)
#PLOTTERS.append(plt.plot(X,y,c="b",label="Casos")[0])
plt.bar(X,y)
#plt.scatter(X,y,c="r",label="Interes",marker="*")


print("Total de casos: "+str(len(df)))

df2 = df.loc[df["RESULTADO"]==1]
y=[]
for i,date in enumerate(X):
    casualidades = len(df2["FECHA_INGRESO"].loc[df2["FECHA_INGRESO"] == date])
    #print('index {} para fecha {} casos estimados {}'.format(i,date,casualidades))
    y.append(casualidades)
PLOTTERS.append(plt.plot(X,y,c="r",label="Positivos")[0])
print("Positivos: "+str(len(df2)))
#plt.scatter(X,y,c="black",label="Positivos",marker="x")


df2 = df.loc[df["RESULTADO"]==2]
y=[]
for i,date in enumerate(X):
    casualidades = len(df2["FECHA_INGRESO"].loc[df2["FECHA_INGRESO"] == date])
    #print('index {} para fecha {} casos estimados {}'.format(i,date,casualidades))
    y.append(casualidades)
PLOTTERS.append(plt.plot(X,y,c="g",label="Negativos")[0])
print("Negativos: "+str(len(df2)))
#plt.scatter(X,y,c="black",label="Negativos",marker="x")

df2 = df.loc[df["RESULTADO"]==3]
y=[]
for i,date in enumerate(X):
    casualidades = len(df2["FECHA_INGRESO"].loc[df2["FECHA_INGRESO"] == date])
    #print('index {} para fecha {} casos estimados {}'.format(i,date,casualidades))
    y.append(casualidades)
print("Pendientes: "+str(len(df2)))
PLOTTERS.append(plt.plot(X,y,c="black",label="Pendientes")[0])
#plt.scatter(X,y,c="black",label="Positivos",marker="x")


plt.xticks(X,rotation="vertical")
plt.yticks(np.arange(0,37,1))
plt.xlabel("Array")
plt.legend(PLOTTERS,["TOTAL","POS","NEG","PEND"])
plt.grid()

plt.show()