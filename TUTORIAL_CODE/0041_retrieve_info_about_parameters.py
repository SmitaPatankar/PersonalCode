import bobo

@bobo.query('/')
def hello(person):
    return 'Hello %s!' % person
# curl -i http://localhost:8080/ error
# curl -i http://localhost:8080/?person=Jim fine

# Within a function object, the __defaults__ attribute holds a tuple with the default values of positional and keyword arguments.

# The defaults for keyword-only arguments appear in __kwdefaults__. The names of the arguments, however, are found within the __code__ attribute, which is a reference to a code object with many attributes of its own.



from clip import clip
clip.__defaults__
# (80,)
# clip.__code__
# <code object clip at 0x...>
clip.__code__.co_varnames
# ('text', 'max_len', 'end', 'space_before', 'space_after')
clip.__code__.co_argcount
# 2

from clip import clip
from inspect import signature
sig = signature(clip)
sig
# <inspect.Signature object at 0x...>
# str(sig)
'(text, max_len=80)'
for name, param in sig.parameters.items():
     print(param.kind, ':', name, '=', param.default)
# POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'>
# POSITIONAL_OR_KEYWORD : max_len = 80

'''
POSITIONAL_OR_KEYWORD
VAR_POSITIONAL
VAR_KEYWORD
KEYWORD_ONLY
POSITIONAL_ONLY
'''

# bind to check before calling

import inspect
sig = inspect.signature(tag)
my_tag = {'name': 'img', 'title': 'Sunset Boulevard',
           'src': 'sunset.jpg', 'cls': 'framed'}
bound_args = sig.bind(**my_tag)
bound_args
# <inspect.BoundArguments object at 0x...>
for name, value in bound_args.arguments.items():
     print(name, '=', value)

# name = img
# cls = framed
# attrs = {'title': 'Sunset Boulevard', 'src': 'sunset.jpg'}
del my_tag['name']

bound_args = sig.bind(**my_tag)
# Traceback (most recent call last):
#   ...
# TypeError: 'name' parameter lacking default value

# tools and frameworks can validate like this

