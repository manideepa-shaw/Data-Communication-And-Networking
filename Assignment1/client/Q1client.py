# create socket
# connect to the server
# send message
# receive reply from server/ close the connection

import socket

IP_ADD='172.24.48.173'
TCP_PORT=3000
BUFF_SIZE=1024

k = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

k.connect((IP_ADD, TCP_PORT))

msg="Hi from Client".encode()
k.send(msg)

data = k.recv(BUFF_SIZE)
print(data.decode())

k.close()