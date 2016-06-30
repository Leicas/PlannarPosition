import evdev
import socket
from struct import pack

#SEND_ADDR = ("localhost", 5432)
SEND_ADDR = ("134.157.19.154", 5432)
UDPSOCK = socket.socket(type=socket.SOCK_DGRAM)

DEVICES = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in DEVICES:
    print(device.fn, device.name, device.phys)
DEV = evdev.InputDevice('/dev/input/event0')
print(DEV.capabilities(verbose=True))
AXIS = {}
AXIS['x'] = 0.0
AXIS['y'] = 0.0
AXIS['pressure'] = 0.0
for event in DEV.read_loop():
    if event.type == evdev.ecodes.EV_ABS:
        if event.code == 0:
            AXIS['x'] = event.value/100.0
        if event.code == 1:
            AXIS['y'] = event.value/100.0
        if event.code == 24:
            AXIS['pressure'] = event.value
        #print(str(AXIS['x']) + " " + str(AXIS['y']))
        data = pack('dddd', 666., AXIS['x'], AXIS['y'], AXIS['pressure'])
        UDPSOCK.sendto(data, SEND_ADDR)
