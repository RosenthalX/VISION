import socket
import struct

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('',53))

s2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

PL = 1024

def desenpacketar(datagrama,apuntador):
    datos = []
    while True:
        unpack = struct.unpack_from('!B',datagrama,apuntador)
        length = unpack[0]
        apuntador += 1


        if length == 0:
            return datos,apuntador

        datos.append(*struct.unpack_from("!%ds" % length, datagram, offset=apuntador))
        apuntador += length



while True:
    datagram , addr = s.recvfrom(PL)
    print(addr)
    ofs = 12
    ST = struct.unpack_from('!6H',datagram,offset=0)
    print("ID({}),MISC({}),PREGUNTA({}),RESPONDE({}),AUTORIZA({}),ADDICIONAL({})".format(ST[0],ST[1],ST[2],ST[3],ST[4],ST[5]))
    print(ST[1] & 0x8000)
    datos,ofs = desenpacketar(datagram,ofs)
    print(datos)
    print("Offset despues de tratamiento: {}".format(str(ofs)))
    print("Ejecutando datagrama de addr "+str(addr[0]))
    s2.sendto(datagram,("8.8.8.8",53))
    print("Datagrama enviado a google")
    datagram2,addr2 = s2.recvfrom(PL)
    print("Resolucion correcta...")
    s2.sendto(datagram2,(addr[0],53))
    print("Resolucion entregada\n\n\n")