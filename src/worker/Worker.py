from datetime import datetime
import socket
from dbFunctions import DBFunctions
import random



class Worker:

    def __init__(self,adresa):
        self.adresa = adresa
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def connectToLB(self):
        try:
            self.sock.connect(self.adresa)
        except socket.error as error:
            print(str(error))
            return False
        return True

    def handle(self,id,code,value,dataset):
        db = DBFunctions()
        if db.dbConnect():
            print("konektovan sa bazom")
            #db.createTable(dataset)
            
            if db.entityExistance(id,dataset):
                print("postoji entitet")
                if code == "CODE_DIGITAL":
                    db.updateTable(id,code,value,dataset)
                else:
                    currentValue = db.getValue(id,dataset)
                    deadband = db.getDeadband(currentValue,value,dataset)
                    if deadband >=2:
                        db.updateTable(id,code,value,dataset)
            else:
                print("pokusavam da insertujem")
                db.InsertIntoTable(id,code,value,dataset)
                print("insertovano")

    def RecvProcess(self):
        while True:
            try:
                data = self.sock.recv(2048)
                print(data.decode())
            except Exception as e:
                print(e)
                break
            if not data:
                break
            else:
                print("usao sam u else")
                id = random.randint(0,200)
                #WRITER: POSLATO:CODE:VALUE
                #LB: CODE:VALUE
                code = data.decode().split(":")[0]
                value = data.decode().split(":")[1]
                dataset = self.getDataSet(code)
                print(f"{code},{value},{dataset}")
                self.handle(id,code,value,dataset)

        self.sock.close()

    def getDataSet(self,code):
        if(code == "CODE_ANALOG")or(code == "CODE_DIGITAL"):
            dataset = 1
        elif(code == "CODE_CUSTOM")or(code == "CODE_LIMITSET"):
            dataset = 2
        elif(code == "CODE_SINGLENODE")or(code == "CODE_MILITPLENOD"):
            dataset = 3
        elif(code == "CODE_CONSUMER")or(code == "CODE_SOURCE"):
            dataset = 4
        return dataset


             
