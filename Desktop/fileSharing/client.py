import socket

# Define server host and port
HOST = "127.0.0.1"
PORT = 12345

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Request a file from the server
file_name = input("Enter the file name to download: ")
client_socket.send(file_name.encode())

# Receive the file data and save it
with open(file_name, "wb") as file:
    data = client_socket.recv(1024)
    while data:
        file.write(data)
        data = client_socket.recv(1024)

print(f"Received {file_name} from the server")

# Close the client socket
client_socket.close()
