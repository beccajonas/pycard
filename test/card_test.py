import pytest
from src.card import Card
class TestCard:

    def test_suit_must_be_valid(self):
        with pytest.raises(ValueError):
            c = Card("Not a Suit", 1)

    def test_higher_value_beats_lower_value(self):
        high_card = Card("Hearts", 4)
        low_card = Card("Hearts", 2)
        assert high_card.beats(low_card), "2 of hearts should beat 2 of hearts"
    
    def test_higher_suit_beats_lower_suit(self):
        low_suit = Card("Clubs", 5)
        high_suit = Card("Spades", 4)
        assert high_suit.beats(low_suit), "Clubs should beat spades when values are the same"
    
