from socket import socket

def echoServer(port):
    '''
    create a server that echos back the message sent
    '''
    s = socket()
    s.bind(('', port))
    s.listen(1)
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data)
    conn.close()
    s.close()
    return
