import socket

from constants import SERVER_HOST_PORT

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(SERVER_HOST_PORT)
server_socket.listen(10)


def process_client(client_socket: socket.socket) -> None:
    while True:
        msg = client_socket.recv(1024).decode()
        if not msg:
            break
        fmt_msg = f"msg received: {msg}"
        print(fmt_msg)
    client_socket.close()
