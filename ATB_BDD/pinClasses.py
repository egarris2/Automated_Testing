#import nanpy serial library for arduino. Information found at https://nanpy.github.io/
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
        #if the pin is an output, write the starting value to the pin
        if self.direction == a.OUTPUT:
            a.digitalWrite(self.pinNumber, self.value)

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

    #monitors pin for a signal and stores the value in self.value if it recieves one
    def readPin(self):
        self.value = a.LOW #sets self.value low at start
        for x in range(0,1000):
            if a.digitalRead(self.pinNumber) == 1:
                self.value = a.HIGH #sets self.value high if signal is recieved

#creating DigitalPinSetup objects for "High Pressure Switch" and "Lockout"
HP = DigitalPin(22, a.OUTPUT, a.HIGH)
L = DigitalPin(26, a.INPUT, a.LOW)

"""print L.value
HP.turnOff()
sleep(.5)
L.readPin()
sleep(.5)
print L.value"""



