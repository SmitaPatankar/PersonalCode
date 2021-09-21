class OldResistor(object):
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms


# above not pythonic

r0 = OldResistor(50e3)
print('Before: %5r' % r0.get_ohms())
r0.set_ohms(10e3)
print('After:  %5r' % r0.get_ohms())

'''
Before: 50000.0
After:  10000.0
'''

r0.set_ohms(r0.get_ohms() + 5e3)


class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


r1 = Resistor(50e3)
r1.ohms = 10e3

r1.ohms += 5e3


# Later, if you decide you need special behavior when an attribute is set,
# you can migrate to the @property decorator and its corresponding setter attribute.

class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


r2 = VoltageResistance(1e3)
print('Before: %5r amps' % r2.current)
r2.voltage = 10
print('After:  %5r amps' % r2.current)

'''
Before:     0 amps
After:   0.01 amps
'''


# Specifying a setter on a property also lets you perform type checking
# and validation on values passed to your class. Here, I define a class that
# ensures all resistance values are above zero ohms:

class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        self._ohms = ohms


r3 = BoundedResistance(1e3)
r3.ohms = 0

# ValueError: 0.000000 ohms must be > 0

BoundedResistance(-5)


# ValueError: -5.000000 ohms must be > 0

# This happens because BoundedResistance.__init__ calls Resistor.__init__,
# which assigns self.ohms = -5. That assignment causes the @ohms.setter method
# from BoundedResistance to be called, immediately running the validation code
# before object construction has completed.

# You can even use @property to make attributes from parent classes immutable.

class FixedResistance(Resistor):
    # ...
    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms


r4 = FixedResistance(1e3)
r4.ohms = 2e3

'''
AttributeError: Can't set attribute
'''


# The biggest shortcoming of @property is that the methods
# for an attribute can only be shared by subclasses. Unrelated classes can’t
# share the same implementation. However,
# Python also supports descriptors that enable reusable property logic
# and many other use cases.

# don’t set other attributes in getter property methods.

class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms

    pass  # ...


# This leads to extremely bizarre behavior.

r7 = MysteriousResistor(10)
r7.current = 0.01
print('Before: %5r' % r7.voltage)
r7.ohms
print('After:  %5r' % r7.voltage)

'''
Before:     0
After:    0.1
'''

# Ensure that @property methods are fast; do slow or complex work using normal methods.
