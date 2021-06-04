#
#
#

import socket

HOST, PORT = '', 8888

# create an INET, STREAMing socket
    # INET == Internet
    # STREAMing socket == stream socket (uses the protocols  TCP, SCTP, or DCCP)
    # a stream socket allows processes to communicate using protocols
    # a stream socket provides a bidirectional, reliable, sequenced, and un-duplicated flow of data
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(f'Serving HTTP on port {PORT} ...')
while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)
    print(request_data.decode('utf-8'))

    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)
    client_connection.close()


