# Tic-Tac-Toe using DFS

# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if the game is over
def is_game_over(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    # Check if the board is full
    for row in board:
        if " " in row:
            return False
    return True

# Function to make a move
def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False

# Function to undo a move
def undo_move(board, row, col):
    board[row][col] = " "

# Function to find the best move using DFS
def find_best_move(board, player):
    best_score = float("-inf")
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                make_move(board, row, col, player)
                score = minimax(board, 0, False)
                undo_move(board, row, col)

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move

# Function to evaluate the board
def evaluate(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == "X":
            return 1
        elif row[0] == row[1] == row[2] == "O":
            return -1

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == "X":
            return 1
        elif board[0][col] == board[1][col] == board[2][col] == "O":
            return -1

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == "X":
        return 1
    elif board[0][0] == board[1][1] == board[2][2] == "O":
        return -1
    if board[0][2] == board[1][1] == board[2][0] == "X":
        return 1
    elif board[0][2] == board[1][1] == board[2][0] == "O":
        return -1

    return 0

# Function for the minimax algorithm with DFS
def minimax(board, depth, is_maximizing):
    if is_game_over(board):
        return evaluate(board)

    if is_maximizing:
        best_score = float("-inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    make_move(board, row, col, "X")
                    score = minimax(board, depth + 1, False)
                    undo_move(board, row, col)
                    best_score = max(score, best_score)
        return best_score

    else:
        best_score = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    make_move(board, row, col, "O")
                    score = minimax(board, depth + 1, True)
                    undo_move(board, row, col)
                    best_score = min(score, best_score)
        return best_score

# Main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while not is_game_over(board):
        print_board(board)

        if player == "X":
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if make_move(board, row, col, player):
                player = "O"
            else:
                print("Invalid move! Try again.")
        else:
            print("Computer's turn...")
            row, col = find_best_move(board, player)
            make_move(board, row, col, player)
            player = "X"

    print_board(board)
    winner = evaluate(board)
    if winner == 1:
        print("Congratulations! You won!")
    elif winner == -1:
        print("Sorry, you lost!")
    else:
        print("It's a draw!")

# Start the game
play_game()
