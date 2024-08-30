import socket

IP_ADD='172.24.48.173'
TCP_PORT=3000
BUFF_SIZE=1024

k = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

k.connect((IP_ADD, TCP_PORT))

filename="Q1server.py"
k.send(filename.encode())

data = k.recv(BUFF_SIZE)
content = data.decode()
if content=="File not Found!!!":
    print(content)
else:
    with open(filename,'w') as file:
        file.write(content)
    print("File downloaded")
k.close()