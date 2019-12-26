# list containing board fields
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


# prints board layout and board fields from list
def printBoard():
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("==========")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("==========")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


# sort of welcome screen
def signature():
    print(r""" 
 _____ _        _____            _____          
|_   _(_)      |_   _|          |_   _|         
  | |  _  ___    | | __ _  ___    | | ___   ___ 
  | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \
  | | | | (__    | | (_| | (__    | | (_) |  __/
  \_/ |_|\___|   \_/\__,_|\___|   \_/\___/ \___|
    """)
    print("Made by Djordje Mancic, 2019 (c)")
    print("\nWelcome to Tic Tac Toe.\nEach field is number 1-9, X is first player and O is second.\n"
          "Type in corresponding field number to play your move.\n")


# takes player input and places it at given index
def makeMove(move):
    # accept only numbers and numbers from 1 to 9 and checks if field is taken
    try:
        player = int(input("Enter field number for " + move + ": ")) - 1
        if(player < 0 or player > 9):
            raise IndexError

        if(board[player] == "X" or board[player] == "O"):
            print("This field is already taken, try another one!")
            makeMove(move)
        else:
            board[player] = move
            printBoard()
    except (IndexError, ValueError):
        print("Invalid position")
        makeMove(move)


# if there are 5 X's on board, its a tie
def isTie():
    return board.count("X") == 5

# winning combos for X and O
def combo():
    return (
        # X combos
        board[0] == "X" and board[1] == "X" and board[2] == "X" or
        board[3] == "X" and board[4] == "X" and board[5] == "X" or
        board[6] == "X" and board[7] == "X" and board[8] == "X" or

        board[0] == "X" and board[3] == "X" and board[6] == "X" or
        board[1] == "X" and board[4] == "X" and board[7] == "X" or
        board[2] == "X" and board[5] == "X" and board[8] == "X" or

        board[0] == "X" and board[4] == "X" and board[8] == "X" or
        board[2] == "X" and board[4] == "X" and board[6] == "X" or

        # O combos
        board[0] == "O" and board[1] == "O" and board[2] == "O" or
        board[3] == "O" and board[4] == "O" and board[5] == "O" or
        board[6] == "O" and board[7] == "O" and board[8] == "O" or

        board[0] == "O" and board[3] == "O" and board[6] == "O" or
        board[1] == "O" and board[4] == "O" and board[7] == "O" or
        board[2] == "O" and board[5] == "O" and board[8] == "O" or

        board[0] == "O" and board[4] == "O" and board[8] == "O" or
        board[2] == "O" and board[4] == "O" and board[6] == "O"
    )


# main game loop
signature()
printBoard()
while(True):
    makeMove("X")
    if(isTie() and combo() == False):
        print("Its a tie")
        break
    if(combo()):
        print("X won")
        break

    makeMove("O")
    if(combo()):
        print("O won")
        break
