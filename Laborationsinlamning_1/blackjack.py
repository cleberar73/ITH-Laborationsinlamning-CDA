#Importing useful models
import gamefunc as gf
from random import shuffle

playerSet = []

class Deck:
    def __init__(self, deck):
        self.deck = deck

class Player:
    def __init__(self, deck, playername, playercards, playerpoints):
        self.playername = playername
        self.playercards = playercards
        self.playerpoints = playerpoints
        self.deck = deck

class Game(Player, Deck):
    #__init__ for the GAME with 5 arguments
    def __init__(self, deck, playername, playercards, playerpoints):
        print(f"\n{playername} has card(s)")
        
        #__init__ for the Player and others with  also arguments
        super().__init__(deck, playername, playercards, playerpoints)
        self.playername = playername
        self.playerpoints = playerpoints
        self.deck = deck.deck
        dealedcards = gf.deal_player_cards(self.deck)
        self.playercards = gf.pop_cards(dealedcards)
        
        #Show cards for the player. Only one from the computer
        if playername == "Computer":
            print(f"Card(s): [{self.playercards[0]}]")
        else:
            print(f"Cards:", self.playercards)
            print(f"Total points:", sum(self.playercards))
    
ds = Deck
deckset = gf.create_deck()
deckset = ds(deckset)

gf.create_friendly_menu()
game = Game
playergame = game(deckset,"Player", playerSet ,0)
computergame = game(deckset,"Computer", playerSet,0)
gf.hit_card(playergame.playercards,computergame.playercards)

# print(f"Playergame Deck", playergame.deck)
# print(f"\nPlayergame Playercards", playergame.playercards)
# print(Game.mro())
