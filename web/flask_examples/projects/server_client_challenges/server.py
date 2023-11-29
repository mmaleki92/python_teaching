import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(1)

print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

conn, addr = server_socket.accept()
print(f"Connection from {addr}")
