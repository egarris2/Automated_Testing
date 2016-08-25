from behave import *
from lockout import *

@given('Y1 is on')
def step_impl(context):
    context.unit = unit()

@when('condensate overflow is closed')
def step_impl(context):
    context.unit.supplyPower()

@then('ICM sends a lockout signal')
def step_impl(context):
    assert (context.unit.power == 1)
    
