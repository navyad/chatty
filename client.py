import socket
from typing import Tuple
from constants import SERVER_HOST_PORT


def connect_server(address: Tuple[str, str]) -> socket.socket:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(address)
    return client_socket


def send_input(client_socket: socket.socket):
    while True:
        input_msg = input("you: ").encode()
        client_socket.send(input_msg)
    client_socket.close()


if __name__ == "__main__":
    client_socket = connect_server(address=SERVER_HOST_PORT)
    send_input(client_socket=client_socket)
