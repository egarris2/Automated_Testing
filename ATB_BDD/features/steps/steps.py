from behave import given, when, then
from pinClasses import *
from digPotClass import *
from initialSetup import *
from time import sleep

@given('Initial Conditions')
def step_impl(context):

    for row in context.table:
        Start.addCondition(varParameter=eval(row['Parameter']), varState=row['State'])

    for x in range (0,12):
        p = Start.parameter[x]
        s = Start.state[x]

            
        if s == 'ON':
            p.on()

        elif s.isdigit():
            s = int(s)
            p.setResistance(s)
            
        else:
            p.off()
    

@when('High pressure goes out of bounds')
def step_impl(context):
    sleep(10)
    pass

@then('HP is open and CC is off')
def step_impl(context):
    pass
