from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game
    from card import Card

class Hand:
    def __init__(self):
        self.card_collection = []
    
    @property
    def card_collection(self): 
        return self._card_collection 

    @card_collection.settter
    def card_collection(self, card_collection):
        if hasattr(self, "card_collection"):
            raise AttributeError("instance already has attribute cards")
        self._card_collection = card_collection
        

    @property
    def has_card(self) -> bool:
        return len(self.card_collection) > 0
    
    def play_card(self) -> Card:
        if not self.has_card:
            raise ValueError('cannot play card from empty hand')
        return self.card_collection.pop()
