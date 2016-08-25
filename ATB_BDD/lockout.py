class dPin:
    pinCount = 0

    def __init__(self, pinNumber, name, direction, value):
        self.pinNumber = pinNumber
        self.name = name
        self.direction = direction
        self.value = value
        dPin.pinCount += 1

    def displayPinCount(self):
        print "# of pins used is: %d" % dPin.pinCount

    def displayPinInfo(self):
        print "Pin #: ", self.pinNumber, "\nName: ", self.name, "\nDirection: ", self.direction, "\nValue: ", self.value

    
pin22 = dPin(22, "Y1", "OUTPUT", 1)
pin22.displayPinInfo()
    
pin22.direction = "INPUT"
pin22.displayPinInfo()

