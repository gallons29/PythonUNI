'''
It determines the sequence for the knight to reach all the squares in a n*n board without repetitions, starting from a corner.
'''
import sys
sys.setrecursionlimit(100_000)

MOVES = [(0, 0), (-1, -2), (1, -2), (2, -1), (2, 1), (-1, 2), (1, 2), (-2, -1), (-2, 1)]
#i = y * n + x



def solve(board, n, x, y, order):
    board[y * n + x] = order
    for dx, dy in MOVES:
        if(not is_solved(board, n)):
            board = reset_board(board, n, order)
            x1, y1 = x+dx, y+dy
            if 0 <= x1 < n and 0 <= y1 < n and board[y1 * n + x1] == 0:
                board = solve(board, n, x1, y1, order+1)

    return board

def reset_board(board, n, order): #setta a 0 le caselle col valore > dell'order
    for i in range(n*n):
        if board[i] > order:
            board[i] = 0
    return board

def is_solved(board, n):
    b = board[:]
    b.sort()
    for i in range(n*n):
        if b[i] != i+1:
            return False
    return True



def print_board(board, n):
    for y in range(n):
        for x in range(n):
            print(board[y * n + x], end="\t")
        print()




n=5
board = [0] * (n * n)

solved_board = solve(board, n, 0, 0, 1)

print_board(solved_board, n)


