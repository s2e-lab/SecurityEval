import socket
def sendData():
    '''
    this function create UDP socket and continuesly recive 1024 bytes of UDP packet
    after parsing UDP packet, it sends the data to appropriate requested IP address
    '''

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind( (UDP_IP,UDP_PORT) )
    while true:
        data = sock.recvfrom(1024)
        if not data:
            break
        (requestIP, record) = parseUDPpacket(data)
        sendResponse(requestIP,record)