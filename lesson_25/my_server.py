import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 65000))
server_send = server_socket.recv(1024)
print(server_send)
server_socket.close()
