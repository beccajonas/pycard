from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game import Game
    from card import Card
    from hand import Hand

import ipdb
import traceback

class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        #! self.hand: list[Card] = []
        self.hand: Hand = Hand([])
        self.games: list[Game] = []
        # above: name, hand, games are all attributes of self

    @property
    def name(self) -> str:
        return self._name
    
    

    @name.setter
    def name(self, name) -> None:
        '''
        The name property setter enforces a length of at least 1
        '''
        if len(name) < 1:
            raise ValueError("player's name must have at least one character")
        self._name = name

    #! @property
    #! def has_card(self) -> bool:
    #!    return len(self.hand) > 0

    @property
    def win_rate(self) -> float:
        '''
        The win rate is the number of games won divided by the total number of games played
        '''
        games_played: int = len(self.games)
        won_games = []
        for game in self.games:
            if game.winner == self:
                won_games.append(game)

        game_rate = (len(won_games) / games_played) * 100
        return f"{round(game_rate, 1)} %"

    #! def play_card(self) -> Card:
    #!     if not self.has_card:
    #!         raise ValueError('cannot play card from empty hand')
    #!     return self.hand.pop()

    def name_input(self):
        input(self.name)
        print(self.name)
