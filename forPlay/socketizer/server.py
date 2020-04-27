import socket
import time
from queue import Queue
import threading
import sys

N_THREADS = 2
QUEUES = [1,2]
q =  Queue()
conection_queue = []
addr_queue = []

#starting params
def start_socket(host1 ,port1):
    try:
        global s 
        global host
        global port

        s = socket.socket()
        host = host1
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



def start_instream():
    del conection_queue[:]
    del addr_queue[:]
    while True:
        try:
            con,addr = s.accept()
            con.setblocking(0)
            conection_queue.append(con)
            addr_queue.append(addr)
            print("Conexión nueva de "+str(addr[0])+":"+str(addr[1]))
        except:
            print("Error en solicitud de conexión: ")



def list_items():
    returner  = ""
    if len(conection_queue) != 0:
        for i,con in enumerate(conection_queue):
            returner += "{} {}:{}\n".format(i,addr_queue[i][0],addr_queue[i][1])
    else:
        returner += "No se encuentran conexiones disponibles."

    print("Conexiones disponibles:\n"+returner)
        

def select_meet(i):
    return conection_queue[i],addr_queue[i]


def start_cmd():
    while True:
        print("shell>",end="")
        cmd = input()
        if(cmd == "list"):
            list_items()
        elif("select " in cmd):
            cmd = cmd.replace("select ","")
            tx,adr = select_meet(int(cmd))
            join_meet(tx,adr)
        elif(cmd == "quit"):
            print("Hasta pronto.\n",end="")
            q.task_done()
            break
            sys.exit(1)
            print("Hasta pronto.\n",end="")
        else:
            print("Comando no valido",end="")

        print("\n",end="")



def Worker():
    while True:
        item  = q.get()
        if item == 1:
            start_instream()
        elif  item ==2:
            start_cmd()
        else:
            q.task_done()



def start_threading():
    for _ in range(N_THREADS):
        threading.Thread(target=Worker,daemon=True).start()


def start_queue():
    for i in QUEUES:
        print("QUEUE : "+str(i))
        q.put(i)
    q.join()

def join_meet(con,addr):
    print("\n"+str(addr)+">>",end="")
    while True:
        cmd = input()
        if cmd == "exit":
            break
        con.send(cmd.encode(encoding="utf-8"))
        time.sleep(1.2)
        datos = con.recv(2048)
        datos.decode("utf-8")
        print("{}\n{}>>".format(str(datos),str(addr)),end="")



start_socket("localhost",40415)
bind_socket()
start_threading()
start_queue()