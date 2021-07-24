import socket
import threading

HOST = '127.0.0.1'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
server.bind((HOST, PORT))

server.listen()

clients = []
nicknames = []

# Broadcast 
 
def broadcast(message):
     for client in clients:
         client.send(message)

# Handle ( This function is used to handel the indevidual connection to the client)

def handle(client): # client take as parameter
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]} says {message}")
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break


# Receive (this function is wait for the new connections)

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with{str(address)}!")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)
        1
        nicknames.append(nickname) 
        clients.append(client)

        print(f"Nickname of the client is {nickname} .")
        broadcast(f"{nickname} Connected to the the server!\n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        thread = threading.Thread (target=handle , args=(client,)) # we use this comma because we need to treated this as tuple
        thread.start()

print("Server Running......")
receive()