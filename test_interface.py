from flashpy.deck import Deck
from os import system

"""
This file contains a command line interface in order to interact with the local flashpy database
"""

l = ["Add Card", "Remove Card", "Shuffle Deck", "List Cards", "Exit"]

def main():
    system("clear")
    print("===Flashpy=CLI===")
    deckname = str(input("Deck Name > "))
    deck = Deck(deckname)
    while True:
        for i, x in enumerate(l):print(f"{i + 1} - {x}")
        inp = input(" > ")
        if inp == '1':
            f = input("Enter Front > ")
            b = input("Enter Back > ")
            deck.addCard(f, b)
            system("clear")
            print("Card was added to deck")
        elif inp == '2':
            pk = int(input("Enter PK of Card > "))
            deck.delCard(pk)
            system("clear")
            print("Card was removed from deck")
            #delete card in deck
        elif inp == '3':
            deck.shuffle()
            system("clear")
            #play the game
        elif inp == '4':
            deck.pasteDeck()
        elif inp == '5':
            print("Exiting Flashpy...")
            exit()

if __name__ == "__main__":
    main()