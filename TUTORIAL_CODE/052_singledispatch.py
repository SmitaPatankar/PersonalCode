import html

def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

htmlize({1, 2, 3})
'<pre>{1, 2, 3}</pre>'
htmlize(abs)
'<pre>&lt;built-in function abs&gt;</pre>'
htmlize('Heimlich & Co.\n- a game')
'<p>Heimlich &amp; Co.<br>\n- a game</p>'
htmlize(42)
'<pre>42 (0x2a)</pre>'
print(htmlize(['alpha', 66, {3, 2, 1}]))
# <ul>
# <li><p>alpha</p></li>
# <li><pre>66 (0x42)</pre></li>
# <li><pre>{1, 2, 3}</pre></li>
# </ul>


# like function overloading in other languages

from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'