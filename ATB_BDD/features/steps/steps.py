from behave import given, when, then
from pinClasses import *
from time import sleep

@given('HP is closed and L is off')
def step_impl(context):
    HP
    L

@when('High pressure goes out of bounds')
def step_impl(context):
    HP.turnOff()
    sleep(30)
    L.readPin()

@then('HP is open and L is on')
def step_impl(context):
    assert (HP.value == 0)
    assert (L.value == 1)
