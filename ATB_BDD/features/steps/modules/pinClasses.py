#import nanpy serial library for arduino. Information found at https://nanpy.github.io/
from nanpy import (ArduinoApi, SerialManager)
from nanpy.MCP41xxx import MCP41xxx

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
        #if the pin is an output, write the starting value to the pin
        if self.direction == a.OUTPUT:
            a.digitalWrite(self.pinNumber, self.value)

    #print pin information
    def displayPinInfo(self):
        print "Pin #: ", self.pinNumber, "\nDirection: ", self.direction, "\nValue: ", self.value

    #turns on an OUTPUT pin
    def on(self):
        a.digitalWrite(self.pinNumber, a.HIGH)
        self.value = a.HIGH

    #turns off an OUTPUT pin
    def off(self):
        a.digitalWrite(self.pinNumber, a.LOW)
        self.value = a.LOW

    #monitors pin for a signal and stores the value in self.value if it recieves one
    def readPin(self):
 #       self.value = a.LOW #sets self.value low at start
        for x in range(0,1000):
            if a.digitalRead(self.pinNumber) == 1:
                self.value = a.HIGH #sets self.value high if signal is recieved
                break

#creating DigitalPinSetup objects for "High Pressure Switch" and "Lockout"
HP = DigitalPin(20, a.OUTPUT, a.LOW)
LP = DigitalPin(22, a.OUTPUT, a.LOW)
FS = DigitalPin(24, a.OUTPUT, a.LOW)
CO = DigitalPin(26, a.OUTPUT, a.LOW)

W1 = DigitalPin(21, a.OUTPUT, a.LOW)
Y1 = DigitalPin(23, a.OUTPUT, a.LOW)
O1 = DigitalPin(25, a.OUTPUT, a.LOW)

L = DigitalPin(5, a.INPUT, a.LOW)
A = DigitalPin(8, a.INPUT, a.LOW)
CC = DigitalPin(3, a.INPUT, a.LOW)
HWG = DigitalPin(4, a.INPUT, a.LOW)
W2 = DigitalPin(6, a.INPUT, a.LOW)
O = DigitalPin(7, a.INPUT, a.LOW)



