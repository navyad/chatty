import socket

HOST_PORT = ("127.0.0.1", 1234)

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_obj.bind(HOST_PORT)
socket_obj.listen()
client_soc, addr = socket_obj.accept()

while True:
    msg = client_soc.recv(1024).decode()
    fmt_msg = f"msg received: {msg}"
    print(fmt_msg)
