# Server Script

import socket
import sys

HOST = 'server'
PORT = 80

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (HOST, PORT)
print >>sys.stderr, 'Starting up on %s Port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
	# Wait for a connections
	print >>sys.stderr, 'Waiting for a Connection...'
	connection, client_address = sock.accept()
	
	# Responds to accepted connection
	try:
		print >>sys.stderr, 'Connection from', client_address
		
		# Receive request and perform functionality
		while True:
			data = connection.recv(1024)
			if data:
				print >>sys.stderr, 'Received: "%s"' % data
				print >>sys.stderr, 'Fetching data for client...'
				# Search for file and return contents
				file = '/tmp' + data.split()[1]
				try:
					with open(file, 'r') as f:
						file_contents = f.read()
						connection.sendall('HTTP/1.1 200 OK\n'+file_contents)
				except IOError:
					try:
						with open('/tmp/404.html', 'r') as d:
							file_contents = d.read()
							connection.sendall('HTTP/1.1 404 Not Found\n'+file_contents)
					except IOError:
						connection.sendall('HTTP/1.1 404 Not Found')
			else:
				print >>sys.stderr, 'No More Data from', client_address
				break
		
	finally:
		# Clean up the connection
		connection.close()