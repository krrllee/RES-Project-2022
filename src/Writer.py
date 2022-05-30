import socket
import pickle
import time
import random
from Item import Item

HEADERSIZE = 10

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

listaKodova = ["CODE_ANALOG","CODE_DIGITAL","CODE_CUSTOM","CODE_LIMITSET","CODE_SINGLENOE","CODE_MULTIPLENODE","CODE_CONSUMER","CODE_SOURCE"]

def saljiPodatke():
    while True:
        
        data = Item(random.choice(listaKodova),random.randint(0,200))
        print(f"Code: {data.code} Value: {data.value}")
        pack = pickle.dumps(data)
        s.send(pack)
        time.sleep(2)

def main():
    msg = s.recv(1024)
    print(msg.decode("utf-8"))
    saljiPodatke()

if __name__ == "__main__":
    main()

             
    
