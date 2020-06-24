import socket
import struct

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(('127.0.0.1',44567))
named = ""
cont = 3
print("UDP Server conectado.")

while(cont < 0):
    data,addr = s.recv(1024)
    print(struct.calcsize(data))
    cont -= 1