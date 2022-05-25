import socket
import time 
import pickle
import random
from enum import Enum

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))
msg = s.recv(1024)
print(msg.decode("utf-8"))

class code(Enum):
    CODE_ANALOG = 1 
    CODE_DIGITAL = 2
    CODE_CUSTOM = 3
    CODE_LIMITSET = 4
    CODE_SINGLENOE = 5  
    CODE_MULTIPLENODE = 6 
    CODE_CONSUMER = 7 
    CODE_SOURCE  = 8

while True:
    CODE = random.choice(list(code))
    VALUE = random.randint(0,200)
    d = CODE,VALUE
    packet = pickle.dumps(d)
    s.sendall(packet)  
    print(d)
    time.sleep(2)

s.close()
