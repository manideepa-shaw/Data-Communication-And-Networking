# create socket
# bind the address 
# accept data from client
# send data to client

import socket

IP_ADD='172.24.48.173'
TCP_PORT=3000
BUFF_SIZE=30

k = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)

k.bind((IP_ADD,TCP_PORT))

# accept blocks execution untill it receives any req from client
conn, add = k.recvfrom(BUFF_SIZE)
print("Connection address is : ",add)

data=conn.decode()
print("Message from client : ",data)

msg="Hi from server".encode()

k.sendto(msg,add)
