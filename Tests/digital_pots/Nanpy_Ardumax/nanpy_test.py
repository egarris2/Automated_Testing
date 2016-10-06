#import nanpy serial library for arduino. Information found at https://nanpy.github.io/
from nanpy import (ArduinoApi, SerialManager)
from nanpy.MCP41xxx import MCP41xxx
from time import sleep
import logging
logging.basicConfig(level=logging.DEBUG)


#setup serial communication with Arduino
connection = SerialManager('COM8')

DigPot = MCP41xxx(49, connection=connection)

DigPot.analogWrite(0,210)
DigPot.analogWrite(1,220)
DigPot.analogWrite(2,230)
DigPot.analogWrite(3,255)

