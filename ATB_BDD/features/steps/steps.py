from behave import given, when, then
from modules.pinClasses import *
from modules.digPotClass import *
from time import sleep
@given('test 1 initial conditions')
def step_impl(context):
    R.on()

    sleep(3)

    HP.off()
    LP.off()
    FS.off()
    CO.off()
    
    LCT.setResistance(235)
    DGT.setResistance(252)
    DLWT.setResistance(235)
    SCT.setResistance(230)

    W1.off()
    Y1.off()
    
    A
    CC
    HWG
    W2
    O

    

@when('High pressure goes out of bounds')
def step_impl(context):
      sleep(5)
      Y1.on()
##    L.readPin()
##    A.readPin()
##    CC.readPin()
##    HWG.readPin()
##    W2.readPin()
##    O.readPin()

@then('HP is open and L is on')
def step_impl(context):
    assert (HP.value == 0)
    assert (L.value == 0)
    assert (CC.value == 0)
    assert (HWG.value == 0)
    assert (A.value == 0)

