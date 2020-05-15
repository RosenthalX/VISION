from flask import Flask
import sys
import requests
recurso = requests.request("GET","https://ls911-41eb4.firebaseio.com/ls911.json")
datos = list(recurso.json())
indexes = dict(recurso.json())





app = Flask(__name__)

@app.route("/hola/<username>&<userpassword>")
def start(username,userpassword):
    return "Bienvenido "+username+" Tu contraseña es "+ str(userpassword)

@app.route("/ls911/check=<numero>")
def numeros(numero):
    return exist_number(numero)

def get_all():
    datacenter = []
    for dato in datos[:]:
        datacenter.append(dato)
    return datacenter

def exist_number(number):
    for dato in datos[:]:
        if number in indexes[dato]:
            return "true"
    return "false"
app.run()