import socket


def my_client(text):
    socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_client.sendto(text, ('127.0.0.1', 65000))

