from behave import given, when, then
from pinClasses import *
from digPotClass import *
from time import sleep

@given('test 1 initial conditions')
def step_impl(context):
    R.on()                      ##Turn on Power to ICM
    sleep(1)                    

    ##Set initial conditions for Fault Sensors
    HP.off()
    LP.off()
    FS.off()
    CO.off()

    ##Set initial conditions for "Thermistor Values"
    LCT.setResistance(235)
    DGT.setResistance(252)
    DLWT.setResistance(235)
    SCT.setResistance(225)

    ##Set initial conditions for "Calls" to lockout board
    W1.off()
    Y1.off()
    O1.off()

@when('High pressure goes out of bounds')
def step_impl(context):
    ##Wait for board to turn on before sending calls
    Y1.on()
    sleep(20)
    HP.on()
    ##check values of Lockout Outputs
    L.readPin()                 
    A.readPin()
    CC.readPin()
    
##    HWG.readPin()
##    W2.readPin()
##    O.readPin()

@then('HP is open and CC is off')
def step_impl(context):
    assert (HP.value == 1)
    assert (L.value == 0)
    assert (CC.value == 0)
    assert (HWG.value == 0)

@when ('30 seconds pass')
def step_impl(context):
    sleep (30)
    L.readPin ()
    A.readPin()
    CC.readPin()

@then('HP is open and CC and A are off. L is on')
def step_impl(context):
    assert (HP.value == 1)
    assert (L.value == 1)
    assert (CC.value == 0)
    assert (HWG.value == 0)
    assert (A.value == 0)



