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
        return self.name
    
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
        conn = sql.connect(f'{DB_DIR}{self.db_name}')
        curs = conn.cursor()
        curs.execute(f"""
        INSERT INTO {self.name}(front, back) VALUES(\'{front}\', \'{back}\')
        """)
        conn.commit()
        curs.close()
        conn.close()

    def deleteCard(self, pk):
        #remove card based on primary key
        conn = sql.connect(f'{DB_DIR}{self.db_name}')
        curs = conn.cursor()
        curs.execute(f"""
        DELETE FROM {self.name} WHERE id={pk}
        """)
        conn.commit()
        curs.close()
        conn.close()

    def deleteDeck(self):
        #delete db
        pass