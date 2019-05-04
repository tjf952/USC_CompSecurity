# Client Script

import socket
import sys

HOST = sys.argv[1]
PORT = 80

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
server_address = (HOST, PORT)
print >>sys.stderr, 'Connecting to %s Port %s' % server_address
sock.connect(server_address)

try:
	# Ask user for file
	file = raw_input("What file do you want to view?  ")

	# Send data
	message = 'GET /' + file + ' HTTP/1.1'
	print >>sys.stderr, 'Sending: "%s"' % message
	sock.sendall(message)

	#Look for response
	data = sock.recv(1024)
	print >>sys.stderr, 'Received: "%s"' % data

finally:
    print >>sys.stderr, 'Closing Socket'
    sock.close()
