import sqlite3 as sql
from os.path import exists
from src.settings import DB_DIR, ABS_DIR
from src.table import Table
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
       
    def __repr__(self):
        #Represent Deck() class as a str
        pass
    
    def selectDeck(self):
        #Select deck from sql database
        pass
    
    def viewDeck(self):
        #begin iterating cards in deck
        conn = sql.connect(f'{DB_DIR}{self.db_name}')
        curs = conn.cursor()
        cards = curs.execute(f"""
        SELECT * FROM {self.name}""").fetchall()
        conn.close()
        return cards

    def makeCard(self, front, back):
        #Add card to deck

        #Check if deck is in database
        conn = sql.connect(f'{DB_DIR}{self.db_name}')
        curs = conn.cursor()
        curs.execute(f"""
        INSERT INTO {self.name}(front, back) VALUES(\'{front}\', \'{back}\')
        """)
        conn.commit()
        conn.close()

    def removeCard(self, pk):
        #remove card based on primary key
        pass
