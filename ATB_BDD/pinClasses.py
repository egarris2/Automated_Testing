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

    def setPin(self):
        a.pinMode(self.pinNumber,self.direction)
    
    def displayPinCount(self):
        print "# of pins used is: %d" % DigitalPinSetup.pinCount

    def displayPinInfo(self):
        print "Pin #: ", self.pinNumber, "\nName: ", self.name, "\nDirection: ", self.direction, "\nValue: ", self.value

pin22 = DigitalPinSetup(22, "Y1", "OUTPUT", 1)

pin22.setPin()

a.digitalWrite(22, a.HIGH)



