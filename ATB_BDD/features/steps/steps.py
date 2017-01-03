from behave import given, when, then
from pinClasses import *
from digPotClass import *
from initialSetup import *
from wait import *
from time import sleep


@given('Initial Conditions')
def step_impl(context):

    for row in context.table:
        TableInfo.addCondition(varParameter=eval(row['Parameter']), varState=row['State'])

    for x in range (0,len(TableInfo.parameter)):
        p = TableInfo.parameter[x]
        s = TableInfo.state[x]
           
        if s == 'ON':
            p.on()

        elif p == WAIT:
            sec = float(s)
            WAIT.wait(sec)
            
        else:
            try:
                value = float(s)
                p.setDigValue(value)
            except ValueError:
                p.off()
    

@when('Conditions change')
def step_impl(context):

    TableInfo.parameter = []
    TableInfo.state = []
    
    for row in context.table:
        TableInfo.addCondition(varParameter=eval(row['Parameter']), varState=row['State'])

    for x in range (0,len(TableInfo.parameter)):
        p = TableInfo.parameter[x]
        s = TableInfo.state[x]
           
        if s == 'ON':
            p.on()

        elif p == WAIT:
            sec = float(s)
            WAIT.wait(sec)
            
        else:
            try:
                value = float(s)
                p.setDigValue(value)
            except ValueError:
                p.off()


@then('Check final conditions')
def step_impl(context):
    assert (R.value == 1)
