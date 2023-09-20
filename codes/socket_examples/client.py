import socket
import threading

# Define host and port for the server
HOST = 'localhost'
PORT = 5000

def receive_messages(client_socket):
    """
    Function to receive and print messages from the server
    """
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            # If there's an error receiving the message, the server may have disconnected
            print('Error receiving message. Server may have disconnected.')
            client_socket.close()
            break

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Continuously send messages to the server
while True:
    message = input()
    client_socket.send(message.encode())