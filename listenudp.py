import socket
from struct import unpack

# Creation d'un socket UDP (SOCK_DGRAM)

UDPSOCK = socket.socket(type=socket.SOCK_DGRAM)

# Ecoute sur port 21567 a tous les IPs
listen_addr = ("",5151)
#send_addr = ("localhost",5432)

UDPSOCK.bind(listen_addr)


while True:
    # On attend un paquet de taille 1024 octets m
    data, addr = UDPSOCK.recvfrom(1024)
    print(len(data))
    message = unpack('dddd', data)
    print (message, " from \t", addr)
  
  #data =  pack('dddddd',666., 3.4, 4.5,7.2, 8.4, 9.5)

  #print "send back now:"
  #UDPSock.sendto(data,send_addr)