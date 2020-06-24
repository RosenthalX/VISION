import struct
import ctypes
import socket

#Pack
generales = b''
datos = struct.pack('!b',22)


print(datos)

generales += datos
generales += datos
generales += datos
print(generales)


data = struct.unpack('!3b',generales)
print(data)