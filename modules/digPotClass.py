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

    def setDigValue(self, temp):
        digValue = 256 -(((1.004067693419610*(10**-9))*(temp**6)-((1.132507884449970 * (10**-6)) * (temp**5))  + ((5.231511472059040 * (10**-4)) * (temp**4)) - (0.1284860695438150 * (temp**3)) + (18.23595112794600 * (temp**2)) - (1498.203540677550*temp) + 60313.60568037830)/390.625)
        d.analogWrite(self.channel, digValue)
        self.value = digValue
        print digValue

LCT     = DigPot(0, 0)
DGT     = DigPot(1, 0)
DLWT    = DigPot(2, 0)
SCT     = DigPot(3, 0)



