import os 
import os.path as path 
os.chdir("C://")
cont = 0
for root, dirs, files in os.walk("."):
    if "jpg" in files:
        print("{}: {}".format(str(cont),files))
        cont += 1
