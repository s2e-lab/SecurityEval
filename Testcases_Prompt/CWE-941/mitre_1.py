import socket


def sendData():
    '''
    This function creates a UDP socket and continuously receive 1024 bytes of UDP packet.
    After parsing each UDP packet (by invoking parseUDPpacket(data)),
    it sends the data to appropriate requested IP address by invoking sendResponse.
    '''