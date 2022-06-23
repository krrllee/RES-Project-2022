from time import sleep
from LoadBalancer import LoadBalancer
from threading import Thread

if __name__ == '__main__':
    
        client_address = ('127.0.0.1',20000)
        worker_address = ('127.0.0.1',21000)
        localBuffer = []
        povezaniKlijenti = []
        povezaniWorkeri = []
        dostupniWorkeri = []
        loadBalancer = LoadBalancer()



        client_socket = loadBalancer.napraviSocket(client_address)
        client_socket.listen(1)
        newThread = Thread(target=loadBalancer.clientListening,args=(client_socket,povezaniKlijenti,localBuffer,povezaniWorkeri,dostupniWorkeri))
        newThread.daemon = True
        newThread.start()
        

        worker_socket = loadBalancer.napraviSocket(worker_address)
        worker_socket.listen(1)
        wThread = Thread(target=loadBalancer.workerListening,args=(worker_socket,povezaniWorkeri,dostupniWorkeri))
        wThread.daemon = True
        wThread.start()

        sendingThread = Thread(target=loadBalancer.pripremaZaSlanjeWorkeru,args=(localBuffer,povezaniWorkeri,dostupniWorkeri))
        sendingThread.daemon = True
        sendingThread.start()


        a = input()

  


