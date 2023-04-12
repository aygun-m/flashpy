# flashpy
A learning and memorisation tool that uses the active-recall method of memorisation which is an evidence based technique to achieve the highest scores on exams and other academic structures.

## installation
perform these commands one after the other in order to install flashpy
```linux
git clone https://github.com/aygun-m/flashpy.git
```
```
cd flashpy
```
```
pip install .
```

## usage
```python
from flashpy.deck import Deck

deck = Deck("MyDeck") # Creates a deck with the name MyDeck, if not already exists. Connects to deck with name if exists.

deck.addCard("front card", "back card")

deck.shuffle() # Command Line Interface function to shuffle through cards

```
