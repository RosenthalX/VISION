import requests
import argparse

parse  = argparse.ArgumentParser(description="Sistema de post y testeo")
parse.add_argument("-u","--url",help="Especificar url de conexión post.")
parse.add_argument("-i","--input",help="Especificar input ejemplo nombre&JuanChacas")
parse.add_argument("-f","--file",help="Indica el archivo a subir")

parse = parse.parse_args()


def main():
    if parse.file:
        pass
    else:
        print("Argumento -f necesario.")

if __name__ == "__main__":
    main()