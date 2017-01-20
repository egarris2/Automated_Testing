from time import sleep

class Wait():

    def __init__(self):
        print 'nothing'
    
    def wait(self, seconds):
##        for x in range (0, seconds):
##            sleep(1)
##            print x
        sleep(seconds)

WAIT = Wait()
