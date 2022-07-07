import socket
def sendData():
    '''
    this function create UDP socket and continuesly recive 1024 bytes of UDP packet
    after parsing UDP packet, it sends the data to appropriate requested IP address
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 0))
    while True:
        data, addr = sock.recvfrom(1024)
        print("Received message: ", data.decode())
        sock.sendto(data, addr)
    return
