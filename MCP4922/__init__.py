"""
MCP4922 - Python Library for driving MCP4922 DAC on Raspberry Pi

This library provides an interface for controlling the MCP4922
Digital-to-Analog Converter via SPI on Raspberry Pi.

Example:
    import RPi.GPIO as GPIO
    from MCP4922 import MCP4922

    GPIO.setmode(GPIO.BCM)
    dac = MCP4922(spibus=0, spidevice=0, cs=8)
    dac.setVoltage(0, 2048)  # Set channel A to 50% of reference voltage
"""

from .MCP4922 import MCP4922

__version__ = "1.0.0"
__author__ = "mrwunderbar666"
__license__ = "MIT"

__all__ = ["MCP4922"]