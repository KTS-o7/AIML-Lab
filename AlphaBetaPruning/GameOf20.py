# The minimax function is the heart of the AI. It recursively calculates the optimal move for the AI.
def minimax(total, turn, alpha, beta):
    # Base case: if total is 20, it's a draw, so return 0
    if total == 20:
        return 0
    # Base case: if total is more than 20, the last player to move loses
    elif total > 20:
        if turn:  # If it's the AI's turn, AI loses, so return -1
            return -1
        else:  # If it's the human's turn, human loses, so return 1
            return 1

    # If it's the AI's turn, we want to maximize the score
    if turn:
        max_eval = -float('inf')  # Initialize max_eval to negative infinity
        for i in range(1, 4):  # For each possible move (1, 2, or 3)
            # Recursively call minimax for the next state of the game
            eval = minimax(total + i, False, alpha, beta)
            max_eval = max(max_eval, eval)  # Update max_eval if necessary
            alpha = max(alpha, eval)  # Update alpha if necessary
            if beta <= alpha:  # If beta is less than or equal to alpha, break the loop (alpha-beta pruning)
                break
        return max_eval  # Return the maximum evaluation
    # If it's the human's turn, we want to minimize the score
    else:
        min_eval = float('inf')  # Initialize min_eval to positive infinity
        for i in range(1, 4):  # For each possible move (1, 2, or 3)
            # Recursively call minimax for the next state of the game
            eval = minimax(total + i, True, alpha, beta)
            min_eval = min(min_eval, eval)  # Update min_eval if necessary
            beta = min(beta, eval)  # Update beta if necessary
            if beta <= alpha:  # If beta is less than or equal to alpha, break the loop (alpha-beta pruning)
                break
        return min_eval  # Return the minimum evaluation

# The total score of the game is initially 0
total = 0

# Game loop
while True:
    # Get the human player's move from input and add it to the total
    human_move = int(input("Enter your move (1, 2, or 3): "))
    while human_move not in [1, 2, 3]:  # If the move is not valid, ask for input again
        print("Invalid move. Please enter 1, 2, or 3.")
        human_move = int(input("Enter your move (1, 2, or 3): "))
    total += human_move
    print(f"After your move, total is {total}")
    if total >= 20:  # If the total is 20 or more after the human's move, the human wins
        print("You win!")
        break

    # If the game is not over, it's the AI's turn
    print("AI is making its move...")
    ai_move = 1
    max_eval = -float('inf')
    for i in range(1, 4):  # For each possible move (1, 2, or 3)
        # Call minimax to get the evaluation of the move
        eval = minimax(total + i, False, -float('inf'), float('inf'))
        if eval > max_eval:  # If the evaluation is greater than max_eval, update max_eval and ai_move
            max_eval = eval
            ai_move = i
    total += ai_move  # Add the AI's move to the total
    print(f"AI adds {ai_move}. Total is {total}")
    if total >= 20:  # If the total is 20 or more after the AI's move, the AI wins
        print("AI wins!")
        break
