#!/usr/bin/python
# Python Library for MCP4922 DAC
# 2 Channels, 12 Bit
"""
Testing script:
Select Channel and Value for your MCP4922
Exit with CTRL C

MIT License

Copyright (c) 2017 mrwunderbar666

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from MCP4922 import MCP4922
import sys
import RPi.GPIO as GPIO

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
