

#There are 9 main socket API functions
# socket()
# bind()
# listen()
# accept()
# connect()
# connect_ex()
# send()
# recv()
# close()

#The following code is going to make an echo server, which will echo whatever it recieves back to the client

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #Creates a socket object that supports the context manager type, so you can use it in a with statement
# The arguments passed to socket() specify the address family and socket type. AF_NET is the address family for IPv4, and SOCK_STREAM is the socket type for TCP.
    s.bind((HOST, PORT)) #bind() associates the socket object with a specific network interface and port number. It's arguments depends on the address family (IPv4)
# So it expectes a HOST and Port.

# HOST can be a hostname, IP address, or an empty string. If an ip address is used, it should be an IPv4-formatted address string.
# The IP address 127.0.0.1 is the standard IPv4 address for the loopback interface, which means it will communicate back to the host. If you use an empty string,
# the server will accept connections on all available IPv4 interfaces.

# PORT should be an integer from 1-65535 (0 is reserved). It’s the TCP port number to accept
# connections on from clients. Some systems may require superuser privileges if the port is < 1024.
    s.listen() # listen() enables a server to accept() connections. It makes it a "listening" socket.
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)