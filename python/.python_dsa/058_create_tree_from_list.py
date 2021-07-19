class Node:
    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = "----" * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addchild(self, node):
        self.children.append(node)

drinks = Node("drinks", [])
cold = Node("cold", [])
hot = Node("hot", [])
pepsi = Node("pepsi", [])
coke = Node("coke", [])
tea = Node("tea", [])
coffee = Node("pepsi", [])
cold.addchild(pepsi)
cold.addchild(coke)
hot.addchild(tea)
hot.addchild(coffee)
drinks.addchild(cold)
drinks.addchild(hot)
print(drinks)
print(cold)
