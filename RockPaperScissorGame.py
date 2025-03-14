import sys
import random
from enum import Enum

def rps():
    game_count = 1
    player_wins = 0
    python_wins=0
    
    

    def rpsgame():
        nonlocal player_wins
        nonlocal python_wins

        class game(Enum):
            ROCK=1
            PAPER=2
            SCISSORS=3 

        print("\nRock Paper Scissors Game 🪨 🗞️ ✂️")
        playerChoice = input("\nEnter... \n1 for Rock  🪨 \n2 for Paper  🗞️ \n3 for Scissors ✂️ \n\n")
        if playerChoice not in ["1","2","3"]:
            print("\nInvalid input: Please enter 1,2,3")
            return rpsgame()
        
        player = int(playerChoice)
        computerChoice = random.choice("123")
        computer=int(computerChoice)

        print(f"\nYou chose the weapon {str(game(player)).replace("game.","").title()}.")
        print(f"Python chose the weapon {str(game(computer)).replace("game.","").title()}.")  

        def winner_decide(player,computer): 
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return "\nYou Win! 👻"

            elif player == 2 and computer == 1:
                player_wins += 1
                return "\nYou Win! 👻" 

            elif player == 3 and computer == 2:
                player_wins += 1
                return "\nYou Win! 👻" 
            elif player == computer :
                return "\nIt\'s a Tie! 😥"
            else:
                python_wins += 1
                return "\nPython wins!! 🐍"
        
        winner_text=winner_decide(player,computer)
        print(winner_text)
        print(f"\nPlayer wins:{str(player_wins)}")
        print(f"\nPython wins:{str(python_wins)}")     
        nonlocal game_count 
        game_count +=1

        
        print("\nPlay again?🤟")
            
        while True:
            playagain = input("\n1.Enter Y for Yes \n2.Enter Q for Quit\n\n")

            if playagain.lower() not in ['y','q']:
                continue
            else:
             break
        
        if playagain.lower() == 'y':
                print(f"\nThis is game No:{str(game_count)}")
                return rpsgame()
        else:
                print("\nThankyou for playing!🤗")
                sys.exit("\nBye!!👋\n")
    return rpsgame

rock_paper_scissors = rps()

if __name__== "__main__":
    rock_paper_scissors()
     
    




