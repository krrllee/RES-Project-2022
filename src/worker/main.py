from Worker import Worker

if __name__ == "__main__":
    adresa = ("127.0.0.1",21000)
    worker = Worker(adresa)
    if worker.connectToLB():
        try:
            worker.RecvProcess()
        except Exception as e:
            print(e)

    a = input()
    