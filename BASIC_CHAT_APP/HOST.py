import socket

s = socket.socket()
host = socket.gethostname()
print("Your connection server is starting on: ", host)
port = 1025

s.bind((host, port))
print("Server is ready to accept")

s.listen(1)

connection, adr = s.accept()
print("Connection established to address: ", adr)

while 1:
    msg = input(str("Enter your Message: "))
    msg = msg.encode()
    connection.send(msg)

    in_msg = connection.recv(1025)
    in_msg = in_msg.decode()
    print("Reply : ", in_msg)
