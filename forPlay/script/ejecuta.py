import pandas as pd
import numpy as np
import datetime

x = str(datetime.datetime.now()).split(" ")[0]

principal = pd.read_excel("extrac.xls", encoding='iso-8859-1')
df2 = pd.DataFrame()

#,"APELLIDO","NOMBRE","NOTAS","CIERRE","LATITUD","LONGITUD","SEXO","EDAD"]]=df[["SUBCENTRO","FOLIO","SUBCENTRO","RELACIONADO","ID_TIPO INCIDENTE","DESC INCIDENTE","SUBCENTRO","SUBTIPO","CORPORACION","UNIDAD","FECHA","HORARECEPCIONSEGUNDOS","HORADESPACHO","TIEMPOARRIBOUNIDAD","HORACIERRE","TIEMPORECIBODESPACHO","SUBCENTRO","TIEMPODESPACHOLLEGADA","TIEMPOLLEGADACIERRE","FECHACIERRE","OPERADOR","DESPACHADOR","MUNICIPIO","SUBCENTRO","DESCOLONIA","DIRECCION","TELEFONO","APPATERNO","NOMBREUSUARIO","NOTASUSUARIOS","MOTIVOCIERRECORPORACIONDESC","LATITUD","LONGITUD","SEXO","SUBCENTRO"]]

def zeros(index):
    return ' ';

df2[["CALLE"]] = principal[["SUBCENTRO"]]
df2[["FOLIO"]] = principal[["FOLIO"]]
df2[["DIVIDIDO"]] = principal[["STATUS"]]
df2.loc[:,"DIVIDIDO"] = ""
df2[["UNIDO/LIGA"]] = principal[["RELACIONADO"]]
df2[["TIPO"]] = principal[["ID_TIPO INCIDENTE"]]
df2[["INCIDENTE"]] = principal[["DESC INCIDENTE"]]
df2[["CODIGO SUBTIPO"]] = principal[["STATUS"]]
df2.loc[:,"CODIGO SUBTIPO"] = ""
df2[["SUBTIPO DE INCIDENTE"]] = principal[["SUBTIPO"]]
df2[["CORPORACION"]] = principal[["CORPORACION"]]
df2[["UNIDAD"]] = principal[["UNIDAD"]]
df2[["FECHA"]] = principal[["FECHA"]]
df2[["RECIBIDO"]] = principal[["HORARECEPCIONSEGUNDOS"]]
df2[["HORA DESPACHO"]] = principal[["HORADESPACHO"]]
df2[["ARRIBO"]] = principal[["TIEMPOARRIBOUNIDAD"]]
df2[["CERRADO"]] = principal[["HORACIERRE"]]
df2[["RCBD/DESP"]] = principal[["TIEMPORECIBODESPACHO"]]
df2[["RCBD/ARR"]] = principal[["STATUS"]]
df2.loc[:,"RCBD/ARR"] = ""
df2[["DES/ARR"]] = principal[["TIEMPODESPACHOLLEGADA"]]
df2[["ARR/CER"]] = principal[["TIEMPOLLEGADACIERRE"]]
df2[["FECHA DE CIERRE"]] = principal[["FECHACIERRE"]]
df2[["OPERADOR"]] = principal[["OPERADOR"]]
df2[["DESPACHO"]] = principal[["DESPACHADOR"]]
df2[["MUNICIPIO"]] = principal[["MUNICIPIO"]]
df2[["CODIGO COLONIA"]] = principal[["STATUS"]]
df2.loc[:,"CODIGO COLONIA"] = ""
df2[["COLONIA"]] = principal[["DESCOLONIA"]]
df2[["DIRECCION"]] = principal[["DIRECCION"]]
df2[["TELEFONO"]] = principal[["TELEFONO"]]
df2[["APELLIDO"]] = principal[["APPATERNO"]]
df2[["NOMBRE"]] = principal[["NOMBREUSUARIO"]]
df2[["NOTAS"]] = principal[["NOTASUSUARIOS"]]
df2[["CIERRE"]] = principal[["MOTIVOCIERRECORPORACIONDESC"]]
df2[["LATITUD"]] = principal[["LATITUD"]]
df2[["LONGITUD"]] = principal[["LONGITUD"]]
df2[["SEXO"]] = principal[["SEXO"]]
df2[["EDAD"]] = principal[["STATUS"]]
df2.loc[:,"EDAD"] = ""

print(df2)

#df2.to_csv("extract_"+str(x)+".csv")

