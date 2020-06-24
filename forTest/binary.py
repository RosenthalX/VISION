import struct

dataset = struct.pack('5i',10,20,30,40,50)
print(dataset)
print(len(dataset))
offsetx = 0 
for _ in range(int(len(dataset)/4)):
    print(struct.unpack_from('i',dataset,offset=offsetx))
    offsetx += 4