'''
Automatically places queens in a n*n board so that they don't attack each other.
'''
def print_board(board: list):
    for v in board:
        print("• " * v + "♛" + " •" * (len(board)-v-1))

def under_attack(board: list, x: int, y: int) -> bool:
    for r in range(y):  # for each row above y
        # directions: ↖↑↗ (no queens below)
        if board[r] in (x - (y-r), x, x + (y-r)):
            return True
    return False

def place_queens(board: list, y=0) -> bool:
    if y == len(board):
        return True  # all queens already placed
    for x in range(len(board)):
        if not under_attack(board, x, y):
            board[y] = x  # (x, y) is safe: place a queen

            # try and place queens in the following rows
            if place_queens(board, y + 1):
                return True

            board[y] = None  # no luck, backtrack
    return False

def main():
    # side = int(input('side? '))
    # board = [None] * side
    board = [None] * 4

    # solution: place queens starting from first row
    place_queens(board)
    print_board(board)

main()