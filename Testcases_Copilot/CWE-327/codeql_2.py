import ssl
import socket

def createSSLWrapper(host, port):
    '''
    create a SSL wrapper for the socket, set-up the connection and return the socket
    '''
    s = socket.socket()
    s.connect((host, port))
    s = ssl.wrap_socket(s, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ALL")
    return s
