from RockPaperScissorGame import rps
from guess_number import number_game
import sys


def arcade(name="PlayerOne"):
    welcome_back = False
    while(True):
        if welcome_back == True:
            print("\nWelcome back to the Arcade Menu 🕹️")

        player = input("\nChoose between the following 2 games:\n  \n1 = Rock,Paper,Scissors 🪨 🗞️ ✂️\n   \n2 = Guess the Number 💯\n  \n\nPress \"X\" to quit\n\n")

        if player.lower() not in ["1","2","x"]:
            print(f"\nInvalid input {name}, please enter 1,2 or X \n")
            return arcade(name)
       
        welcome_back = True

        if player == "1":
            rpsgame = rps(name)
            rpsgame()
            
        elif player == "2":
            numsgame = number_game(name)
            numsgame()

        else:
            print("\nThankyou for playing! 😌\n")
            sys.exit("Bye!!👋👋")

        

if __name__== "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Provides a personalized greeting for each player in the game")
    parser.add_argument("-n","--name",metavar="name",required=True,help="The name of the person to greet")
    args = parser.parse_args()
    print(f"\n{args.name}, welcome to the Arcade! 🤖")
    arcadia = arcade(args.name)
    arcadia()
