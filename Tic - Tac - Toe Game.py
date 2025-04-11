board = [" " for _ in range(9)]  # A list of 9 spaces (empty cells)

# Display the game board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Check for a winner
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check if the board is full (i.e., the game is a draw)
def is_board_full():
    return " " not in board

# Main function to handle the game
def play_game():
    current_player = "X"  # X goes first
    while True:
        print_board()
        
        # Get the player's move
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        # Update the board with the player's move
        board[move] = current_player

        # Check for a winner
        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if is_board_full():
            print_board()
            print("It's a draw!")
            break

        # Switch to the next player
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    play_game()