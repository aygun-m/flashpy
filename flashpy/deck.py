import sqlite3 as sql
from os.path import exists
from colorama import Fore
from flashpy.settings import DB_DIR
from os import remove, listdir, system

class Table:

    def __init__(self):
        
        #obtain list of all databases/decks

        self.db_dir = DB_DIR

        self.allDecks = listdir(self.db_dir)

    def __repr__(self):

        #list table

        return str(self.allDecks)

class Deck(Table):
    
    def __init__(self, name):
        if '-' in name:
            raise Exception("The deck name cannot contain a hyphen due to SQLite3 database compatibility issues")
        try:
            #Constructor for Deck() class
            if isinstance(name, str): 
                self.name = name
                self.db_name = f'{self.name}.db'
                if not exists(f"{DB_DIR}/{self.db_name}"):
                    conn = sql.connect(f'{DB_DIR}{self.db_name}')
                    curs = conn.cursor()
                    curs.execute(f"""
                        CREATE TABLE IF NOT EXISTS {self.name} 
                    (
                        id INTEGER PRIMARY KEY, 
                        front TEXT,
                        back TEXT
                    )
                    """)
                    conn.close()
                self.init = True
            else: raise TypeError("Inappropriate argument type for Deck() class")
            d = Table()
            self.allDecks = d.allDecks
            self.__updateDeckStatus()
        except Exception:
            pass
        
    def __repr__(self):
        #Represent Deck() class as a str
        return self.name
    
    def getDeck(self):
        #begin iterating cards in deck
        conn = sql.connect(f'{DB_DIR}{self.db_name}')
        curs = conn.cursor()
        cards = curs.execute(f"""
        SELECT * FROM {self.name}""").fetchall()
        conn.close()
        return (cards)

    def addCard(self, front, back):
        #Add card to deck
        front, back = str(front), str(back)
        conn = sql.connect(f'{DB_DIR}/{self.db_name}')
        curs = conn.cursor()
        curs.execute(f"""INSERT INTO {self.name}(front, back) VALUES(\"{front}\", \"{back}\")""")
        conn.commit()
        curs.close()
        conn.close()
        self.__updateDeckStatus()

    def pasteDeck(self):
        print(f"DECK NAME : {self.name}")
        for i, x in enumerate(self.deck):
            if i == 0: print("======CARD=1======")
            else: print(f"======CARD={x[0]}======")
            print(f"{x}")
        print("=======END=OF=DECK=======")

    def shuffle(self):
        #Plays through the cards
        b = Fore.BLUE
        w = Fore.WHITE
        for x in self.deck:
            system("clear")
            print(f"{b}Question > {w}{x[1]}")
            input(f"{b}Press Enter to Continue > ")
            system("clear")
            print(f"{b}Answer > {w}{x[2]}")
            input(f"{b}Press Enter to Continue > ")
        print(f"{w}You have completed this deck")

    def delCard(self, pk):
        #remove card based on primary key
        conn = sql.connect(f'{DB_DIR}{self.db_name}')
        curs = conn.cursor()
        curs.execute(f"""DELETE FROM {self.name} WHERE id={pk}""")
        conn.commit()        
        self.__updateDeckStatus()
        curs.close()
        conn.close()

    def delDeck(self, name=None):
        #delete db
        if name == None:
            deckPath = f'{DB_DIR}/{self.db_name}'
            remove(deckPath)
        else:
            remove(f'{DB_DIR}/{name}')
        
    def __updateDeckStatus(self):
        #private method to update deck constructor variable self.deck
        conn = sql.connect(f'{DB_DIR}{self.db_name}')
        curs = conn.cursor()
        deck = curs.execute(f"""SELECT * FROM {self.name}""").fetchall()
        self.deck = deck
        curs.close()
        conn.close()

