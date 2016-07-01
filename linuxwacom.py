import socket
import time
from struct import pack

#SEND_ADDR = ("localhost", 5432)
SEND_ADDR = ("134.157.18.177", 5151)
UDPSOCK = socket.socket(type=socket.SOCK_DGRAM)


while True:
    data = pack('ddd', 664., 55, 0)
    print('envoyé')
    time.sleep(1)
    UDPSOCK.sendto(data, SEND_ADDR)
