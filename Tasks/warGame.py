colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []
for i in colors:
    for j in figures:
        aCard = j.copy()
        aCard['Color'] = i
        allCards.append(aCard)

import random

random.shuffle(allCards)

player1 = []
player2 = []

for card in range(len(allCards)):
    if card % 2 == 0:
        player1.append(allCards[card])
    else:
        if card % 2 != 0:
            player2.append(allCards[card])

print('-------PLAYER 1--------')
print(player1)

print('-------PLAYER 1--------')
print(player2)

print("\n")

#while len(player1) > 0 and len(player2) > 0:
for players in range(12):
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    if card1['Power'] == card2['Power']:
        player1.append(card1)
        player2.append(card2)
        print('=EQUAL \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')

    elif card1['Power'] > card2['Power']:
        player1.append(card1)
        player1.append(card2)
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')

    else:
        player2.append(card1)
        player2.append(card2)
        print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"])+ len(player1)*'*')


if len(player1) > len(player2):
    print('PLAYER 2 WON!!!!')
else:
    print('PLAYER 1 WON!!!!')
