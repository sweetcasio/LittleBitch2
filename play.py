import keyboard
import time
import file
import sys
import os

# expected line in file -> key type time

STOP = 'esc'


     
def play():
    def stop(event):
        nonlocal run
        run = False

    events = []
    with open(file.current, 'r') as src:
            for line in src.readlines():
                line = line.split()
                code = int(line[0])
                etype = line[1]
                etime = float(line[2])
                events.append(keyboard.KeyboardEvent(etype, scan_code=code, time=etime))

    if len(events) > 0:
        keyboard.hook_key(STOP, stop)
        run = True
        while run:
            keyboard.play(events[:-1], stop=STOP)
            if not run:
                break 

        