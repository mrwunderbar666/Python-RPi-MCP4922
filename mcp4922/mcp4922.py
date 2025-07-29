#!/usr/bin/python

"""
Python Library for MCP4922 DAC using Raspberry Pi 3 Model B+
2 Channels, 12 Bit
Currently only supports Hardware SPI
Requires: RPi.GPIO & spidev libraries

Wiring:

MCP4922    =======>   Raspberry Pi

CS         ------->   GPIO08 Physical Pin 24 (SPI0 CE0) => Can be changed
SDI        ------->   GPIO10 Physical Pin 19 (SPI0 MOSI) => cannot be changed in hardware SPI MODE
SCK        ------->   GPIO11 Physical Pin 23 (SPI0 SCLK) => cannot be changed in hardware SPI MODE
"""

from typing import Literal

import RPi.GPIO as GPIO
import spidev


class MCP4922:
    """Class for the Microchip MCP4922 digital to analog converter"""

    spi = spidev.SpiDev()

    def __init__(self, bus=0, device=1, chip_select: int | None = None):
        """Initialize MCP4922 device with hardware SPI
        Chipselect default value is BCM Pin 8 (Physical Pin: 24)
        Select the bus and device number. Default values are:
        Bus = 0 ; Device = 1
        If you're not sure, just keep default values
        """
        mode = GPIO.getmode()
        if mode == GPIO.BOARD:
            default_cs = 24
        elif mode == GPIO.BCM:
            default_cs = 8
        else:
            raise ValueError(
                "You haven't selected a GPIO Mode? Use: e.g. GPIO.setmode(GPIO.BCM)"
            )

        self.bus = bus
        self.device = device

        if chip_select is None:
            self.chip_select = default_cs
        else:
            self.chip_select = chip_select

        GPIO.setup(self.chip_select, GPIO.OUT)
        GPIO.output(self.chip_select, 1)
        # As soon as MCP4922 object is instantiated spidev bus and device are opened
        # otherwise causes memory leak and creates Errno 24
        self.spi.open(self.bus, self.device)

    def __repr__(self) -> str:
        return f"MCP4922(bus={self.bus}, device={self.device}, chip_select={self.chip_select}"

    def set_voltage(self, channel: Literal[0, 1], value: int):
        """
        Regular set_voltage Function
        Select your channel 0 or 1
        Select Voltage value 0 to 4095
        """
        if channel == 0:
            output = 0x3000
        elif channel == 1:
            output = 0xB000
        else:
            raise ValueError(
                "MCP4922 Says: Wrong Channel Selected! Chose either 0 or 1!"
            )
        if value > 4095:
            value = 4095
        if value < 0:
            value = 0

        output |= value
        buf0 = (output >> 8) & 0xFF
        buf1 = output & 0xFF
        GPIO.output(self.chip_select, 0)
        self.spi.writebytes([buf0, buf1])
        GPIO.output(self.chip_select, 1)

    def set_voltage_gain(self, channel: Literal[0, 1], value: int):
        """
        The MCP4922 has the ability to output the double of the reference Voltage
        Reference Voltage is measured by the MCP4922 at pin 13 (VrefA) for Channel A and pin 11 (VrefB) for Channel B
        Note that the output voltage cannot exceed the supply voltage from pin 1 (VDD)
        """
        if channel == 0:
            output = 0x1000
        elif channel == 1:
            output = 0x9000
        else:
            raise ValueError(
                "MCP4922 Says: Wrong Channel Selected! Chose either 0 or 1!"
            )
        if value > 4095:
            value = 4095
        if value < 0:
            value = 0

        output |= value
        buf0 = (output >> 8) & 0xFF
        buf1 = output & 0xFF
        GPIO.output(self.chip_select, 0)
        self.spi.writebytes([buf0, buf1])
        GPIO.output(self.chip_select, 1)

    def set_voltage_buffered(self, channel: Literal[0, 1], value: int):
        """
        Using the buffer feature of the MCP4922,
        refer to the datasheet for details
        """
        if channel == 0:
            output = 0x7000
        elif channel == 1:
            output = 0xF000
        else:
            raise ValueError(
                "MCP4922 Says: Wrong Channel Selected! Chose either 0 or 1!"
            )
        if value > 4095:
            value = 4095
        if value < 0:
            value = 0

        output |= value
        buf0 = (output >> 8) & 0xFF
        buf1 = output & 0xFF
        GPIO.output(self.chip_select, 0)
        self.spi.writebytes([buf0, buf1])
        GPIO.output(self.chip_select, 1)

    def shutdown(self, channel: Literal[0, 1]):
        """
        Completely shutdown selected channel for power saving
        Sets the output of selected channel to 0 and 500K Ohms.
        Read Datasheet (SHDN) for details
        """
        if channel == 0:
            output = 0x2000
        elif channel == 1:
            output = 0xA000
        else:
            raise ValueError(
                "MCP4922 Says: Wrong Channel Selected! Chose either 0 or 1!"
            )

        buf0 = (output >> 8) & 0xFF
        buf1 = output & 0xFF
        GPIO.output(self.chip_select, 0)
        self.spi.writebytes([buf0, buf1])
        GPIO.output(self.chip_select, 1)

    def close(self):
        """
        Closes the device
        """
        self.spi.close()

    def open(self):
        """
        Manually Open the device
        """
        self.spi.open(self.bus, self.device)
