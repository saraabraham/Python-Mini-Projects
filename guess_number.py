import sys
import random




def number_game(name="Player_One"):
        
        game_count = 0
        player_wins = 0 

        def play_game():
            nonlocal game_count
            nonlocal player_wins
            nonlocal name
            print("\nGuess The Number!!! 🎯")
            playerChoice= input(f"\n{name},guess which number I am thinking of......1,2,3\n\n")
            player=int(playerChoice)
        
            if player not in [1,2,3]:
                print(f"\n😑Invalid Input {name}!! Please enter 1,2,3\n")
                return play_game()
            else:
                print(f"\n{name}, you chose " + playerChoice)
        
            computerChoice = random.choice("123")
            computer = int(computerChoice)

            print("\nI was thinking about number "+ computerChoice)
            game_count += 1

            if player == computer:
                print(f"\n{name},you win!! 🙌\n")
                player_wins += 1
            else:
                print(f"\nSorry {name}! Better luck next time!🥲\n")

            win_per = round((player_wins/game_count) * 100,2)
            print("\nGame count = "+ str(game_count))
            print(f"\n{name}'s Wins 🏆:" + str(player_wins))
            print(f"\n{name},your winning percentage is " + str(win_per) + "%")
            
            while(True):
                play_again=input(f"\n{name}, play again? 🤟 \nPlease enter Y for Yes \nPlease enter Q for Quit\n\n")
                if play_again.lower() not in ["y","q"]:
                    
                    continue
                else:
                    break
            
            if play_again == "y":
                 play_game()
            else:

                if __name__ == "__main__":
                    sys.exit(f"Bye {name}! 👋")
                else:
                  return
        return play_game

if __name__== "__main__":
   
    import argparse
    parser = argparse.ArgumentParser(description="Provides a personalized greeting for each player in the game")
    parser.add_argument("-n","--name",metavar="name",required=True,help="The name of the person to greet")
    args = parser.parse_args()
    num_game = number_game(args.name)
    num_game()
    
        

