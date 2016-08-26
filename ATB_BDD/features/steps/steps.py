from behave import given, when, then
from pinClasses import *
from time import sleep

@given('FS is on')
def step_impl(context):
    FS

@when('Flow stops')
def step_impl(context):
    FS.turnOff()
    sleep(3)

@then('FS is off')
def step_impl(context):
    assert (FS.value == 1)

@when('Flow starts again')
def step_impl(context):
    FS.turnOn()

@then('FS is on')
def step_impl(context):
    assert (FS.value == 1)
