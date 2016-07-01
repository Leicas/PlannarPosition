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
CARAC = DEV.capabilities()
print(CARAC[3])
AXIS = {}
AXIS['x'] = {}
AXIS['x']['num'] = 0
AXIS['y'] = {}
AXIS['y']['num'] = 1
AXIS['pressure'] = {}
AXIS['pressure']['num'] = 24
i = 1
for axis in AXIS:
    AXIS[axis]['value'] = 0.0
    AXIS[axis]['max'] = CARAC[3][i][2][3]
    print(AXIS[axis]['max'])
    i += 1

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
