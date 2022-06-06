from http import server
import socket
import pickle
from sqlite3 import connect
import time
import random

#Treba da se napravi odredjena memorija ili lokacija gde ce se nalaziti podaci o aktivnim workerima da bi
#mogli da se gase i pale

from models import Item as Item

HEADERSIZE = 10
#LOCALHOST = socket.gethostbyname(socket.gethostname())
LOCALHOST = 'localhost'
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


    def UGASI(self,id:int):
    #connect.UGASIWORKERA(id)
        print(f"WORKER SA ID:{id} je upaljen")

    def UPALI(self,id:int):
    #connect.UPALIWORKERA(id)
        print(f"WORKER SA ID:{id} je ugasen")

    def Komanda(self):
        while True:
            data = input("Unesite komandu u formatu: UPALI/UGASI:BROJ \n ")
            commands = data.split(":") # commands = ["UPALI","0"]
            print(f"UNETA OPCIJA: {commands[0]} \n WORKER-ID: {commands[1]}")

            id=int(commands[1])

            match commands[0]:
                case "UPALI":
                    self.UPALI(id)
                case "UGASI":
                    self.UGASI(id)
                case _:
                    print("NIJE UNETA DOBRA OPCIJA")

    def start(self):
        #ovde treba implementirati sta radi metoda start
        return NotImplementedError
                

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



def main():                 #bolje ovako
    adresa = (LOCALHOST,PORT)
    writer1 = Writer(adresa)
    writer1.start()

if __name__ == "__main__":
    main()

             
    
