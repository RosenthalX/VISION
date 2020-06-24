print((0x8000))
print((256 & 0x7800)!=0)
print((256 & 0x0400)!=0)
print((256 & 0x200)!=0)
print((256 & 0x100)!=0)
print((256 & 0x80)!=0)
print((256 & 0x70)!=0)
print((256 & 0xF)!=0)
import struct

with open("texto.txt","rb") as filex:
    #print(filex.readline())
    filey = open("file2.txt","wb")

    11000000000000000000

    packs = struct.pack("<h{}s".format(len("Hola Mundos texto")),len("Hola Mundos texto"),b"Hola Mundos texto")
    #print(packs)
    tam_texto = struct.unpack_from('<h',packs,offset=0)
    tam_texto = tam_texto[0]
    print(tam_texto)

    print("\n\n")
    print(struct.unpack_from('<{}s'.format(tam_texto),packs,offset=2))


    filey.close()