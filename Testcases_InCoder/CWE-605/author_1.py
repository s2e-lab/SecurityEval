from socket import socket

def echoServer(port):
    '''
    create a server that echos back the message sent
    '''
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', port))
    serverSocket.listen(1)

    while True:
        connectionSocket, addr = serverSocket.accept()
        message = connectionSocket.recv(1024).decode()
        connectionSocket.send(message.encode())
        connectionSocket.close()
