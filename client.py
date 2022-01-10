import socket

SERVER_HOST_PORT = ("127.0.0.1", 1234)

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj.connect(SERVER_HOST_PORT)

while True:
    input_msg = input("you: ").encode()
    assert isinstance(input_msg, bytes)
    socket_obj.send(input_msg)
