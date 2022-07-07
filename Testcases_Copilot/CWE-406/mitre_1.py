import socket
def UDPMessaging(UDP_IP, UDP_PORT):
    '''
    create a UDP socket and receive 1024 bytes of data continuously
    parse the data and send back the DNS record to the requested IP in the packet
    '''
