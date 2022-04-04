from socket import socket
import config as c

cl = socket()

cl.connect((c.HOST, c.PORT))

name = input("Enter your name: ")
cl.send(bytes(name, 'utf-8'))

# receive(buffer size)
print(cl.recv(1024).decode())
