import socket

# Get the hostname and set the port number
host = socket.gethostname()
port = 2004

# Set the buffer size
BUFFER_SIZE = 2000

# Prompt the user for a message
MESSAGE = input("tcpClientB: Enter message/ Enter exit:")

# Create a socket object
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
tcpClientB.connect((host, port))

# Continuously send and receive messages until the user enters 'exit'
while MESSAGE != 'exit':
    # Send the message to the server
    tcpClientB.send(MESSAGE.encode())

    # Receive data from the server
    data = tcpClientB.recv(BUFFER_SIZE).decode()

    # Print the received data
    print("Client2 received data:", data)

    # Prompt the user for the next message
    MESSAGE = input("tcpClientB: Enter message to continue/ Enter exit:")

# Close the socket
tcpClientB.close()
