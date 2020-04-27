import socket
import time
import subprocess
import sys

host = "localhost"
port = 40415

try:
    s=socket.socket()
    s.connect((host,port))
    while True:
        datos = s.recv(2048)
        if(datos[:4].decode("utf-8")=="quit"):
            print("Se cerro la session remota.")
            break
        else:
            strin = datos.decode("utf-8")
            print("Nuevos datos llegaron: "+strin)
            strin="Datos nuevos "+strin
            time.sleep(1.2)
            s.send(strin.encode(encoding="utf-8"))
            
    s.close()


except socket.error as err:
    print("Error al iniciar el socket "+str(err))


