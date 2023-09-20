import socket
import threading

# Define host and port for the server
HOST = 'localhost'
PORT = 5000

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

# List to hold all connected clients
clients = []

def handle_client(client_socket, client_address):
    """
    Function to handle incoming messages from a client
    """
    while True:
        try:
            # Receive message from the client
            message = client_socket.recv(1024).decode()

            # Broadcast the message to all other clients
            for c in clients:
                if c != client_socket:
                    c.send(message.encode())

        except:
            # Remove the client from the list if it disconnects
            clients.remove(client_socket)
            client_socket.close()
            break

while True:
    # Accept incoming connection
    client_socket, client_address = server_socket.accept()

    # Add the client to the list of clients
    clients.append(client_socket)

    # Create a thread to handle incoming messages from the client
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    thread.start()