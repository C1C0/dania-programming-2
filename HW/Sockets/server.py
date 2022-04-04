from socket import AF_INET6, SOCK_DGRAM, socket, AF_INET, SOCK_STREAM
import config as c

# Socket
# Expecting IPv4 on TCP port
s = socket(AF_INET, SOCK_STREAM)

# Socket - Expecting IPv6 on UDP port
# s = socket(AF_INET6, SOCK_DGRAM)
print("Socket created")

# Binding
s.bind((c.HOST, c.PORT))

# Listen for connections
s.listen(c.SERVER_NUMBER_OF_CONNECTIONS)
print("waiting for connections")

try:
    while True:
        # Accepts connection
        # returns Client socket and client's address
        cl, addr = s.accept()
        name = cl.recv(1024).decode()
        
        # addr = tuple of: (ip add, port number of client)
        print("connected with:", addr, name)        
        
        # sending message
        cl.send(bytes(f"{name} Welcome to Server", 'utf-8'))
        
        # Saving resources
        cl.close()
        
except KeyboardInterrupt:
    print("Shutting down application and all connections")
    exit()
    
