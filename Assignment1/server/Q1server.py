# create socket
# bind
# listen on port
# accept data(connection, address)
# send data/close connection
import socket

IP_ADD='172.24.48.173'
TCP_PORT=3000
BUFF_SIZE=30

k = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

k.bind((IP_ADD,TCP_PORT))
k.listen(1)

# accept blocks execution untill it receives any req from client
conn, add = k.accept()
print("Connection address is : ",add)

data=conn.recv(BUFF_SIZE)
print("Message from client : ",data.decode())

msg="Hi from server".encode()

conn.send(msg)

conn.close()