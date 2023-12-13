
from game import Game
from player import Player
from deck import Deck
import ipdb

if __name__ == "__main__":
    '''
    Here we'll run simulations of our game playing, then print out the win 
    rate for each player. 
    '''

    ask_num_input = input("How many players do you have?: ")
    ask_num_input ="5"

    num_players = range(int(ask_num_input))
    
    list_of_players = []

    for i in num_players:   
        # username = input(f"Player {i + 1}, enter username: ")
        username = "Becca"
        player = Player(username)
        list_of_players.append(player)
    

    # player1_username = input("Player 1, enter username: ")
    # print("Player 1 username is: " + player1_username)

    # player1 = Player(player1_username)

    # player2_username = input("Player 2, enter username: ")
    # print("Player 2 username is: " + player2_username)

    # player2 = Player(player2_username)

    deck = Deck()
    game = Game(list_of_players, deck=deck)
    game.play()
    # calling play on the game object
    for i in range(0,10):
        deck.reset()
        game = Game(list_of_players, deck)
        game.play()
    # print(f"{player1.name}'s win rate {player1.win_rate}")
    # print(f"{player2.name}'s win rate {player2.win_rate}")

