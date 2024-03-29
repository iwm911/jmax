import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (sys.argv[1], int(sys.argv[2]))
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
sock.settimeout(5.0)

try:
    # Send data
    message = 'This is the message.  It will be repeated.'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    counter = 0
    while amount_received < amount_expected:
        counter += 1
        data = sock.recv(16)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data
        if counter > 50:
                break

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
