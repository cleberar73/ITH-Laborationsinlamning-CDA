#Importing useful models
from random import shuffle
from random import randint

deckset = []
playerSet = []
computercards = []

def create_friendly_menu():
    print(f"*********************")
    print(f"WELCOME TO BLACKJACK ")
    print(f"*********************")
    show_player_game()
    print(f"Computer\'s cards", computercards[0])

def show_player_game():
    print(f"Player\'s cards", playerSet)
    print(f"Total points", sum(playerSet))
    if sum(playerSet) > 21: 
        print(f"YOU LOOSE THE GAME...!!!")
        return

def show_computer_game():
    print(f"Computer\'s cards", computercards)
    print(f"Total points", sum(computercards))

#Create the deck
def create_deck():
    cardcount = 1
    for i in range(1,53):
        if i%4 == 0:
            deckset.append(cardcount)
            cardcount += 1
        else:
            if cardcount < 10:
                deckset.append(cardcount)
            else:
                cardcount = 10
                deckset.append(cardcount)

#Shuffle the deck
def shuffle_deck():
    shuffle(deckset)

#Deal the cards to players
def deal_player_cards():
    for i in range(1,3):
        playerSet.append(deckset.pop(0))
        computercards.append(deckset.pop(0))
    print(f"Player\'s cards", playerSet)
    print(f"Computer\'s cards", computercards[0])

def hit_card():
    while True:
        print(f"\n PLAYER MAIN MENU:")
        print(f"(1) Yes one more card!")
        print(f"(2) No no more cards!")
        print(f"(3) Close the GAME!")

        choice = input(f"\n1=Yes - 2=No - 3=Close : ")

        if choice == "1":
            player_hitted()
            show_player_game()
        elif choice == "2":
            computer_hitted()
            show_computer_game()
        elif choice == "3":
            print(f"\nBLACKJACK STOP. Bye bye...!")
            break
        else:
            print(f"Not a valid choice. Try again.")

def player_hitted():
    playerSet.append(deckset.pop(0))

def computer_hitted():
    if sum(computercards) >= 17:
        show_winner()
        return
    else:
        computercards.append(deckset.pop(0))
    if sum(computercards) < 17:
        computer_hitted()
    else:
        show_winner()

def show_winner():
    if sum(computercards) < 17:
        computer_hitted()

    if sum(computercards) == sum(playerSet):
        print(f"There is a tie good GAME...")
        show_computer_game()
        show_player_game()
    elif sum(computercards) > 17 and sum(computercards) <= 21 and sum(computercards) > sum(playerSet):
        print(f"The Computer is BEATING you up....!!!")
        show_computer_game()
        show_player_game()
    elif sum(computercards) < sum(playerSet) and sum(playerSet) < 21 and sum(computercards) < 21:
        print(f"The Player is winner the Great job...!!!")
        show_player_game()
        show_computer_game()
    elif sum(computercards) > 21:
        print(f"The Computer is a LOOSER...!!!")
        print(f"The Player is the winner Great job...!!!")
        show_computer_game()
        show_player_game()

create_deck()
shuffle_deck()
deal_player_cards()
create_friendly_menu()
hit_card()
