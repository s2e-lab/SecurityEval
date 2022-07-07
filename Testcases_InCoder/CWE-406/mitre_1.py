import socket
def UDPMessaging(UDP_IP, UDP_PORT):
    '''
    create a UDP socket and receive 1024 bytes of data continuously
    parse the data and send back the DNS record to the requested IP in the packet
    '''
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((UDP_IP, UDP_PORT))
        while True:
            data, addr = sock.recvfrom(1024)
            message = data.decode()
            IP = addr[0]
            PORT = addr[1]
            socket.sendto(message, ("8.8.8.8", 53))
    except socket.error as msg:
        print(msg)
    finally:
        sock.close()