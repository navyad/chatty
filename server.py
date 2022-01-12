import socket
from typing import Tuple
from constants import SERVER_HOST_PORT


def setup_server(address: Tuple[str, str], backlog: int = 100) -> Tuple[socket.socket, str]:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(address)
    server_socket.listen(backlog)
    return server_socket.accept()


def process_client(client_socket: socket.socket) -> None:
    while True:
        msg = client_socket.recv(1024).decode()
        fmt_msg = f"msg received: {msg}"
        print(fmt_msg)


if __name__ == "__main__":
    client_socket, client_address = setup_server(address=SERVER_HOST_PORT)
    process_client(client_socket=client_socket)
