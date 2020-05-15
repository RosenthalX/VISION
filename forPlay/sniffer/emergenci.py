import requests


recurso = requests.request("GET","https://ls911-41eb4.firebaseio.com/ls911.json")

datos = list(recurso.json())
indexes = dict(recurso.json())

for dato in datos[:]:
    print(indexes[dato])