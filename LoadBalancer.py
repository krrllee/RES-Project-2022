import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
        cliensocket,address = s.accept()
        print(f"Connection from {address} has been established!")
        cliensocket.send(bytes("Welcome, writer.","utf-8"))
        cliensocket.close()