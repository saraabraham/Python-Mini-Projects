import sys
import random
from enum import Enum

class game(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3
playagain = True

while playagain:

    print(" ")
    print("Rock Paper Scissors Game")
    print("")
    playerChoice = input("Enter... \n1 for Rock \n2 for Paper \n3 for Scissors\n\n")
    player = int(playerChoice)

    if player < 1 or player > 3:
        sys.exit("Invalid Input")

    computerChoice = random.choice("123")
    computer=int(computerChoice)

    print("\nYou chose the weapon " + str(game(player)).replace("game.","")+".")
    print("Python chose the weapon " + str(game(computer)).replace("game.","")+".")   

    if player == 1 and computer == 3:
        print("\nYou Win! :)")

    elif player == 2 and computer == 1:
        print("\nYou Win! :)")

    elif player == 3 and computer == 2:
        print("\nYou Win! :)")
    elif player == computer :
        print("\nIt\'s a Tie! :|")
    else:
        print("\nPython wins!! :(")
    playagain = input("\nPlay again? \n1.Enter Y for Yes \n2.Enter Q for Quit\n\n")

    if playagain.lower() == 'y':
        playagain = True
    else:
        playagain = False
        sys.exit("\nBye!!\n")






