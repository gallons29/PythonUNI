from boardgame import BoardGame
from boardgamegui import gui_play

class Slitherlink(BoardGame):

    def __init__(self, cols, rows, board):
        self._cols = cols
        self._rows = rows
        self._board = board

    def play_at(self, x: int, y: int):
        '''
        In x pari, y pari: si trovano i segni +
        In x dispari, y dispari: si trovano i numeri (se presenti)
        Le linee vanno per cui messe nei casi in cui:
            - x dispari, y pari: linea orizzontale -
            - x pari, y dispari: linea verticale |
        '''
        if x % 2 == 0 and y % 2 != 0:
            if self._board[y * self._cols + x] == ' ': #se lo "slot" è vuoto, viene riempito con la linea,
                self._board[y * self._cols + x] = '|'
            else:                                      #altrimenti (caso "slot" già riempito dalla linea), rimuove la linea
                self._board[y * self._cols + x] = ' '
        elif x % 2 != 0 and y %2 == 0:
            if self._board[y * self._cols + x] == ' ':
                self._board[y * self._cols + x] = '-'
            else:
                self._board[y * self._cols + x] = ' '

    def value_at(self, x: int, y: int) -> str:
        return self._board[y * self._cols + x]

    def flag_at(self, x: int, y: int): 
        if (x % 2 == 0 and y % 2 != 0) or (x % 2 != 0 and y % 2 == 0):
            self._board[y * self._cols + x] = 'x'
    
    def cols(self) -> int: 
        return self._cols
    def rows(self) -> int: 
        return self._rows

    def finished(self) -> bool:
        pass
    def message(self) -> str:
        pass


# -------------------------------- #
# Lettura board da file:           #
with open("Slitherlink\game_5x5.txt", "r") as b:
    board = []
    for line in b:
        for char in line:
            if char != "\n":
                board.append(char)
# -------------------------------- #


gui_play(Slitherlink(11, 11, board))