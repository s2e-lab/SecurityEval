import socket

def parseUDPpacket(data):
    pass


def resolveName(nameToResolve):
    pass


def sendResponse(requestIP, record):
    pass


def UDPMessaging(udp_ip, udp_port):
    '''
    Create a UDP socket that listens on the IP and port provided for DNS requests.
    Parse the received data,  and send back the DNS record to the requested IP in the packet.
    '''

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((udp_ip, udp_port))
    while True:
        data = sock.recvfrom(1024)
        if not data:
            break
        (requestIP, nameToResolve) = parseUDPpacket(data)
        record = resolveName(nameToResolve)
        sendResponse(requestIP, record)
