import sys
import random
from enum import Enum

class game(Enum):
    ROCK=1
    PAPER=2
    SCISSORS=3
game_count = 1
def rpsgame():
    print("\nRock Paper Scissors Game 🪨 🗞️ ✂️")
    playerChoice = input("\nEnter... \n1 for Rock  🪨 \n2 for Paper  🗞️ \n3 for Scissors ✂️ \n\n")
    if playerChoice not in ["1","2","3"]:
        print("Invalid input: Please enter 1,2,3")
        return rpsgame()
    
    player = int(playerChoice)
    computerChoice = random.choice("123")
    computer=int(computerChoice)

    print("\nYou chose the weapon " + str(game(player)).replace("game.","").lower()+".")
    print("Python chose the weapon " + str(game(computer)).replace("game.","").lower()+".")  

    def winner_decide(player,computer): 

        if player == 1 and computer == 3:
            return "\nYou Win! 👻"

        elif player == 2 and computer == 1:
            return "\nYou Win! 👻" 

        elif player == 3 and computer == 2:
            return "\nYou Win! 👻" 
        elif player == computer :
            return "\nIt\'s a Tie! 😥"
        else:
            return "\nPython wins!! 🐍"
    
    winner_text=winner_decide(player,computer)
    print(winner_text)
    global game_count 
    game_count +=1

    
    print("\nPlay again?🤟")
          
    while True:
        playagain = input("\n1.Enter Y for Yes \n2.Enter Q for Quit\n\n")

        if playagain.lower() not in ['y','q']:
            continue
        else:
           break
    
    if playagain.lower() == 'y':
            print("This is game No:"+ str(game_count))
            return rpsgame()
    else:
            print("\nThankyou for playing!🤗")
            sys.exit("\nBye!!👋\n")

rpsgame()




