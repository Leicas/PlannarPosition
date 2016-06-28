import evdev

devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
for device in devices:
    print(device.fn, device.name, device.phys)
dev = evdev.InputDevice('/dev/input/event0')
print(dev.capabilities(verbose=True))
axis = {}
axis['x'] = 0.0
axis['y'] = 0.0
axis['pressure'] = 0.0
for event in dev.read_loop():
    if event.type == evdev.ecodes.EV_ABS:
      if event.code == 0:
       axis['x'] = event.value/100.0
      if event.code == 1:
       axis['y'] = event.value/100.0
      print(str(axis['x']) + " " + str(axis['y']))
