import socket

# Define host and port
HOST = '127.0.0.1'
PORT = 1823

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Get user input
user_input = input("Enter a string: ")

# Send the input to the server
client_socket.send(user_input.encode())

# Receive the response from the server
response = client_socket.recv(1024).decode()

# Print the response
print("ASCII codes: " + response)

# Close the connection
client_socket.close()
