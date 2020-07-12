import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_client.sendto(b'Hello Word, I am beetroot student >:)', ('127.0.0.1', 65000))

