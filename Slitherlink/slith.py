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
        x = 0
        y = 0
        p = (x, y)
        

    def message(self) -> str:
        pass


# -------------------------------- #
# Lettura board da file:           #
with open("Slitherlink\game_5x5.txt", "r") as b:
    board = []
    n_rows = 0
    n_elem = 0
    for line in b:
        n_rows += 1 # conto il numero di linee del file (-1 perchè parte da 0). n_rows indicherebbe quindi il numero di righe
        for char in line:
            n_elem += 1
            if char != "\n":
                board.append(char)

    n_cols = (n_elem // n_rows) - 1
# -------------------------------- #


gui_play(Slitherlink(n_cols, n_rows, board))