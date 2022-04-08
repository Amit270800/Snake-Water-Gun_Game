# Snake-Water-Gun Game
"""
It is a Snake Water Gun game where:
1. Snake beats Water
2. Water beats Gun
3. Gun beats Snake
"""

import random

def swg_game(pc,player1):
    if pc == 'S':
        if player1 == 'G':
            return "player1"
        elif player1 == 'W':
            return "pc"
        else:
            return 0
    elif pc == 'W':
        if player1 == 'S':
            return "player1"
        elif player1 == 'G':
            return "pc"
        else:
            return 0
    elif pc == 'G':
        if player1 == 'W':
            return "player1"
        elif player1 == 'S':
            return "pc"

n = 0
playerwin = 0
pcwin = 0
while(n<10):
    n += 1
    lst = ["S", "W", "G"]
    pc = random.choice(lst)

    print("Enter your choice: \nS for Snake \nW for Water \nG for Gun")
    player = input()
    player1 = player.upper()
    ch = swg_game(pc, player1)

    if ch == "player1":
        print("Round", n, ": Player Win\n")
        playerwin += 1
    elif ch == "pc":
        print("Round", n, ": Computer Win\n")
        pcwin += 1
    else:
        print("Round", n, ": Draw\n")

if playerwin > pcwin:
    print("!!!You Win!!!")
    print("You won", playerwin, "times")
elif playerwin < pcwin:
    print("Computer win, You loose")
    print("Computer wins", pcwin, "times")
else:
    print("Match is draw")