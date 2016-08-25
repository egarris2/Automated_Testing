from nanpy import (ArduinoApi, SerialManager)
from time import sleep

connection = SerialManager('COM8')
a = ArduinoApi(connection=connection)

class DigitalPinSetup:
    pinCount = 0

    def __init__(self, pinNumber, name, direction, value):
        self.pinNumber = pinNumber
        self.name = name
        self.direction = direction
        self.value = value
        DigitalPinSetup.pinCount += 1
        a.pinMode(self.pinNumber, self.direction)

    def displayPinCount(self):
        print "# of pins used is: %d" % DigitalPinSetup.pinCount

    def displayPinInfo(self):
        print "Pin #: ", self.pinNumber, "\nName: ", self.name, "\nDirection: ", self.direction, "\nValue: ", self.value

    def energize(self):
        a.digitalWrite(self.pinNumber, a.HIGH)

Y1 = DigitalPinSetup(22, "Y1", a.OUTPUT, 2)
