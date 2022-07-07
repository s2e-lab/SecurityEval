from socket import socket

def echoServer(port):
    '''
    create a server that echos back the message sent
    '''
    s = socket()
    s.bind(('', port))
    s.listen(1)
    c, addr = s.accept()
    print('Connected to: ', addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        c.send(data)
    c.close()
    s.close()
