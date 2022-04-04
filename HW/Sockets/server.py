from socket import AF_INET6, SOCK_DGRAM, socket, AF_INET, SOCK_STREAM
import config as c

with socket(AF_INET, SOCK_STREAM) as s:
    print("Socket created.")
    s.bind((c.HOST, c.PORT))
    s.listen()

    try:       
        while True:
            # Accepts connection
            # returns Client socket and client's address
            cl, addr = s.accept()
            
            with cl:
                name = cl.recv(1024).decode()
                
                # addr = tuple of: (ip add, port number of client)
                print("connected with:", addr, name)        
            
                # sending message
                cl.send(bytes(f"{name} Welcome to Server", 'utf-8'))
            
    except KeyboardInterrupt:
        print("Shutting down application and all connections")
        exit()
        
