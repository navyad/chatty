import socket
from typing import Tuple
from constants import SERVER_HOST_PORT


def connect_server(address: Tuple[str, str]) -> socket.socket:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(address)
    return server_socket


def send_input(server_socket: socket.socket):
    while True:
        input_msg = input("you: ").encode()
        assert isinstance(input_msg, bytes)
        server_socket.send(input_msg)


if __name__ == "__main__":
    server_socket = connect_server(address=SERVER_HOST_PORT)
    send_input(server_socket=server_socket)
