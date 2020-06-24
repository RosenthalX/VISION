#import sys

#print(sys.byteorder)
#print(268 & 0xC0)

dato = bytes(b'h')

for b in dato:
    for i in range(8):
        print((b>>i)&1)
        