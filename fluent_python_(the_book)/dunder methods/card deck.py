import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = Deck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


class Deck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades clubs diamonds hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, key, value):
        self._cards[key] = value


deck = Deck()

print(len(deck))
print("\n")

print(deck[3])
print("\n")

print(choice(deck))
print("\n")

for card in sorted(deck, key=spades_high):
    print(card)

print("\n")
print(deck[3])

print("\n")
deck[3].rank = 5

print("\n")
print(deck[3])
