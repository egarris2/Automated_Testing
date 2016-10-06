from behave import given, when, then
from pinClasses import *
from digPotClass import *
from time import sleep

@given('HP is closed and L is off')
def step_impl(context):
    HP
    L
    Therm1
    Therm2

@when('High pressure goes out of bounds')
def step_impl(context):
    Therm1.setResistance(255) #Therm1 goes to low temp
    Therm2.setResistance(255) #Therm2 goes to High Temp
    HP.turnOff()
    sleep(30)
    L.readPin()

@then('HP is open and L is on')
def step_impl(context):
    assert (HP.value == 0)
    assert (L.value == 1)
    assert (Therm1.value == 255)
    assert (Therm2.value == 255)

