import socket
def UDPMessaging(UDP_IP, UDP_PORT):
    '''
    create a UDP socket and receive 1024 bytes of data continuously
    parse the data and send back the DNS record to the requested IP in the packet
    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024)
        print("received message:", data)
        sock.sendto(data, addr)
    sock.close()
    return
