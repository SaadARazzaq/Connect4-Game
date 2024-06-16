'''

Connect 4 Game:
Programming Language: Python
Interface: CLI based

'''

import random
import art

# Print welcome message
art.tprint("Welcome to Connect Four")
art.tprint("-----------------------")

# Possible columns where players can place their tokens
possibleLetters = ["A", "B", "C", "D", "E", "F", "G"]
# Initialize the game board as a 6x7 grid
gameBoard = [["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""],
             ["", "", "", "", "", "", ""]]

rows = 6
cols = 7

# Function to print the game board
def printGameBoard():
    print("\n     A    B    C    D    E    F    G  ", end="")
    for x in range(rows):
        print("\n   +----+----+----+----+----+----+----+")
        print(x, " |", end="")
        for y in range(cols):
            if gameBoard[x][y] == "🔵":
                print("", gameBoard[x][y], end=" |")
            elif gameBoard[x][y] == "🔴":
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   +----+----+----+----+----+----+----+")

# Function to modify the game board with the player's token
def modifyArray(spacePicked, turn):
    gameBoard[spacePicked[0]][spacePicked[1]] = turn

# Function to check for a winner
def checkForWinner(chip):
    # Check horizontal spaces
    for y in range(rows):
        for x in range(cols - 3):
            if gameBoard[x][y] == chip and gameBoard[x + 1][y] == chip and gameBoard[x + 2][y] == chip and gameBoard[x + 3][y] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    # Check vertical spaces
    for x in range(rows):
        for y in range(cols - 3):
            if gameBoard[x][y] == chip and gameBoard[x][y + 1] == chip and gameBoard[x][y + 2] == chip and gameBoard[x][y + 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    # Check upper right to bottom left diagonal spaces
    for x in range(rows - 3):
        for y in range(3, cols):
            if gameBoard[x][y] == chip and gameBoard[x + 1][y - 1] == chip and gameBoard[x + 2][y - 2] == chip and gameBoard[x + 3][y - 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True

    # Check upper left to bottom right diagonal spaces
    for x in range(rows - 3):
        for y in range(cols - 3):
            if gameBoard[x][y] == chip and gameBoard[x + 1][y + 1] == chip and gameBoard[x + 2][y + 2] == chip and gameBoard[x + 3][y + 3] == chip:
                print("\nGame over", chip, "wins! Thank you for playing :)")
                return True
    return False

# Function to convert user input (e.g., "A1") to board coordinates
def coordinateParser(inputString):
    if len(inputString) != 2:
        raise ValueError("Invalid input format. Input should be a letter followed by a number (e.g., A1).")
    column = inputString[0].upper()
    if column not in possibleLetters:
        raise ValueError("Invalid column letter.")
    row = int(inputString[1])
    if row < 0 or row >= rows:
        raise ValueError("Invalid row number.")
    return [row, possibleLetters.index(column)]

# Function to check if a space on the board is available
def isSpaceAvailable(intendedCoordinate):
    if gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔴':
        return False
    elif gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔵':
        return False
    else:
        return True

# Function to check if a space is valid according to gravity rules
def gravityChecker(intendedCoordinate):
    # Calculate space below
    spaceBelow = [intendedCoordinate[0] + 1, intendedCoordinate[1]]
    # Check if the coordinate is at ground level
    if spaceBelow[0] == 6:
        return True
    # Check if there's a token below
    if isSpaceAvailable(spaceBelow) == False:
        return True
    return False

# Function to handle a player's turn
def playerTurn(playerName, playerChip):
    while True:
        print(f"{playerName}'s turn ({playerChip})")
        spacePicked = input("Choose a space: ")
        try:
            coordinate = coordinateParser(spacePicked)
            # Check if the space is available and valid according to gravity rules
            if isSpaceAvailable(coordinate) and gravityChecker(coordinate):
                modifyArray(coordinate, playerChip)
                break
            else:
                print("Not a valid coordinate")
        except ValueError as e:
            print(e)

# Function to handle the computer's turn
def computerTurn():
    print("Computer's turn (🔴)")
    while True:
        cpuChoice = [random.choice(possibleLetters), random.randint(0, 5)]
        cpuCoordinate = coordinateParser(cpuChoice[0] + str(cpuChoice[1]))
        if isSpaceAvailable(cpuCoordinate) and gravityChecker(cpuCoordinate):
            modifyArray(cpuCoordinate, '🔴')
            break

# Function to start a two-player game
def twoPlayerGame():
    player1Name = input("Enter Player 1 name: ")
    player2Name = input("Enter Player 2 name: ")
    print(f"\n{player1Name} VS {player2Name} BATTLE:\n")
    leaveLoop = False
    turnCounter = 0
    while not leaveLoop:
        printGameBoard()
        if turnCounter % 2 == 0:
            playerTurn(player1Name, '🔵')
            winner = checkForWinner('🔵')
        else:
            playerTurn(player2Name, '🔴')
            winner = checkForWinner('🔴')
        turnCounter += 1
        if winner:
            printGameBoard()
            break

# Function to start a game against the computer
def playAgainstCPU():
    playerName = input("Enter Player name: ")
    print(f"\n{playerName} VS Computer BATTLE:\n")
    leaveLoop = False
    turnCounter = 0
    while not leaveLoop:
        printGameBoard()
        if turnCounter % 2 == 0:
            playerTurn(playerName, '🔵')
            winner = checkForWinner('🔵')
        else:
            computerTurn()
            winner = checkForWinner('🔴')
        turnCounter += 1
        if winner:
            printGameBoard()
            break

def mainMenu():
      print("\nMain Menu")
      print("1. Play a 2 player game")
      print("2. Play a game against CPU (Computer)")
      print("3. Exit")
      choice = input("Select an option: ")
      if choice == "1":
          twoPlayerGame()
      elif choice == "2":
          playAgainstCPU()
      elif choice == "3":
          print("Thank you for playing! Goodbye.")
          exit(0)
      else:
          print("Invalid choice. Please select again.")

mainMenu()
