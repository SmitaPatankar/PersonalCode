# tuple supports all list methods that do not involve adding or removing items,
# with one exception—tuple lacks the __reversed__ method.
# reversed(my_tuple) works without it

'''
list and tuple both

s.__add__(s2) - s+s2
s.__contains__(e) - e in s
s.__getitem__(p) - s[p]
s.count(e)
s.index(e)
s.__iter__()
s.__len__() - len(s)
s.__mul__(n) - s * n—repeated concatenation
s.__rmul__(n) - n * s—reversed repeated concatenation**

only list
s.__iadd__(s2) - s += s2
s.append(e)
s.clear()
s.copy()
s.__delitem__(p)
s.extend(it)
s.__getnewargs__() - Support for optimized serialization with pickle
s.insert(p, e)
s.__imul__(n) - s *= n
s.pop([p])
s.remove(e)
s.reverse()
s.__reversed__()
s.__setitem__(p, e) - s[p] = e
s.sort([key], [reverse])
'''
