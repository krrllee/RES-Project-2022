from http import server
import socket
import pickle
from sqlite3 import connect
import time
import random


from models import Item as Item

HEADERSIZE = 10
LOCALHOST = socket.gethostbyname(socket.gethostname())
PORT = 1234
listaKodova = ["CODE_ANALOG","CODE_DIGITAL","CODE_CUSTOM","CODE_LIMITSET","CODE_SINGLENOE","CODE_MULTIPLENODE","CODE_CONSUMER","CODE_SOURCE"]

class Writer:
    server : object
    konektovana_adresa : object

    def __init__(self, server_adresa):
        self.server_adresa=server_adresa
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def Connect(self):
        self.sock, self.konektovana_adresa = self.sock.connect((self.server_adresa,PORT))


    def Komande(self):
        while(True):
            print("\n\t1 - UPALI\n \t2 - UGASI")
            opcija=int(input())
            poruka=""
            if(opcija==1):
                poruka="Upali"
            elif(opcija==2):
                poruka="Ugasi"
            else:
                print("\t Zadata opcija ne postoji.")

            if poruka!="" :
                self.socket.connect(self.server_addres)
                

    def saljiPodatke(self):
        while True:
            
            data = Item(random.choice(listaKodova),random.randint(0,200))
            print(f"Code: {data.code} Value: {data.value}")
            pack = pickle.dumps(data)
            self.sock.send(pack)
            time.sleep(2)

    def PrimiPodatke(self):
        msg = self.sock.recv(1024)
        msg = msg.decode("utf-8")
def main():
    writer1 = Writer(LOCALHOST)
    writer1.saljiPodatke()

if __name__ == "__main__":
    main()

             
    
