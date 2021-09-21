"""
objects are created in heap memory
references are created in stack memory
garbage collected when ref count is 0
"""

"""
name
reference
object (class is also an object i.e. container)

del/setting to None or function exiting/program exiting i.e. when object goes out of scope - deletes references
objects with ref count 0 gets deleted

global objects never go out of scope
hence do manually

object holds - type, value, refcount

garbage collection - reference counting(cascading)
overhead for refcount and changes to it
does not detect cyclic references
not thread safe - hence GIL
__del__ is called when ref count reaches 0 - before deletion

garbage collection - generational - stores container objects with refcount > 0 in 3 generations 0(new),1,2(old)
run GC on current and younger generations when threshold is reached - removes cyclic references
promote remaining to next generation

PYTHON container object contains dictionary of names and values
obj.__dict__()

use __slots__ to use tuple instead
class X:
    __slots__ = ('a','b')
import sys
sys.getsizeof(dict())  # 288 bytes
sys.getsizeof(tuple())  # 48 bytes
"""
