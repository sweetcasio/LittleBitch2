import keyboard
import time
import file
import sys
import os

# record file like -> code type time

STOP = 'esc'

now = time.time()


def record():
    recording = keyboard.record(STOP)

    with open(file.current, 'w') as dst:
        for r in recording:
            dst.write(f'{r.scan_code} {r.event_type} {round(r.time - now, 3)}\n')

