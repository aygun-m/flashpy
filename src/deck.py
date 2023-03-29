import sqlite3 as sql
from os.path import exists
from src.settings import DB_DIR
from os import remove, listdir

class Table:

    def __init__(self):
        
        #obtain list of all databases/decks

        self.db_dir = DB_DIR

        self.allDecks = listdir(self.db_dir)

    def decks(self):

        return self.allDecks

class Deck(Table):
    
    def __init__(self, name):
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
        self.allDecks = d.decks()
        self.__updateDeckStatus()
        
    def __repr__(self):
        #Represent Deck() class as a str
        return self.name
    
    def printDeck(self):
        #begin iterating cards in deck
        conn = sql.connect(f'{DB_DIR}{self.db_name}')
        curs = conn.cursor()
        cards = curs.execute(f"""
        SELECT * FROM {self.name}""").fetchall()
        conn.close()
        print(cards)

    def addCard(self, front, back):
        #Add card to deck
        conn = sql.connect(f'{DB_DIR}{self.db_name}')
        curs = conn.cursor()
        curs.execute(f"""       
        INSERT INTO {self.name}(front, back) VALUES(\'{front}\', \'{back}\')
        """)
        self.__updateDeckStatus()
        conn.commit()
        curs.close()
        conn.close()

    def remCard(self, pk):
        #remove card based on primary key
        conn = sql.connect(f'{DB_DIR}{self.db_name}')
        curs = conn.cursor()
        curs.execute(f"""DELETE FROM {self.name} WHERE id={pk}""")
        conn.commit()        
        self.__updateDeckStatus()
        curs.close()
        conn.close()

    def remDeck(self):
        #delete db
        deckPath = f'{DB_DIR}/{self.db_name}'
        remove(deckPath)
        
    def __updateDeckStatus(self):
        #private method to update deck constructor variable self.deck
        conn = sql.connect(f'{DB_DIR}{self.db_name}')
        curs = conn.cursor()
        deck = curs.execute(f"""SELECT * FROM {self.name}""").fetchall()
        self.deck = deck
        curs.close()
        conn.close()

