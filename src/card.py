
from __future__ import annotations
import ipdb

class Card:
    def __init__(self, suit: str, value: int):
       self.suit = suit
       self.value = value 
    #    self.name = convert_value(value)

    def convert_value(self, value):
        card_values = {
            1: "Ace", 2: "Two", 3: "Three", 4: "Four",
            5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten", 11: "Jack", 12: "Queen", 13: "King"
        }
        self._name = card_values.get(value)
        if value not in card_values.keys():
            return self._name
            
    @property
    def suit(self) -> str:
        return self._suit

    @suit.setter
    def suit(self, suit: str) -> None:
        '''
        The suit property setter enforces that the parameter is in the 
        set of suit letters.
        '''
        if suit not in {'Spades', 'Diamonds', 'Clubs', 'Hearts'}:
            raise ValueError("Suit must be 'Spades', 'Diamonds', 'Clubs', 'Hearts'")
        self._suit = suit
        
    @property
    # above: decorator (@) - takes the function below and adds functionality to it - for 
    # a specific type of method 
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, value: int) -> None:
        '''
        The value property setter enforces that the parameter is a legal card value
        '''
        if value < 1 or value > 13:
            raise ValueError("card value must be between 1 and 13, inclusive") 
        self._value = value 
    

    def beats(self, card: Card) -> bool:
        '''
        The current card (i.e. self) beats the challenging card if the value 
        is higher. If the values are the same, we check the suit and the 
        letter that is higher alphabetically wins (so _S_pades beats _C_lubs)
        '''
        if self.value == card.value:
            return self.suit > card.suit
        return self.value > card.value
