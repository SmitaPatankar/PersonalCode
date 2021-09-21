from operator import mul
from functools import partial
triple = partial(mul, 3)
triple(7)
# 21
list(map(triple, range(1, 10)))
# [3, 6, 9, 12, 15, 18, 21, 24, 27]

import unicodedata, functools
nfc = functools.partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
s1, s2
# ('café', 'café')
s1 == s2
# False
nfc(s1) == nfc(s2)
# True

from tagger import tag
tag
# <function tag at 0x10206d1e0>
from functools import partial
picture = partial(tag, 'img', cls='pic-frame')
picture(src='wumpus.jpeg')
# '<img class="pic-frame" src="wumpus.jpeg" />'
picture
# functools.partial(<function tag at 0x10206d1e0>, 'img', cls='pic-frame')
picture.func
# <function tag at 0x10206d1e0>
picture.args
# ('img',)
picture.keywords
# {'cls': 'pic-frame'}
