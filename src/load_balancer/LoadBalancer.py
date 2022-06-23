from threading import Thread
import threading
import os
import socket
import time
import pickle

class LoadBalancer:
    def __init__(self):
        self.mutexBuffer = threading.Semaphore(1)
        self.mutexWorker = threading.Semaphore(1)

    def napraviSocket(self,adresa):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind(adresa)
        s.listen(5)
        return s

    def primiPodatke(self,conn):
        data =  conn.recv(2048)
        return data

    def otpakujPodatke(self,data):
        return data.decode()

    def primiKomandu(self,poruka):
        return poruka.split(":")[0]

    def uzmiParametre(self,poruka):
        return poruka.split(":")[1] + ":" + poruka.split(":")[2]

    def smjestiPodatke(self,localBuffer,data):
        try:
            localBuffer.append(data)
            return True
        except:
            return False

    def pokreniWorkerApp(self,file):
        
        os.startfile(file)

    def pokreniWorker(self,file):
        try:
            wthread = Thread(target=self.pokreniWorkerApp,args=(file,)) 
            wthread.start()
            return True
        except:
            return False

    def provjeriDostupneWorkere(self,dostupniWorkeri):
        for worker in dostupniWorkeri:
            if(worker == False):
                return False
        return True

    def pronadjiWorkera(self,dostupniWorkeri):
        for worker in range(len(dostupniWorkeri)):
            if(dostupniWorkeri[worker]):
                return worker
        return -1

    def uzmiWorkera(self,index,povezaniWorkeri):
        if(index == -1):
            raise IndexError('Index out of range.')
        return povezaniWorkeri[index]

    def ugasiWorker(self,index,povezaniWorkeri,dostupniWorkeri):
        try:
            worker = povezaniWorkeri[index]
            del povezaniWorkeri[index]
            del dostupniWorkeri[index]
            worker.close()

            return True
        except:
            return False

    def porukaZaWorkera(self,localBuffer):
        poruka = ""
        for i in range(len(localBuffer)):
           poruka += localBuffer[i]
        localBuffer.clear()
        return poruka
           
    def workerListening(self,wSocket,povezaniWorkeri,dostupniWorkeri):
        try:

            while True:
                conn,wAddress = wSocket.accept()
                povezaniWorkeri.append(conn)
                dostupniWorkeri.append(True)
        except:
            exit()

    def clientListening(self,cSocket,povezaniKlijenti,localBuffer,povezaniWorkeri,dostupniWorkeri):
        try:

            while True:
                conn,adresa = cSocket.accept()
                povezaniKlijenti.append(conn)
                cThread = Thread(target=self.handle,args=(conn,adresa,povezaniKlijenti,localBuffer,povezaniWorkeri,dostupniWorkeri))
                print("Thread kreiran")
                cThread.start()
                print("Thread pokrenut")
                cThread.join()
                print("Thread zavrsen")
        except:
            exit()

    def ugasiKlijenta(self,conn,povezaniKlijenti):
        try:
            povezaniKlijenti.remove(conn)
            conn.close()

            return True
        except:
            return False
        
    def handle(self,conn,cAddress,povezaniKlijenti,localBuffer,povezaniWorkeri,dostupniWorkeri):
        while True:
            data = self.primiPodatke(conn)
            
            if(data):
                
                poruka = self.otpakujPodatke(data)
                print(poruka)
                komanda = self.primiKomandu(poruka)
                if(komanda == "Poslato"):
                    print("Usao sam u if POSLATO")
                    params = self.uzmiParametre(poruka)
                    print("Uzeo sam parametre:"+params)
                    #self.mutexBuffer.acquire()
                    print("prosao semafor")
                    smjestenPodatak = self.smjestiPodatke(localBuffer,params)
                    print(str(smjestenPodatak))
                    if(smjestenPodatak):
                        print("Spremljeno.")
                    #self.mutexBuffer.release()
                    self.ugasiKlijenta(conn,povezaniKlijenti)
                    break

                elif(komanda == "UPALI"):
                    path = os.path.dirname(__file__)
                    file = os.getcwd()
                    file = os.path.normpath(os.getcwd()+os.sep + os.pardir)
                    #file = os.path.join(path,'..','Worker','main.py')
                    #../../Desktop/Worker/main.py
                    file = os.path.join(file,'Worker','main.py')
                    print(file)
                    pokrenutWorker = self.pokreniWorker(file)
                    print("WORKER UPALJEN")

                elif(komanda == "UGASI"):
                    sviDostupniWorkeri = self.provjeriDostupneWorkere(dostupniWorkeri)
                    ugaseniWorker = False
                    if(sviDostupniWorkeri):
                        #self.mutexWorker.acquire()
                        index = self.pronadjiWorkera(dostupniWorkeri)
                        ugaseniWorker = self.ugasiWorker(index,povezaniWorkeri,dostupniWorkeri)
                        #self.mutexWorker.release()
                        
                        print("WORKER UGASEN.")
            else:
                ugasenKlijent = self.ugasiKlijenta(conn,povezaniKlijenti)
                if(ugasenKlijent):
                    break

    def posaljiWorkeru(self,index,worker,dostupniWorkeri,poruka):
        try:
            worker.send(poruka)
            dostupniWorkeri[index] = False
            return True
        except Exception as e:
            print(e)
            return False

    def pripremaZaSlanjeWorkeru(self,localBuffer,povezaniWorkeri,dostupniWorkeri):
        while True:
            #self.mutexBuffer.acquire()
            if(len(localBuffer)>=1):
                #self.mutexWorker.acquire()
                print("prosao if za worker bafer")
                index = self.pronadjiWorkera(dostupniWorkeri)
                print(f"pronasao sam workera:{index}")
                if(index == -1):
                    #self.mutexBuffer.release()
                    #self.mutexWorker.release()
                    time.sleep(2)
                    continue
                worker = self.uzmiWorkera(index,povezaniWorkeri)
                print(worker)
                poruka = self.porukaZaWorkera(localBuffer)
                print(poruka)
                #self.mutexBuffer.release()
                workerPoruka = self.posaljiWorkeru(index,worker,dostupniWorkeri,poruka.encode())
                print(workerPoruka)
                if(workerPoruka):
                    print(f"Poslato workeru:{poruka}")
   

    