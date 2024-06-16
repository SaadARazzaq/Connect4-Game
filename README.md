# Connect 4 CLI Game Overview

Welcome to Connect 4, a classic two-player game now available in a Command Line Interface (CLI) version! In this game, you can choose to play against another player or challenge the computer. The objective is to connect four of your tokens in a row, either horizontally, vertically, or diagonally.

![image](https://github.com/SaadARazzaq/Connect4-Game/assets/123338307/50ca5e8f-a9be-4c14-900e-a44039346328)

## Features

- Two-player mode
- Player vs. Computer mode
- Simple and intuitive CLI interface
- Dynamic game board display

## Requirements

- Python 3.x
- art library (for the welcome message)

## Installation

- Ensure you have Python 3.x installed on your system.
- Install the art library using pip:
```bash
pip install art
```

## How to Play

1. Clone this repository or download the game script.
2. Open your terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using Python:
```bash
python Connect_4.py
```
5. Follow the on-screen instructions to start the game.

## Game Instructions

### Main Menu

When you start the game, you will be presented with the main menu. You have the following options:

1. Play a 2 player game
2. Play a game against CPU (Computer)
3. Exit

### Playing the Game

- Two Player Game: Each player takes turns to place their token on the board. Player 1 uses the "🔵" token and Player 2 uses the "🔴" token.
- Player vs. CPU: You will play against the computer. You use the "🔵" token, and the computer uses the "🔴" token.

### Making a Move

- The game board is displayed with columns labeled A to G and rows numbered 0 to 5.
- To make a move, input the column letter followed by the row number (e.g., A0).
- The token will drop to the lowest available space in the selected column, adhering to gravity rules.

### Winning the Game

- The game ends when a player connects four of their tokens in a row, either horizontally, vertically, or diagonally.
- The winner is announced, and the game board is displayed one final time.

## Example Game Play

1. Start the game and choose to play against the computer.
2. Enter your player name.
3. The game board is displayed, and the player's turn is indicated.
4. Enter your move (e.g., "A0").
5. The computer makes its move.
6. The game continues until there is a winner or the board is full.

## Game Screenshots:

![image](https://github.com/SaadARazzaq/Connect4-Game/assets/123338307/50ca5e8f-a9be-4c14-900e-a44039346328)
![image](https://github.com/SaadARazzaq/Connect4-Game/assets/123338307/65402c0f-8e70-4634-8410-936290f9074c)
![image](https://github.com/SaadARazzaq/Connect4-Game/assets/123338307/a9fc8be6-09c4-4230-aec9-032eeb6d4e0b)
![image](https://github.com/SaadARazzaq/Connect4-Game/assets/123338307/461523dd-090a-44f9-b0a3-70f8cc6f0005)
![image](https://github.com/SaadARazzaq/Connect4-Game/assets/123338307/9abcba75-61d6-4304-b20b-7736d3568776)
![image](https://github.com/SaadARazzaq/Connect4-Game/assets/123338307/7c1c798e-0721-439e-a885-8eb0f7beee95)
![image](https://github.com/SaadARazzaq/Connect4-Game/assets/123338307/37de5d3f-1bcf-4c0a-b52a-377ba5aa9e42)
![image](https://github.com/SaadARazzaq/Connect4-Game/assets/123338307/eda7ac9f-a7bd-48c9-98f2-32c098fcc7bf)
![image](https://github.com/SaadARazzaq/Connect4-Game/assets/123338307/9f282a63-1d14-4617-8e4c-03ca4bac891f)
![image](https://github.com/SaadARazzaq/Connect4-Game/assets/123338307/d7a81000-db56-45c8-b906-6ab3549ac9ff)
![image](https://github.com/SaadARazzaq/Connect4-Game/assets/123338307/d7003b55-c5f6-4b10-a91f-4a6c98756a79)
![image](https://github.com/SaadARazzaq/Connect4-Game/assets/123338307/ebd4a515-787b-4d73-8e30-2fce74f4fbd5)

## Developer Notes

- The game uses a 6x7 grid to represent the Connect 4 board.
- The art library is used to print the welcome message in a stylized font.
- Functions are modular and handle specific tasks like printing the board, checking for a winner, and managing turns.

## Future Enhancements

- Add difficulty levels for the computer opponent.
- Implement a graphical user interface (GUI) for a more interactive experience.
- Allow players to undo moves.

---
Enjoy the game and have fun connecting four! 💖
