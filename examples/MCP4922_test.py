#!/usr/bin/python

import time
import sys
import RPi.GPIO as GPIO

from mcp4922 import MCP4922

GPIO.setmode(GPIO.BCM)  # use the Broadcom pin numbering
GPIO.setwarnings(False)  # disable warnings


if __name__ == "__main__":
    print("""
    Testing script
    Incrementally increases and decreases voltage from 0 to 4000
    never ending loop on both channels
    """)
    dac = MCP4922()
    try:
        while True:
            x = 0
            for i in range(0, 100):
                x = x + 40
                dac.set_voltage(0, x)
                dac.set_voltage(1, x)
                print(x)
                time.sleep(0.1)
            for i in range(0, 100):
                x = x - 40
                dac.set_voltage(0, x)
                dac.set_voltage(1, x)
                print(x)
                time.sleep(0.1)

    except KeyboardInterrupt:  # Press CTRL C to exit program
        dac.set_voltage(0, 0)
        dac.set_voltage(1, 0)
        dac.shutdown(0)
        dac.shutdown(1)
        GPIO.cleanup()
        sys.exit(0)
