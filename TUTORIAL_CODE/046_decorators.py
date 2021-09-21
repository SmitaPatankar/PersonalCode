'''
decorator takes other function
does processing on the function
returns or replaces it with other function
'''

@decorate
def target():
    print('running target()')

'''
same as

def target():
    print('running target()')
target = decorate(target)
'''

def deco(func):
     def inner():
         print('running inner()')
     return inner

@deco
 def target():
     print('running target()')

target()
# running inner()
target
# <function deco.<locals>.inner at 0x10063b598>

# decorators are executed immediately when a module is loaded

import registration

# running register(<function f1 at 0x10063b1e0>)
# running register(<function f2 at 0x10063b268>)

registration.registry

# [<function f1 at 0x10063b1e0>, <function f2 at 0x10063b268>]

# A real decorator is usually defined in one module and applied to functions in other modules.

# In practice, most decorators define an inner function and return it.

promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):
    """Select best discount available
    """
    return max(promo(order) for promo in promos)