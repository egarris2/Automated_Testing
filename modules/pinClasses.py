#import nanpy serial library for arduino. Information found at https://nanpy.github.io/
from nanpy import (ArduinoApi, SerialManager)
from nanpy.MCP41xxx import MCP41xxx

from time import sleep

#setup serial communication with Arduino
connection = SerialManager('COM4')
a = ArduinoApi(connection=connection)

#some initial pin settings to allow for status LEDs and non floating pins
a.pinMode(28, a.OUTPUT)
a.pinMode(29, a.OUTPUT)
a.pinMode(48, a.INPUT_PULLUP)
a.pinMode(50, a.INPUT_PULLUP)
a.pinMode(47, a.INPUT_PULLUP)
a.pinMode(49, a.INPUT_PULLUP)

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
        a.digitalWrite(29, a.HIGH)
        sleep(.01)
        a.digitalWrite(29, a.LOW)

    #turns off an OUTPUT pin
    def off(self):
        a.digitalWrite(self.pinNumber, a.LOW)
        self.value = a.LOW
        a.digitalWrite(28, a.HIGH)
        sleep(.01)
        a.digitalWrite(28, a.LOW)

    #monitors pin for a signal and stores the value in self.value if it recieves one
    def readPin(self):
        self.value = a.LOW #sets self.value low at start
        for x in range(0,1000):
            if a.digitalRead(self.pinNumber) == 1:
                self.value = a.HIGH #sets self.value high if signal is recieved
                break

#creating DigitalPinSetup objects for "High Pressure Switch" and "Lockout"
HP = DigitalPin(39, a.OUTPUT, a.HIGH)
LP = DigitalPin(41, a.OUTPUT, a.LOW)
FS = DigitalPin(43, a.OUTPUT, a.LOW)
CO = DigitalPin(45, a.OUTPUT, a.HIGH)

W1 = DigitalPin(38, a.OUTPUT, a.LOW)
Y1 = DigitalPin(40, a.OUTPUT, a.LOW)
O1 = DigitalPin(36, a.OUTPUT, a.LOW)
Y2 = DigitalPin(42, a.OUTPUT, a.LOW)
G  = DigitalPin(44, a.OUTPUT, a.LOW)        ##PINS SWITCHED WITH O1 BECAUSE OF MISLABELED BOARD


L = DigitalPin(24, a.INPUT, a.LOW)
A = DigitalPin(27, a.INPUT, a.LOW)
CC = DigitalPin(22, a.INPUT, a.LOW)
HWG = DigitalPin(23, a.INPUT, a.LOW)
W2 = DigitalPin(25, a.INPUT, a.LOW)
O = DigitalPin(26, a.INPUT, a.LOW)


R = DigitalPin(34, a.OUTPUT, a.HIGH)
red = DigitalPin(28, a.OUTPUT, a.LOW)



