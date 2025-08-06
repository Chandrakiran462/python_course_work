# snake and ladder game
import random
import sys
def dice():
    return random.randint(1,6)


player1 = input('Player1 Name: ')
player2 = input('Player2 Name: ')

player1_score = 0
player2_score = 0

win_score = 100

while player1_score < win_score and player2_score < win_score:
    
