import socket
import threading
from typing import Tuple
from constants import SERVER_HOST_PORT


def setup_server(address: Tuple[str, str], backlog: int = 100) -> socket.socket:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(address)
    server_socket.listen(backlog)
    return server_socket


def process_client(client_socket: socket.socket) -> None:
    while True:
        msg = client_socket.recv(1024).decode()
        if not msg:
            break
        fmt_msg = f"msg received: {msg}"
        print(fmt_msg)
    client_socket.close()


if __name__ == "__main__":
    server_socket = setup_server(address=SERVER_HOST_PORT)
    print("server is running")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"{client_address} connected")
        client_thread = threading.Thread(target=process_client, args=(client_socket,))
        client_thread.start()
