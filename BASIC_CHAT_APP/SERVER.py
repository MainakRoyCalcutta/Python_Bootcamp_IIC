import socket

s = socket.socket()
host = input(str("Please enter the host you want to connect to: "))
port = 1025

try:
    s.connect((host, port))
    print("Connected to internet")
except:
    print("Connection Failed")

while 1:
    in_msg = s.recv(1025)
    in_msg = in_msg.decode()
    print("Reply :", in_msg)

    msg = input(str("Enter your Message : "))
    msg = msg.encode()
    s.send(msg)
