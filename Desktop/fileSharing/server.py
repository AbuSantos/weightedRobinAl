import socket
import os
import threading

# Define server host and port
HOST = "127.0.0.1"
PORT = 12345

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}")


def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    try:
        # Receive the requested file name from the client
        file_name = client_socket.recv(1024).decode()

        # Ensure that file_name is a valid path and within a specific directory
        if not file_name.startswith("/path/to/your/files/"):
            raise ValueError("Invalid file path")

        # Open and send the requested file to the client
        with open(file_name, "rb") as file:
            data = file.read(1024)
            while data:
                client_socket.send(data)
                data = file.read(1024)
            print(f"Sent {file_name} to {client_address}")
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        client_socket.send("File not found".encode())
    except ValueError as ve:
        print(f"Invalid file path: {file_name}")
        client_socket.send(f"Invalid file path: {str(ve)}".encode())
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        client_socket.send(f"An error occurred: {str(e)}".encode())
    finally:
        # Close the client socket
        client_socket.close()


while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()

    # Create a new thread to handle the client
    client_thread = threading.Thread(
        target=handle_client, args=(client_socket, client_address)
    )
    client_thread.start()
