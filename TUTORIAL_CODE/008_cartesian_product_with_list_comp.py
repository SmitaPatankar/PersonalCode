colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)
# [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'),
#  ('white', 'M'), ('white', 'L')]

for color in colors:
    for size in sizes:
        print((color, size))
# ('black', 'S')
# ('black', 'M')
# ('black', 'L')
# ('white', 'S')
# ('white', 'M')
# ('white', 'L')

tshirts = [(color, size) for size in sizes
                         for color in colors]
print(tshirts)
# [('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'),
#  ('black', 'L'), ('white', 'L')]

# Note how the resulting list is arranged as if the for loops were nested in the same order as they appear in the listcomp.

# similarly

# self._cards = [Card(rank, suit) for suit in self.suits
#                for rank in self.ranks]

