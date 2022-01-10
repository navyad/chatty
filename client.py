import socket

SERVER_HOST_PORT = ("127.0.0.1", 1234)

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj.connect(SERVER_HOST_PORT)

while True:
    client_msg = input("you: ")
    socket_obj.send(b"hi from client")
    server_message = socket_obj.recv(1024)
