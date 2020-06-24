import socket
import struct


s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
mensaje = "Enviando mensaje"
structured = struct.pack("!b",len(mensaje))
offset = 1
for i in mensaje:
    print(structured+struct.pack('!s',"m".encode("utf-8")))

print(structured)
print(struct.unpack('!b',structured))

print(len(structured))
#s.sendto(structured,("127.0.0.1",44567))
print("UDP WOrks")
