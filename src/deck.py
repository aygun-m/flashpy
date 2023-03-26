import sqlite3 as sql
from table import Table
class Deck(Table):
    
    def __init__(self):
        #Constructor for Deck() class
        pass

    def __repr__(self):
        #Represent Deck() class as a str
        pass
    
    def selectDeck(self):
        #Select deck from sql database
        pass
    
    def makeCard(self, front, back):
        #Add card to deck
        conn = sql.connect()