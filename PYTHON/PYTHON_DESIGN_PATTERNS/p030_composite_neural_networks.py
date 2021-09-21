from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):
    def connect_to(self, other):
        if self == other:
            return
        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)


class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __str__(self):
        return f"{self.name} - {len(self.inputs)} - {len(self.outputs)}"

    def __iter__(self):
        yield self


class NeuronLayer(list, Connectable):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        for x in range(count):
            self.append(Neuron(f"{name}-{x}"))

    def __str__(self):
        return f"{self.name} - {len(self)}"


if __name__ == "__main__":
    n1 = Neuron("n1")
    n2 = Neuron("n2")
    layer1 = NeuronLayer("l1", 3)
    layer2 = NeuronLayer("l2", 4)
    n1.connect_to(n2)
    n1.connect_to(layer1)
    layer1.connect_to(n2)
    layer1.connect_to(layer2)
    print(n1)
    print(n2)
    print(layer1)
    print(layer2)
