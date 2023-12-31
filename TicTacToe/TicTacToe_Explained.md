
## Code Explained
```python
# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
```
This function prints the current state of the Tic-Tac-Toe board. It iterates over each row in the board and prints the elements of the row separated by "|". It also prints a line of "-" after each row to separate the rows visually.

```python
# Function to check if the game is over
def is_game_over(board):
```
This function checks if the game is over. The game is over if there is a winner or if the board is full.

```python
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True
```
This part checks all the rows to see if there is a winner. If all elements in a row are the same (and not empty), it means that player has won.

```python
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True
```
This part checks all the columns to see if there is a winner. If all elements in a column are the same (and not empty), it means that player has won.

```python
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
```
This part checks both the diagonals to see if there is a winner. If all elements in a diagonal are the same (and not empty), it means that player has won.

```python
    # Check if the board is full
    for row in board:
        if " " in row:
            return False
    return True
```
This part checks if the board is full. If there is any empty space left on the board, it means the game is not over yet. If the board is full and there is no winner, it means the game is a draw.

```python
# Function to make a move
def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False
```
This function makes a move on the board. It takes the board, the row and column where the move should be made, and the player ('X' or 'O') as input. If the specified cell on the board is empty, it places the player's mark there and returns True. If the cell is not empty, it returns False.

```python
# Function to undo a move
def undo_move(board, row, col):
    board[row][col] = " "
```
This function undoes a move. It takes the board and the row and column of the move to be undone as input. It sets the specified cell on the board to be empty.

```python
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
```
This function finds the best move for the given player using Depth-First Search (DFS). It iterates over each cell on the board. If a cell is empty, it makes a move there, calculates the score of the board using the minimax function, and then undoes the move. If the score of the move is better than the best score found so far, it updates the best score and the best move. After checking all the cells, it returns the best move.

```python
# Function to evaluate the board
def evaluate(board):
```
This function evaluates the board and returns a score. The score is 1 if 'X' has won, -1 if 'O' has won, and 0 otherwise.

```python
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == "X":
            return 1
        elif row[0] == row[1] == row[2] == "O":
            return -1
```
This part checks all the rows to see if there is a winner. If 'X' has won, it returns 1. If 'O' has won, it returns -1.

```python
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == "X":
            return 1
        elif board[0][col] == board[1][col] == board[2][col] == "O":
            return -1
```
This part checks all the columns to see if there is a winner. If 'X' has won, it returns 1. If 'O' has won, it returns -1.

```python
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == "X":
        return 1
    elif board[0][0] == board[1][1] == board[2][2] == "O":
        return -1
    if board[0][2] == board[1][1] == board[2][0] == "X":
        return 1
    elif board[0][2] == board[1][1] == board[2][0] == "O":
        return -1
```
This part checks both the diagonals to see if there is a winner. If 'X' has won, it returns 1. If 'O' has won, it returns -1.

```python
    return 0
```
If there is no winner, the function returns 0.

```python
# Function for the minimax algorithm with DFS
def minimax(board, depth, is_maximizing):
    if is_game_over(board):
        return evaluate(board)
```
This function implements the minimax algorithm with DFS. It takes the board, the current depth of the search tree, and a boolean indicating whether the current player is maximizing or minimizing as input. If the game is over, it returns the score of the board.

```python
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
```
If the current player is maximizing, the function initializes the best score to negative infinity. It then iterates over each cell on the board. If a cell is empty, it makes a move there, calculates the score of the board using a recursive call to the minimax function, and then undoes the move. If the score of the move is better than the best score found so far, it updates the best score. After checking all the cells, it returns the best score.

```python
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
```
If the current player is minimizing, the function initializes the best score to positive infinity. It then iterates over each cell on the board. If a cell is empty, it makes a move there, calculates the score of the board using a recursive call to the minimax function, and then undoes the move. If the score of the move is better (i.e., less) than the best score found so far, it updates the best score. After checking all the cells, it returns the best score.

```python
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
```
This is the main game loop. It initializes an empty board and sets the current player to 'X'. It then

