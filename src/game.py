from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from deck import Deck
    from player import Player
    from card import Card

import random
from player import Player

class Game:
    def __init__(self, list_of_players: list[str], deck: Deck) -> None:
        #! list_of_players = ['username1', 'username2', 'username3']
        self.length_of_player_list = range(len(list_of_players))
        self.players = {}
    
        for i in self.length_of_player_list:
            username = list_of_players[i]
            self.players[username]= Player(username)
            self.players[username].games.append(self)

        # for username, player in self.players.items():
        #     print(f"Username: {username}, Player: {player}")

        self.deck: Deck = deck
        self.game_over: bool = False
        self.winner: Player | None = None

        # self.player1.games.append(self)
        # self.player2.games.append(self)

    def distribute_cards(self) -> None:
        """
        count from 0 to n, where n is the length of the number of
        cards in the deck. if the number is even, deal a card to
        player one, else deal a card to player 2
        """
        assert len(self.deck.cards) == 52, "Deck was not refreshed"
        leftover_cards = 52
        for i in range(0, len(self.deck.cards)):
            if leftover_cards >= len(self.players):
                username = list(self.players.keys())[i % len(self.players)]
                player = self.players[username]
                player.add_card_to_hand(self.deck.deal_card())
                leftover_cards -= 1

    def play(self) -> None:
        """
        Rules of the game:
        - The cards are distributed to the players
        - A round consists of each player comparing the top
        card of their deck. The player with the higher
        value wins the round and gets a point. If the values
        are the same then the suit is compared and the highest
        by alphabetical order wins.
        - After all cards have been played, the player with
        the higher score wins
        - If there is a draw, a coin is flipped. If heads player
        one wins, if tails player two wins.
        """
        self.distribute_cards()
        
        if self.winner is None:
            for player_name in self.players:
                self.players[player_name].score = 0
            winning_players = []
            #? assert len(self.player1.hand.card_collection) == len(self.player2.hand.card_collection)
        
            for i in self.length_of_player_list:
                username = list(self.players.keys())[i % len(self.players)]
                player = self.players[username]

                while all(player.hand.has_card for player in self.players.values()):
                    highest_card_value = 0
                    player_card: Card = player.hand.play_card()

                    if player_card.value > highest_card_value:
                        highest_card_value = player_card.value
                        winning_players = [player_name]
                    elif player_card.value == highest_card_value:
                        winning_players.append(player_name)

                    max_score = max(player.score for player in self.players.values())
                    winning_players = [player_name for player_name, player in self.players.items() if player.score == max_score]
                    
                    if len(winning_players) == 1:
                        self.winner = self.players[winning_players[0]]
                    else:
                        winner_name = random.choice(winning_players)
                        self.players[winner_name].score += 1

                    

                    # if player_card.beats(player2_card):
                    #     player1_score += 1
                    # elif player2_card.beats(player1_card):
                    #     player2_score += 1

                # if player1_score > player2_score:
                #     self.winner = self.player1
                # elif player2_score > player1_score:
                #     self.winner = self.player2
                # else:
                #     coin = ["HEADS", "TAILS"]
                #     if random.choice(coin) == "HEADS":
                #         self.winner = self.player1
                #     else:
                #         self.winner = self.player2
