import requests as R
import argparse 

parser = argparse.ArgumentParser(description="Detector de cabeceras")
parser.add_argument("-t","--target",help="Objetivo")
parser = parser.parse_args()



def main():
    if parser.target:
        print("Conectando a :"+parser.target+"\n")
        try:
            url = R.get(parser.target)
            cabecera = dict(url.headers)
            for x in cabecera:
                print("{}:{}".format(x,cabecera[x]))
        except Exception as e:
            print("No es posible la conexión."+str(e))
    else:
        print("No hay objetivo.")


if __name__ == '__main__':
    main()