from boardgame import BoardGame
from boardgamegui import gui_play

class Slitherlink(BoardGame):

    def __init__(self, cols, rows, board):
        self._cols = cols
        self._rows = rows
        self._board = board

    def play_at(self, x: int, y: int):
        if x % 2 == 0 and y % 2 != 0:
            if self._board[y * self._cols + x] == ' ':
                self._board[y * self._cols + x] = '|'
            else:
                self._board[y * self._cols + x] = ' '
        elif x % 2 != 0 and y %2 == 0:
            if self._board[y * self._cols + x] == ' ':
                self._board[y * self._cols + x] = '-'
            else:
                self._board[y * self._cols + x] = ' '

    def value_at(self, x: int, y: int) -> str:
        return self._board[y * self._cols + x]

    def flag_at(self, x: int, y: int): 
        pass
    
    def cols(self) -> int: 
        return self._cols
    def rows(self) -> int: 
        return self._rows

    def finished(self) -> bool:
        pass
    def message(self) -> str:
        pass

board = list("+ + + + + +" +
             "   3 2 2   " +
             "+ + + + + +" +
             "   0     2 " +
             "+ + + + + +" +
             "   2     1 " +
             "+ + + + + +" +
             "   0     2 " +
             "+ + + + + +" +
             "   2   2   " +
             "+ + + + + +")

gui_play(Slitherlink(11, 11, board))