import evdev
import socket
from struct import pack

# Communication udp
#SEND_ADDR = ("localhost", 5432)
SEND_ADDR = ("134.157.19.154", 5432)
UDPSOCK = socket.socket(type=socket.SOCK_DGRAM)

# Caracteristiques tablette
DEVICES = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in DEVICES:
    print(device.fn, device.name, device.phys)
DEV = evdev.InputDevice('/dev/input/event0')
CARAC = DEV.capabilities(verbose=True)
print(CARAC[3])
AXIS = {}
AXIS['x'] = {}
AXIS['y'] = {}
AXIS['pressure'] = {}
for axis in AXIS:
    AXIS[axis]['value'] = 0.0
    #AXIS[axis]['max'] = 

for event in DEV.read_loop():
    if event.type == evdev.ecodes.EV_ABS:
        if event.code == 0:
            AXIS['x']['value'] = event.value/100.0
        if event.code == 1:
            AXIS['y']['value'] = event.value/100.0
        if event.code == 24:
            AXIS['pressure']['value'] = event.value
        #print(str(AXIS['x']) + " " + str(AXIS['y']))
        data = pack('dddd', 666., AXIS['x']['value'], AXIS['y']['value'], AXIS['pressure']['value'])
        UDPSOCK.sendto(data, SEND_ADDR)
