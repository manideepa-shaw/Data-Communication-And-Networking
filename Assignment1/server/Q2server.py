import socket
import os

IP_ADD='172.24.48.173'
TCP_PORT=3000
BUFF_SIZE=8*1024*1024 #1 MB

k = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

k.bind((IP_ADD,TCP_PORT))
k.listen(1)

# accept blocks execution untill it receives any req from client
conn, add = k.accept()

data=conn.recv(BUFF_SIZE)
filename=data.decode()

# check if the file exists
if os.path.exists(filename):
    with open(filename,'r') as sendfile:
        msg=sendfile.read(BUFF_SIZE)
else:
    msg="File not Found!!!"


conn.send(msg.encode())

conn.close()