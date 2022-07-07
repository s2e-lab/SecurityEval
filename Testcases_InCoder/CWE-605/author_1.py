from socket import socket

def echoServer(port):
    '''
    create a server that echos back the message sent
    '''
    server = socket()
    server.bind(('',port))
    server.listen(5)
    while 1:
        client,address = server.accept()
        data = client.recv(1024)
        if not data:
            break
        server.send(data)
    client.close()
    server.close()