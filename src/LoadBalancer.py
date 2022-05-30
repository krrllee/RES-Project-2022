import socket
import pickle
from models import Item as Item
import random
import Writer

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)
cliensocket,address = s.accept()
print(f"Connection from {address} has been established!")
cliensocket.send(bytes("Welcome, writer.","utf-8"))



skladiste = []


def primiPodatke():
    while True:
        rec = cliensocket.recv(2048)
        data = pickle.loads(rec)
        skladiste.append(data)
        print(f"Code: {data.code} Value: {data.value}")





def main():
    primiPodatke()

if __name__ == "__main__":
    main()

