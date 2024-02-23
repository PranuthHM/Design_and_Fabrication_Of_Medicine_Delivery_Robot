from movement import *

import socket
TCP_IP = '192.168.107.178'
TCP_PORT = 8080
BUFFER_SIZE = 20
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connection address:', addr)
ck=1

while ck==1:
    data = conn.recv(BUFFER_SIZE)
    data=data.decode('UTF-8','ignore')

    print ("received data:", str(data))
    if str(data) == 'f':
        FORWORD(2)

    if str(data) == 'b':
        BACKWORD(2)

    if str(data) == 'l':
        LEFT(2)

    if str(data) == 'r':
        RIGHT(2)
  
    if str(data) == 's':
        STOP()

    if str(data) == 'one':
        ONE()

    if str(data) == 'two':
        TWO()
  
    if str(data) == 'three':
        THREE()

conn.close()
