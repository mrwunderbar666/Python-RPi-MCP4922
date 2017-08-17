#!/usr/bin/python
# Python Library for MCP4922 DAC
# 2 Channels, 12 Bit
"""
Testing script:
Select Channel and Value for your MCP4922
Exit with CTRL C
"""

from MCP4922 import MCP4922
import sys

GPIO.setmode(GPIO.BCM)                 # use the Broadcom pin numbering
GPIO.setwarnings(False)             # disable warnings


if __name__ == '__main__':
    dac = MCP4922()

    try:
        while True:
            print("Regular setVoltage() Function")
            select_value = int(raw_input("Select Value: "))
            select_channel = int(raw_input("Select Channel, 0 or 1: "))
            dac.setVoltage(select_channel, select_value)
    except KeyboardInterrupt:   # Press CTRL C to exit program
        dac.setVoltage(0, 0)
        dac.setVoltage(1, 0)
        dac.shutdown(0)
        dac.shutdown(1)
        GPIO.cleanup()
        sys.exit(0)
