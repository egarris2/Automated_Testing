from pinClasses import DigitalPin

print " the pin count is %d\n" % DigitalPin.pinCount
pin22 = DigitalPin(22, "Y1", "INPUT", 1)

pin22.displayPinInfo()
print " the pin count is %d\n" % DigitalPin.pinCount
