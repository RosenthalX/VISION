import subprocess
import os
import requests


while True:
    cmd = input("(turtle) {}> ".format(os.getcwd()))
    if cmd == "quit":
        break

    if cmd[:2] == "cd":
        if len(cmd) > 3:
            if os.path.exists(os.path.join(os.getcwd(),cmd[3:])):
                os.chdir(cmd[3:])
            else:
                print("Path no existe, verifique la ruta con ls o dir.")
        else:
            os.chdir("..")
    
    elif cmd[:5] == "isDir":
        if len(cmd) > 7:
            if os.path.exists(os.path.join(os.getcwd(),cmd[6:])):
                if os.path.isdir(os.path.join(os.getcwd(),cmd[6:])):
                    print("True")
                else:
                    print("False")
            else:
                print("Nombre de archivo inexistente")
        else:
            print("Debe especificar un archivo.")

    else:
        result = subprocess.Popen(cmd,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        aprint  = result.stdout.read()+result.stderr.read()
        aprint = str(aprint,encoding="utf-8",errors="ignore")
        print(aprint)
    
    
print("CMD Finish")
    
