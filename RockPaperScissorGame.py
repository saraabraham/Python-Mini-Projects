import sys
import random
from enum import Enum

def rps(name):
    game_count = 1
    player_wins = 0
    python_wins=0

    def rpsgame():
        nonlocal player_wins
        nonlocal python_wins
        nonlocal name

        class game(Enum):
            ROCK=1
            PAPER=2
            SCISSORS=3 

        
        print("\nRock Paper Scissors Game 🪨 🗞️ ✂️")
        playerChoice = input(f"\n{name},please enter... \n1 for Rock  🪨 \n2 for Paper  🗞️ \n3 for Scissors ✂️ \n\n")
        if playerChoice not in ["1","2","3"]:
            print(f"\nInvalid input {name}! Please enter either 1,2,3")
            return rpsgame()
        
        player = int(playerChoice)
        computerChoice = random.choice("123")
        computer=int(computerChoice)

        print(f"\n{name} chose the weapon {str(game(player)).replace("game.","").title()}.")
        print(f"Python chose the weapon {str(game(computer)).replace("game.","").title()}.")  

        def winner_decide(player,computer): 
            nonlocal player_wins
            nonlocal python_wins
            nonlocal name

            if player == 1 and computer == 3:
                player_wins += 1
                return f"\n{name} Wins! 👻"

            elif player == 2 and computer == 1:
                player_wins += 1
                return f"\n{name} Wins! 👻" 

            elif player == 3 and computer == 2:
                player_wins += 1
                return f"\n{name} Wins! 👻" 
            elif player == computer :
                return "\nIt\'s a Tie! 😥"
            else:
                python_wins += 1
                return f"\nPython wins!! 🐍, sorry {name} 😢"
        
        winner_text=winner_decide(player,computer)
        print(winner_text)
        print(f"\n{name}'s wins:{str(player_wins)}")
        print(f"\nPython wins:{str(python_wins)}")     
        nonlocal game_count 
        game_count +=1

        
        print(f"\n{name}, do you want to play again?🤟")
            
        while True:
            playagain = input("\n1.Please enter Y for Yes \n2.enter Q for Quit\n\n")

            if playagain.lower() not in ['y','q']:
                continue
            else:
             break
        
        if playagain.lower() == 'y':
                print(f"\nYeayyyyy! Way to go {name}!")
                print(f"\nThis is game No:{str(game_count)}")
                return rpsgame()
        else:
                if __name__ == "__main__":
                  sys.exit(f"Bye {name}! 👋")
                else:
                  return
                
    return rpsgame



if __name__== "__main__":
   
    import argparse
    parser = argparse.ArgumentParser(description="Provides a personalized greeting for each player in the game")
    parser.add_argument("-n","--name",metavar="name",required=True,help="The name of the person to greet")
    args = parser.parse_args()
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
    
     
    




