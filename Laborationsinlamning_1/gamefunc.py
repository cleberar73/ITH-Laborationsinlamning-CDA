from random import shuffle

deckset = []
playerSet = []

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
    shuffle_deck()
    return deckset

def shuffle_deck():
    shuffle(deckset)

def create_friendly_menu():
    print(f"*********************")
    print(f"WELCOME TO BLACKJACK ")
    print(f"*********************")
    print(f"The GAME has STARTED!")

def deal_player_cards(deckset):
    for i in range(1,3):
        playerSet.append(deckset.pop(0))
    return playerSet

def pop_cards(set):
    tempset = []
    for i in range(1,3):
        tempset.append(set.pop(0))
    return tempset

def hit_card(playercards, computercards):
    while True:
        print(f"\n PLAYER MAIN MENU:")
        print(f"(1) Yes one more card!")
        print(f"(2) No no more cards!")
        print(f"(3) Close the GAME!")

        choice = input(f"1=Yes - 2=No - 3=Close : ")

        if choice == "1":
            player_hitted(playercards)
            show_player_game(playercards)
        elif choice == "2":
            computer_hitted(playercards, computercards)
            show_computer_game(computercards)
        elif choice == "3":
            print(f"\nBLACKJACK STOPS. Bye bye...!!!")
            break
        else:
            print(f"Not a valid choice. Try again.")

def player_hitted(playercards):
    playercards.append(deckset.pop(0))

def computer_hitted(playercards, computercards):
    if sum(computercards) >= 17:
        show_winner(playercards, computercards)
        return
    else:
        computercards.append(deckset.pop(0))
    if sum(computercards) < 17:
        computer_hitted(playercards, computercards)
    else:
        show_winner(playercards, computercards)

def show_player_game(playercards):
    print(f"Player\'s cards", playercards)
    print(f"Total points", sum(playercards))
    
    if sum(playercards) > 21: 
        print(f"YOU LOOSE THE GAME...!!!")
        # return

def show_computer_game(computercards):
    print(f"Computer\'s cards", computercards)
    print(f"Total points", sum(computercards))

def show_winner(playercards,computercards):
    if sum(computercards) < 17:
        computer_hitted()
    if sum(computercards) == sum(playercards):
        print(f"There is a tie good GAME...")
        show_computer_game(computercards)
        show_player_game(playercards)
    elif sum(computercards) > 17 and sum(computercards) <= 21 and sum(computercards) > sum(playercards):
        print(f"The Computer is BEATING you up....!!!")
        show_computer_game(computercards)
        show_player_game(playercards)
    elif sum(computercards) < sum(playercards) and sum(playercards) < 21 and sum(computercards) < 21:
        print(f"The Player is winner the Great job...!!!")
        show_player_game(playercards)
        show_computer_game(computercards)
    elif sum(computercards) > 21:
        print(f"The Computer is a LOOSER...!!!")
        print(f"The Player is the winner Great job...!!!")
        show_computer_game(computercards)
        show_player_game(playercards)

if __name__ == '__main__':
    print(f"Greetings from my blackjack game functions...!!!")
