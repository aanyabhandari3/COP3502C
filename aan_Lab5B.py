board = []
counter = 0
height = int(0)
game_play = True

def print_board(board):
    for row in board:
        print(" ".join(row))

def initialize_board(num_rows, num_cols):
    global board, height
    for i in range(0, int(num_rows)):
        ab = []
        for j in range (0, int(num_cols)):
            ab.append("-")
        board.append(ab)
    return board

def insert_chip(board, col, chip_type):
    for r in range(height - 1, -1, -1):
        if board[r][col] == "-":
            board[r][col] = chip_type
            check = check_if_winner(board, col, r, chip_type)
            if check:
                return True
            break
        return board

def check_if_winner(board, col, row, chip_type):
    width = len(board[0])
    height = len(board)
    count = 0
    for w in range(0,width):
        if board[row][w] == chip_type:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0

    count = 0
    for h in range(0,height):
        if board[h][col] == chip_type:
            count += 1
            if count >= 4:
                return True
        else:
            count = 0

    return False

if __name__ == "__main__":
    height = int(input("What would you like the height of the board to be? "))
    length = int(input("What would you like the length of the board to be? "))
    gameboard = initialize_board(height, length)
    print_board(gameboard)
    print("\nPlayer 1: x\nPlayer 2: o\n")
    counter = int(height)* int(length)

    while game_play:
        column = int(input("Player 1: Which column would you like to choose? "))
        check = insert_chip(gameboard,column,chip_type ="x")
        print_board(gameboard)
        counter -= 1
        if check == True:
            print("Player 1 won the game!")
            game_play = False
            break

        column = int(input("Player 2: Which column would you like to choose? "))
        check = insert_chip(gameboard, column, chip_type="o")
        print_board(gameboard)
        counter -= 1
        if check == True:
            print("Player 2 won the game!")
            game_play = False
            break

        if check == 0:
            print("Draw. Nobody wins.")
            game_play = False
            break
        
