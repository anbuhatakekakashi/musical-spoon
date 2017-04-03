import socket
import threading
from Settings import menu

class ThreadedServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        #Passive listening for new connections
        self.sock.listen(5)

        while True:
        
            client, address = self.sock.accept()
            client.settimeout(300)
            
            #Creating thread for each connection coming in
            threading.Thread(target = self.listenToClient, \
            args = (client,address)).start()
            
            print ("[+] New thread started for " + str(address))

    def listenToClient(self, client, address):
        bufferSize = 1024
        
        #Must do ".encode()" for strings to be sent using ".send()"
        client.send(menu.encode())
        
        while True:
            try:
                data = client.recv(bufferSize).decode()
                
                if data:
                    if   (data == 1):
                        client.send("**Option 1: This is a placeholder**\n".encode())
                    elif (data == 2):
                        client.send("**Option 2: This is a placeholder**\n".encode())
                    else:
                        client.send("ERROR: Please choose a valid option\n".encode())
                        
                    # Set the response to echo back the recieved data 
                    #response = data
                    
                    #client.send(response)
                    
                else:
                    raise error('Client disconnected')
                    
            except:
            
                client.close()
                
                return False

def Main():
    #serverIP = input("IP? ")
    #portNum = int(input("PORT? "), 10)
    
    serverIP = "127.0.0.1"
    portNum = 5000
    
    ThreadedServer(serverIP, portNum).listen()

if __name__ == "__main__":
    Main()
