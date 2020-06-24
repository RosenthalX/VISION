from fbchat import Client
from fbchat.models import *
from fbchat import Message 
from fbchat import ThreadType


client = Client('diegomartinez1417@gmail.com','Spawndslyer13')

if client.isLoggedIn():
    print("Logins sucess")
    client.send(Message(text='Prueba'),thread_id="dlego.martinez",thread_type=ThreadType.USER)
    client.logout()
else:
    print("Failed to log in")
