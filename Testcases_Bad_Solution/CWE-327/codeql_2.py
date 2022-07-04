import ssl
import socket

def createSSLWrapper(host, port):
    '''
    create a SSL wrapper for the socket, set-up the connection and return the socket
    '''
    ssl_sock = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    ssl_sock.connect((host, port))
    return ssl_sock
