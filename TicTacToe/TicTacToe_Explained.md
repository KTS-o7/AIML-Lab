# Code Explained

## Intuition

The game is a classic example of a two-player game where one player tries to win by making a line (horizontal, vertical, or diagonal) before the other player does. The AI uses a depth-first search (DFS) strategy to explore all possible moves and chooses the best one.

## Approach

The game is implemented as a class `TicTacToe` with several methods each performing a specific task in the game.

### Step 1: Initialize the board

The `__init__` method initializes the game board as a 3x3 matrix and sets the AI player as 'X'.

```python
def __init__(self):
    self.board = [[' ' for _ in range(3)] for _ in range(3)]
    self.player = 'X'  # AI player
```

### Step 2: Print the board

The `print_board` method prints the current state of the game board.

```python
def print_board(self):
    for row in self.board:
        print(' | '.join(row))
        print('-' * 5)
```

### Step 3: Check if the game is over

The `is_game_over` method checks if there is a winner by checking all rows, columns, and diagonals.

```python
def is_game_over(self):
    ...
```

### Step 4: Accept keyboard input for 'O'

In the `play` method, if it's the human player's turn, the game accepts keyboard input for the player 'O'.

```python
if self.player == 'O':
    ...
```

### Step 5: DFS logic to choose the best move

The `dfs` method implements the DFS logic. It recursively checks all possible moves and returns the best move for the AI player.

```python
def dfs(self, board, depth, player):
    ...
```

## Visualization

Here's a simple visualization of the game board after a few moves:

```
X | O | X
---------
O | X |
---------
    |   | O
```

In this state, if it's 'X's turn, the AI will use the `dfs` method to calculate the best move. If it's 'O's turn, the game will wait for the human player's input.

---

---

### Detailed Code explaination.

---

```python
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = 'X'  # AI player
```

This is the constructor method that gets called when an object of `TicTacToe` is created. It initializes the game board as a 3x3 matrix filled with spaces, representing an empty board. It also sets the first player as 'X', which is the AI player.

```python
    def print_board(self):
        for row in self.board:
            print(' | '.join(row))
            print('-' * 5)
```

This method prints the current state of the game board. It iterates over each row of the board and prints the elements separated by '|'. After each row, it prints a line of dashes for visual separation.

```python
    def is_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True
```

This method checks if the game is a draw. It iterates over each row of the board and checks if there is any empty space left. If there is no empty space left on the board, it means the game is a draw.

```python
    def is_game_over(self):
        for row in self.board:
            if row.count(row[0]) == len(row) and row[0] != ' ':
                return row[0]
        for col in range(len(self.board[0])):
            check = []
            for row in self.board:
                check.append(row[col])
            if check.count(check[0]) == len(check) and check[0] != ' ':
                return check[0]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return False
```

This method checks if the game is over, which can be due to a win by either player or a draw. It checks all rows, columns, and diagonals for a win. If any row, column, or diagonal has all 'X' or all 'O', it means the respective player has won.

```python
    def dfs(self, board, depth, player):
        winner = self.is_game_over()
        if winner:
            if winner == 'X':  # AI wins
                return {'score': 1}
            else:  # Human wins
                return {'score': -1}
        elif self.is_draw():
            return {'score': 0}  # Draw

        if player == 'X':
            best = {'score': -float('inf')}
            symbol = 'X'
        else:
            best = {'score': float('inf')}
            symbol = 'O'

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = symbol
                    score = self.dfs(board, depth + 1, 'O' if player == 'X' else 'X')
                    board[i][j] = ' '
                    score['row'] = i
                    score['col'] = j

                    if player == 'X':
                        if score['score'] > best['score']:
                            best = score
                    else:
                        if score['score'] < best['score']:
                            best = score
        return best
```

This method implements the depth-first search logic to choose the best move for the AI player. It recursively checks all possible moves and returns the best move. It uses a scoring system where a win by the AI player (X) is +1, a win by the human player (O) is -1, and a draw is 0. The AI player tries to maximize the score, while the human player tries to minimize it.

```python
    def play(self):
        while True:
            self.print_board()
            winner = self.is_game_over()
            if winner or self.is_draw():
                print("Game Over.")
                if self.is_draw():
                    print("It's a draw!")
                else:
                    print(f"Player {winner} wins!")
                break

            if self.player == 'X':
                best_move = self.dfs(self.board, 0, 'X')
                self.board[best_move['row']][best_move['col']] = 'X'
            else:
                while True:
                    try:
                        row = int(input("Enter the row number (0-2): "))
                        col = int(input("Enter the column number (0-2): "))
                        if self.board[row][col] == ' ':
                            self.board[row][col] = 'O'
                            break
                        else:
                            print("Invalid move. Try again.")
                    except (ValueError, IndexError):
                        print("Invalid input. Please enter numbers between 0 and 2.")

            self.player = 'O' if self.player == 'X' else 'X'

game = TicTacToe()
game.play()
```

This is the main game loop. It keeps running until the game is over. In each iteration, it first prints the current state of the board. Then it checks if the game is over or a draw. If so, it prints the result and breaks the loop. If it's the AI player's turn, it calculates the best move using the depth-first search method and makes the move. If it's the human player's turn, it waits for the human player's input and makes the move.

The `game = TicTacToe()` line creates an object of the `TicTacToe` class, and `game.play()` starts the game.
