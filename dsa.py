import random

# Define the size of the chessboard (N x N)
N = 8
# List to store all valid solutions
solution = []
# Step counter to track the number of steps taken
STEP_COUNTER = 1

# Function to check if the queen can be placed at the given position
def is_safe(board, cell):
    """
    Check if placing a queen in the given cell is safe.
    
    Args:
        board (list): The current board state, where each element is a column position of a queen.
        cell (int): The column where the new queen is to be placed.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    # Check if the column is already occupied
    if cell in board:
        return False

    # Check for conflicts in the diagonals
    for row, col in enumerate(board):
        if abs(row - len(board)) == abs(col - cell):
            return False

    return True

# Function to solve the N-Queens problem using backtracking
def n_queen(board):
    """
    Recursively finds all possible solutions for placing N queens on an N x N chessboard.

    Args:
        board (list): The current board state, where each element is a column position of a queen.
    """
    global STEP_COUNTER

    # Base case: If the board is complete with N queens, save the solution
    if len(board) == N:
        STEP_COUNTER += 1
        solution.append([STEP_COUNTER, board.copy()])
        return

    # Flag to check if a safe position is found in the current row
    found_safe = False

    # Try placing a queen in each column of the current row
    for cell in range(N):
        if is_safe(board, cell):
            found_safe = True
            # Recursively solve for the next row with the current queen placed
            n_queen(board + [cell])

    # Increment the step counter if no safe position is found
    if not found_safe:
        STEP_COUNTER += 1

# Entry point of the program
if __name__ == "__main__":
    # Start solving the N-Queens problem
    n_queen([])

    # Print results
    print("\nTotal Possible Cases (Steps):", STEP_COUNTER)
    print("Total Solutions Found:", len(solution))
    print("\nSolutions:")
    for s in solution:
        print(f"Step {s[0]}: {s[1]}")

    # Wait for user input to exit
    input("\nPress Enter to exit...")

