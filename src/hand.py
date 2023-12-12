from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game
    from card import Card

class Hand:
    def __init__(self):
        self.card_collection = []

    @property
    def has_card(self) -> bool:
        return len(self.card_collection) > 0
    
    def play_card(self) -> Card:
        if not self.has_card:
            raise ValueError('cannot play card from empty hand')
        return self.card_collection.pop()
