import socket
def sendData():
    '''
    this function create UDP socket and continuesly recive 1024 bytes of UDP packet
    after parsing UDP packet, it sends the data to appropriate requested IP address
    '''
    global UDPsocket
    global UDP_Socket_IP
    global UDP_Socket_Port
    UDPsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    UDPsocket.bind((UDP_Socket_IP, UDP_Socket_Port))
    UDPsocket.settimeout(1)
    while True:
        try:
            data, addr = UDPsocket.recvfrom(1024)
            if data:
                parseUDP(data)
            else:
                UDPsocket.close()
                break
        except socket.timeout:
            pass
        except socket.error as error:
            print('socket error', error)
            break