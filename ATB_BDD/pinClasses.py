#import serial library for arduino
from nanpy import (ArduinoApi, SerialManager)

from time import sleep

#setup serial communication with Arduino
connection = SerialManager('COM8')
a = ArduinoApi(connection=connection)

#creating class for digital pins
class DigitalPin():

    #setting attributes for pins
    def __init__(self, pinNumber, direction, value):
        self.pinNumber = pinNumber
        self.direction = direction
        self.value = value
        #sets the actual pin upon initialization of object
        a.pinMode(self.pinNumber, self.direction)

    #print pin information
    def displayPinInfo(self):
        print "Pin #: ", self.pinNumber, "\nDirection: ", self.direction, "\nValue: ", self.value

    #turns on an OUTPUT pin
    def turnOn(self):
        a.digitalWrite(self.pinNumber, a.HIGH)
        self.value = a.HIGH

    #turns off an OUTPUT pin
    def turnOff(self):
        a.digitalWrite(self.pinNumber, a.LOW)
        self.value = a.LOW

    #reads whether an INPUT pin is reading 1 or zero and prints
    def readPin(self):
        self.value = a.digitalRead(self.pinNumber)
        print self.value

#creating DigitalPinSetup object for "flow switch"
FS = DigitalPin(22, a.OUTPUT, a.HIGH)
L = DigitalPin(26, a.INPUT, a.LOW)

