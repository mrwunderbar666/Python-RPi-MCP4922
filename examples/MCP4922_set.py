#!/usr/bin/python

from mcp4922 import MCP4922
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # use the Broadcom pin numbering
GPIO.setwarnings(False)  # disable warnings


if __name__ == "__main__":
    print("""
    Interactive testing script:
    Select Channel and Value for your MCP4922
    Exit with CTRL C
    """)
    dac = MCP4922()

    try:
        while True:
            print("Regular set_voltage() Function")
            select_value = int(input("Select Value: ").strip())
            select_channel = int(input("Select Channel, 0 or 1: ").strip())
            dac.set_voltage(select_channel, select_value)
    except KeyboardInterrupt:  # Press CTRL C to exit program
        dac.set_voltage(0, 0)
        dac.set_voltage(1, 0)
        dac.shutdown(0)
        dac.shutdown(1)
        GPIO.cleanup()
        sys.exit(0)
