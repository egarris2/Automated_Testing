#import nanpy serial library for arduino. Information found at https://nanpy.github.io/
from nanpy import (ArduinoApi, SerialManager)
from nanpy.MCP41xxx import MCP41xxx
from time import sleep
from pinClasses import connection

#instance of MCP41xxx class from Nanpy
d = MCP41xxx(53, connection=connection)

#creating class for digital potentiometers MCP41xxx
class DigPot():

    def __init__(self, channel, value):
        self.channel = channel
        self.value = value
        d.analogWrite(self.channel, self.value)

    def setResistance(self, resistance):
        d.analogWrite(self.channel, resistance)
        self.value = resistance

LCT     = DigPot(0, 0)
DGT     = DigPot(1, 0)
DLWT    = DigPot(2, 0)
SCT     = DigPot(3, 0)



