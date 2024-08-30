import socket

IP_ADD='172.24.48.173'
TCP_PORT=3000
BUFF_SIZE=1024

k=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

k.connect((IP_ADD, TCP_PORT))

msg="Hi from client.".encode()
k.send(msg)

try:
    data, _ = k.recvfrom(BUFF_SIZE)
    print(data.decode())
finally:
    k.close()