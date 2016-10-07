from behave import given, when, then
from modules.pinClasses import *
from modules.digPotClass import *
from time import sleep
@given('HP is closed and L is off')
def step_impl(context):
    HP.off()
    LP.off()
    FS.off()
    CO.off()
    
    LCT.setResistance(0)
    DGT.setResistance(255)
    DLWT.setResistance(0)
    SCT.setResistance(255)

    W1.off()
    Y1.on()
    O1.on()
    
    L
    A
    CC
    HWG
    W2
    O

    

@when('High pressure goes out of bounds')
def step_impl(context):
    HP.on()
    L.readPin()

@then('HP is open and L is on')
def step_impl(context):
    assert (HP.value == 0)
    assert (L.value == 0)
    assert (CC.value == 0)
    assert (HWG.value == 0)
    assert (A.value == 0)

