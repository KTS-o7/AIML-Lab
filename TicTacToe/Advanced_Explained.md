## Code Explained

```python
class TicTacToe:
```

This line defines a class `TicTacToe` which will represent the game board.

```python
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize an empty board
        self.current_winner = None  # Track the winner
```

The `__init__` method is the constructor for the class. It initializes an empty board and sets the `current_winner` to `None`.

```python
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
```

The `print_board` method prints the current state of the board.

```python
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
```

The `available_moves` method returns a list of indices that represent empty spots on the board.

```python
    def empty_squares(self):
        return ' ' in self.board
```

The `empty_squares` method checks if there are any empty squares left on the board.

```python
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
```

The `make_move` method makes a move on the board. If the move leads to a win, it updates `current_winner`.

```python
    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False
```

The `winner` method checks if the current move leads to a win.

```python
def play(game, x_player, o_player, print_game=True):
```

The `play` function starts a game between `x_player` and `o_player`.

```python
class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass
```

The `Player` class represents a player. It has a `get_move` method that should be implemented by subclasses.

```python
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val
```

The `HumanPlayer` class represents a human player. It asks for input from the user to get the next move.

```python
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
```

The `RandomComputerPlayer` class represents a computer player that chooses a random available move.

```python
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        if state.current_winner == other_player:
            return {'position': None, 'score': 1*(state.empty_squares()+1) if other_player == max_player else -1*(state.empty_squares()+1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        if player == max_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
```

The `GeniusComputerPlayer` class represents a computer player that uses the minimax algorithm (a depth-first search technique) to determine the best move. The `minimax` method is a recursive function that simulates all possible games after the current state and chooses the move that leads to the best possible outcome for the computer player. It uses a scoring system where the computer player aims to maximize its score and the human player aims to minimize the computer player's score. The score of a state is the number of empty squares plus or minus one, depending on whether the state is a winning state for the computer player or the human player. If the state is a draw, the score is zero. The `get_move` method of the `GeniusComputerPlayer` class uses the `minimax` method to get the best move. If the board is empty, it chooses a random move.
