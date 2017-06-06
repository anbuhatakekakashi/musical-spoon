import time
import socket
from threading import Thread


MAX_LENGTH = 4096

counter = 0

def handle(clientsocket):
  counter = 4
  
  while 1:
  
    MAX_LENGTH = 4096
    buf = clientsocket.recv(MAX_LENGTH).lower()
    
    print(buf)
    
    #if (buf == ""):
     #   clientsocket.send("\n Close me try again!!! Close me try again!!! Close me try again!!! \n")
        
    if (buf == "rick" and counter == 4):
        clientsocket.send("\n[<< : Okay, well, sometimes, science is more art than science, Morty. A lot of people don't get that.\n")
        counter = 3
        print(counter)
 
    elif (buf == "morty" and counter == 3):
        clientsocket.send("\n[<< : OK, take it easy, Rick! Th-that's dark.\n")
        counter = 2
        print(counter)
        
    elif (buf == "morty" and counter == 2):
        clientsocket.send("\n[<< : Ah geez...I don't know Rick.\n")
        counter = 1
        print(counter)
        
        
    elif (buf == "rick" and counter == 1):
        clientsocket.send("\n[<< : Wait, wait. Stop. Hold it. Not like this. We need a hang glider. And a crot...\n")
        
        
        clientsocket.send("\n[<< : I WANT MY MCNUGGET DIPPING!!!\n")
        if (buf == "szechuan sauce"):
            clientsocket.send("\n[> : <username> & <password>\n")
            
        else:    
            time.sleep(10)
            clientsocket.send("\n[<< : Wub a lub a dub dub!!! Am I right?\n")
        
    #elif (buf is not ("Rick" or "Morty"):
    else:
        clientsocket.send("\n[<< : SHOW ME WHAT YOU GOT!!!\n")
        counter = 4

def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    PORT = 10002
    HOST = '127.0.0.1'

    serversocket.bind((HOST, PORT))
    serversocket.listen(10)

    while 1:
        #accept connections from outside
        (clientsocket, address) = serversocket.accept()

        ct = Thread(target=handle, args=(clientsocket,))
        ct.run()

if __name__ == '__main__':
    main()
