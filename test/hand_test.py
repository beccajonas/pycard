import pytest
from src.hand import Hand
from src.card import Card
class TestCard:

    def test_empty_hand_has_no_cards(self):
        hand = Hand()
        assert not hand.has_card 

    def test_has_card_is_true_when_card_added(self):
        hand = Hand()
        card = Card("Hearts", 4)
        hand.card_collection.append(card)
        assert hand.has_card, "card added but has_card was false"

    def test_setting_cards_raises_error(self):
        with pytest.raises(ValueError):
            hand = Hand()
            hand.cards = []

    def test_play_card_raises_error_when_empty_cards(self):
        with pytest.raises(ValueError):
            hand = Hand()
            hand.play_card()

    def test_play_card_when_card_exists(self):
        hand = Hand()
        card = Card("Hearts", 4)
        hand.card_collection.append(card)
        assert card == hand.play_card(), "play card should return the card that was added"
        assert len(hand.cards) == 0, "cards list should be empty"
