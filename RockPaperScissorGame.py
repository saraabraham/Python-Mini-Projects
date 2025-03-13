import sys
import random
from enum import Enum

class game(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3

print(" ")
print("Rock Paper Scissors Game")
print("")
playerChoice = input("Enter... \n1 for Rock \n2 for Paper \n3 for Scissors\n\n")
player = int(playerChoice)

if player < 1 or player > 3:
    sys.exit("Invalid Input")

computerChoice = random.choice("123")
computer=int(computerChoice)

print("")
print("You chose the weapon " + str(game(player)).replace("game.","")+".")
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





