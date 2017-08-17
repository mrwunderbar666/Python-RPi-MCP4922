# Python-RPi-MCP4922
Python Library for driving MCP4922 DAC (Digital to Analog Converter) on Raspberry Pi 3 Model B+

## About MCP 4922
The MCP4922 is a Digital to Analog Converter that has 2 Channels and 12 bit resolution.
The regular version has 14 pins and the datasheet is available here: http://ww1.microchip.com/downloads/en/DeviceDoc/22250A.pdf

## Installation

To install the library run the following commands on a Raspberry Pi or other Debian-based OS system:

### Install Git 
If you don't have it already:

```shell
sudo apt-get install git build-essential python-dev
```

### Requirements
To run this module you need RPi.GPIO and spidev:

```shell
sudo pip install RPi.GPIO
sudo pip install spidev
```

### Clone the repository

```shell
git clone https://github.com/mrwunderbar666/Python-RPi-MCP4922.git
```

### Install with Setup.py

```shell
cd Python-RPi-MCP4922
sudo python setup.py install
```

## Software
### Getting started

Go to the example directory and execute the test script:

```shell
cd examples
sudo python MCP4922_test.py
```

This script will initialize the MCP4922 and incrementally increase the voltage on both channels. Then it will decrease the voltage and loop forever.

If you want to manually set the channel and voltage, you can use the other test script:

```shell
sudo python MCP4922_set.py
```

### Use it in your own code

#### Setup
First import the required GPIO module in python:

```python    
import RPi.GPIO as GPIO
```

Set your pin mode to BCM:

```python
GPIO.setmode(GPIO.BCM)
``` 

and then import the MCP4922 module:

```python
from MCP4922 import MCP4922
```

#### MCP4922 Class
The MCP4922 Class takes 3 arguments: **spibus**, **spidevice** and **cs**.
To configure just simple use this code in python:

```python
dac = MCP4922(spibus=0, spidevice=0, cs=8)
```

##### spibus
Select the bus for your MCP4922. Should be either 0 or 1. 
If no argument is given it will turn to the default of 0.

Have a closer look at the spidev module (https://github.com/doceme/py-spidev) for more details.

##### spidevice
Select the device connected to the bus, should be either 0 or 1.
If no argument is given it will turn to the default of 1.

Also checkout the spidev documentation for more details.

##### cs
Chip select pin. Enter the pin number (Broadcom or Physical pin) where the MCP4922 is connected to.
If no argument is given it will turn to the default of 8 (Broadcom pin numbering) or 24 (physical pin numbering).


#### setVoltage(channel, value)
This method sets the desired output voltage at the requested channel. It is as easy as:

```python
dac.setVoltage(0, 2048)
```

This will set the voltage output to 50% of the reference voltage.

##### channel
The MCP4922 has two channels, you can select by giving the arguments 0 or 1.
0 is channel A, 1 is channel B.

Anything else will throw an error at you.

##### value
Interger value from 0 to 4095, where 4095 is 100% of the reference voltage.

If you insert a value beyond that reach it will be clamped to 4095 (or 0 if you give a negative value).

#### setVoltage_gain(channel, value)
The MCP4922 has the ability to output the double of the reference Voltage
Reference Voltage is measured by the MCP4922 at pin 13 (VrefA) for Channel A and pin 11 (VrefB) for Channel B
Note that the output voltage cannot exceed the supply voltage from pin 1 (VDD).

Example:

```python
dac.setVoltage_gain(0, 2048)
```

#### setVoltage_buffered(channel, value)
Using the buffer feature of the MCP4922, refer to the datasheet for details.

Example:

```python
dac.setVoltage_buffered(0, 2048)
```

#### shutdown(channel)
Completely shutdown selected channel for power saving. Sets the output of selected channel to 0 and 500K Ohms. Read Datasheet (SHDN) for details.

Example:

```python
dac.shutdown(1)
```

## Hardware

Here is an example of hooking up your MCP4922 to your Raspberry Pi.

**Of course no warranties for any damage.**

![MCP4922 Breadboard Example](https://github.com/mrwunderbar666/Python-RPi-MCP4922/raw/master/documentation/mcp4922sketch_bb.png)

And the schematic view:

![MCP4922 Schematic Example](https://github.com/mrwunderbar666/Python-RPi-MCP4922/raw/master/documentation/mcp4922sketch_schem.png)

Also: **Refer to the datasheet**


