# Arcade Games

This Python project provides a simple command-line arcade where users can play two classic games: Rock Paper Scissors and Guess the Number.

## Overview

The `arcade.py` script utilizes command-line arguments and user input to offer an interactive gaming experience. Users can start the arcade by providing their name as a command-line argument. Once inside, they can choose between Rock Paper Scissors, Guess the Number, or exit the program.

## Features

* **Command-Line Argument:** Uses `argparse` to accept the user's name as a command-line argument (`-n <name>`).
* **Game Selection Menu:** Presents a menu to choose between Rock Paper Scissors (1), Guess the Number (2), or exit (x).
* **Rock Paper Scissors:** A classic game where the user plays against the computer.
* **Guess the Number:** The user tries to guess a randomly generated number.
* **User-Friendly Interface:** Provides clear prompts and feedback to the user.

## Technologies Used

* Python 3
* `argparse` (for command-line argument parsing)
* `random` (for generating random numbers and computer choices)

## Getting Started

### Prerequisites

* Python 3 installed on your system.

### Running the Arcade

1.  **Clone the repository (if applicable):**

    ```bash
    git clone https://github.com/saraabraham/Python_Arcade_Game.git
    ```

2.  **Run the `arcade.py` script:**

    ```bash
    python3 arcade.py -n <your_name>
    ```

    Replace `<your_name>` with your actual name.

3.  **Follow the on-screen instructions:**

    * Enter `1` to play Rock Paper Scissors.
    * Enter `2` to play Guess the Number.
    * Enter `X` to exit the arcade.

## Example Usage

```bash
Sara, welcome to the Arcade! 🤖

Choose between the following 2 games:
  
1 = Rock,Paper,Scissors
   
2 = Guess the Number
  

Press "X" to quit

1

Rock Paper Scissors Game 🪨 🗞️ ✂️

Sara,please enter... 
1 for Rock  🪨 
2 for Paper  🗞️ 
3 for Scissors ✂️ 

1

Sara chose the weapon Rock.
Python chose the weapon Rock.

It's a Tie! 😥

Sara's wins:0 

