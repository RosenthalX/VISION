import numpy as np 
import pandas as pd 

df = pd.read_csv("200423COVID19MEXICO.csv",encoding = "ISO-8859-1")
df2 = pd.DataFrame()

print(df.keys())

df2[["1","2","3"]]=df[["SEXO","RESULTADO","MIGRANTE"]]

print(df2.keys())
print(df2.head(5))