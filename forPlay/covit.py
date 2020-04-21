import urllib.request as url_
import zipfile
import pandas as pd
from datetime import datetime,timedelta,date
import numpy as np

zipFile = "http://187.191.75.115/gobmx/salud/datos_abiertos/datos_abiertos_covid19.zip"

#usock = url_.urlopen(zipFile)
#usock = usock.read()

#output = open("covit.zip",'wb')
#output.write(usock)
#output.close()

zip_file = zipfile.ZipFile("covit.zip")

obj_name=zip_file.namelist()[0]
#obj = zip_file.read(obj_name)

#output = open(obj_name,'wb')
#output.write(obj)
#output.close()

df = pd.read_csv(obj_name)
#print(df.keys())

df["FECHA_INGRESO"] = pd.to_datetime(df["FECHA_INGRESO"])

X = np.arange(date(2020,4,1),date(2020,4,20),timedelta(days=1)).astype(date)

print(len(df["FECHA_INGRESO"].loc[df["FECHA_INGRESO"] == "2020-04-18"]))
print(X[0].date.value)