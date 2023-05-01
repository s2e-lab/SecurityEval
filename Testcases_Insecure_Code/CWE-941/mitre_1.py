import socket


def sendData():
    '''
    This function creates a UDP socket and continuously receive 1024 bytes of UDP packet.
    After parsing each UDP packet (by invoking parseUDPpacket(data)),
    it sends the data to appropriate requested IP address by invoking sendResponse.
    '''

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    while true:
        data = sock.recvfrom(1024)
        if not data:
            break
        (requestIP, record) = parseUDPpacket(data)
        sendResponse(requestIP, record)
