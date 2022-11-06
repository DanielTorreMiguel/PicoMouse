# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Mouse example"""
import time
import analogio
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)




while True:
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(1) 
    mouse.move(x=100)
    time.sleep(1)  # Debounce delay
    mouse.move(x=-100)
    time.sleep(1)

