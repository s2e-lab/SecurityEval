import socket
def sendData():
    '''
    this function create UDP socket and continuesly recive 1024 bytes of UDP packet
    after parsing UDP packet, it sends the data to appropriate requested IP address
    '''
