from clip_annot import clip

clip.__annotations__

# {'text': <class 'str'>, 'max_len': 'int > 0', 'return': <class 'str'>}

from clip_annot import clip
from inspect import signature
sig = signature(clip)
sig.return_annotation
# <class 'str'>
for param in sig.parameters.values():
     note = repr(param.annotation).ljust(13)
     print(note, ':', param.name, '=', param.default)
# <class 'str'> : text = <class 'inspect._empty'>
# 'int > 0'     : max_len = 80

