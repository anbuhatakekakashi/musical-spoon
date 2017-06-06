import socket
import sys


HOST = '127.0.0.1'
PORT = 10002
s = socket.socket()
s.connect((HOST, PORT))

while 1:
    msg = raw_input("[>> Enter Rick or Morty: ")
    if msg == "close":
       s.close()
       sys.exit(0)
    s.send(msg)
    buf = s.recv(1024)
    print(buf)
