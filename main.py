"""Get the current mouse position."""

import logging
import sys

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG,
                    stream=sys.stdout)


def get_mouse_position():
    """
    Get the current position of the mouse.

    Returns
    -------
    dict :
        With keys 'x' and 'y'
    """
    mouse_position = None
    import sys
    try:
        import tkinter  # Tkinter could be supported by all systems
    except ImportError:
        logging.info("Tkinter not installed")
        tkinter = None
    if tkinter is not None:
        p = tkinter.Tk()
        x, y = p.winfo_pointerxy()
        mouse_position = {'x': x, 'y': y}
    return mouse_position
while True:
    print(get_mouse_position())