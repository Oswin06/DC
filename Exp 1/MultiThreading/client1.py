import socket

# Get the hostname and set the port number
host = socket.gethostname()
port = 2004

# Set the buffer size
BUFFER_SIZE = 2000

# Prompt the user for a message
MESSAGE = input("tcpClientA: Enter message/ Enter exit:")

# Create a socket object
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
tcpClientA.connect((host, port))

# Continuously send and receive messages until the user enters 'exit'
while MESSAGE != 'exit':
    # Send the message to the server
    tcpClientA.send(MESSAGE.encode())

    # Receive data from the server
    data = tcpClientA.recv(BUFFER_SIZE).decode()

    # Print the received data
    print("Client2 received data:", data)

    # Prompt the user for the next message
    MESSAGE = input("tcpClientA: Enter message to continue/ Enter exit:")

# Close the socket
tcpClientA.close()
