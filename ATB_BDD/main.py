from pinClasses import DigitalPin
from pinClasses import FS, L
from time import sleep

#counter for exiting while loop
count = 0

#main loop that runs as long as there is no lockout signal
while (L.value==0):
    print "working"

    count += 1

    #throws a flow switch fault after 30 "loops"
    if (count == 30):
        FS.turnOn()

    #checks for a lockout signal
    L.readPin()

    sleep(.2)
    
    if (count == 100):
        break

print "**Locked out due to Flow Switch fault**"

    
    

