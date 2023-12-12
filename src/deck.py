from __future__ import annotations
import random
from card import Card

import ipdb
class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []
        self.reset()

    def reset(self) -> None:
        """
        The cards attribute is populated by iterating over every possible suit
        and value in a nested loop to get every combination (in other words,
        the Cartesian product of the two sets)
        """
        self.cards.clear()
        suits: set[str] = {"Hearts", "Diamonds", "Clubs", "Spades"}
        values: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
        for s in suits:
            for v in values:
                self.cards.append(Card(suit=s, value=v))
        self.shuffle()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
        

    @property
    def has_cards(self) -> bool:
        return len(self.cards) > 0
    
    def deal_card(self) -> Card:
        if not self.has_cards:
            raise ValueError("cannot deal from empty deck")
        return self.cards.pop()



