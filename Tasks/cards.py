import random

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']
allCards = []

for i in figures:
    for j in colors:
        allCards.append(i + " " + j)

random.shuffle(allCards)

player_1 = []
player_2 = []
max = len(allCards)

for card in range(max):
    if card % 2 == 0:
        player_1.append(allCards[card])
    if card % 2 != 0:
        player_2.append(allCards[card])

print("Cards for player1 : ",player_1,"\nCards for player2 : ",player_2)

