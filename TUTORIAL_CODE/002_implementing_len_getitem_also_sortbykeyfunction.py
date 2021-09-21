import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades clubs diamonds hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()
print(len(deck))
# 52
print(deck[5])
# Card(rank='3', suit='clubs')
print(deck[-1])
# Card(rank='A', suit='hearts')
beer_card = Card('7', 'diamonds')
print(beer_card)
# Card(rank='7', suit='diamonds')

print("#########")

from random import choice
print(choice(deck))
# Card(rank='K', suit='clubs')
print(deck[:3])
# [Card(rank='2', suit='spades'), Card(rank='2', suit='clubs'), Card(rank='2', suit='diamonds')]
print(deck[12::13])
# [Card(rank='5', suit='spades'), Card(rank='8', suit='clubs'), Card(rank='J', suit='diamonds'), Card(rank='A', suit='hearts')]
for card in deck:
    print(card)
# Card(rank='2', suit='spades')
# Card(rank='2', suit='clubs')
# ...
print("*****")
for card in reversed(deck):
    print(card)
print("*****")
# Card(rank='A', suit='hearts')
# Card(rank='A', suit='diamonds')
# ...
print(Card('Q', 'hearts') in deck)
# True

print("############")

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
for card in sorted(deck, key=spades_high):
    print(card)
# for each card from deck its calling key function i.e. spades_high and getting return value and end result is as per those
'''
Card(rank='2', suit='clubs')
Card(rank='2', suit='diamonds')
Card(rank='2', suit='hearts')
Card(rank='2', suit='spades')
Card(rank='3', suit='clubs')
Card(rank='3', suit='diamonds')
Card(rank='3', suit='hearts')
...
'''
