from socket import AF_INET, SOCK_STREAM, socket
import config as c

with socket(AF_INET, SOCK_STREAM) as cl:
    cl.connect((c.HOST, c.PORT))

    name = input("Enter your name: ")
    cl.send(bytes(name, 'utf-8'))

    # receive(buffer size)
    print(cl.recv(1024).decode())
