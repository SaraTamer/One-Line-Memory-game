# memory line game

import random
import os
import time

# initializing variables
n, i, j, turn = 0, 0, 0, 0
player1_score = 0
player2_score = 0

# the line
line = ['A', "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'A', "B", 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
random.shuffle(line)

# the visible cards
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# display cards


def line_displaying():
    print(cards)


line_displaying()

# game function


def game_play():

    global turn
    global player1_score
    global player2_score

    # check_game_over():
    if player1_score + player2_score == 10:
        if player1_score > player2_score:
            print('The winner is player1')
        elif player2_score > player1_score:
            print('The winner is player2')
        else:
            print('Its tie')

     # handle turns
while player1_score + player2_score != 10:

    turn += 1
    if turn % 2 == 1:
        print('Player1, score:', player1_score)
        i = int(input(' Choose two numbers from 1 to 20. '))
        j = int(input('and '))
    elif turn % 2 == 0:
        print('Player2, score:', player2_score)
        i = int(input(' Choose two numbers from 1 to 20. '))
        j = int(input('and '))

    # game defence
    while i not in range(1, 21):
        i = int(input(' Please, Choose two numbers from 1 to 20. '))
        j = int(input('and '))
    while j not in range(1, 21):
        i = int(input(' Please, Choose two numbers from 1 to 20. '))
        j = int(input('and '))

    while cards[i-1] == '*':
        i = int(input('These cards are already used, Choose another ones'))
        j = int(input('and '))
    while cards[j - 1] == '*':
        i = int(input('These cards are already used, Choose another ones'))
        j = int(input('and '))

    cards[i-1] = line[i-1]
    cards[j-1] = line[j-1]
    print(cards)
    time.sleep(3)
    os.system('cls')

    # check winner
    if line[i-1] == line[j-1]:
        cards[i-1] = cards[j-1] = '*'
        print(cards)
        if turn % 2 == 1:
            player1_score = player1_score + 1
        elif turn % 2 == 0:
            player2_score = player2_score + 1
    else:
        cards[i-1] = i
        cards[j-1] = j
        print(cards)

# calling my game
game_play()
