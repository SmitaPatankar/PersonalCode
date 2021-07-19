from behave import *

a = None
b = None
result = None

@given('2 and 3')
def step_impl(context):
    global a
    global b
    a = 2
    b = 3    

@when('we add them')
def step_impl(context):
    global result
    result = a + b

@then('we get 5')
def step_impl(context):
    global result
    assert result == 5
