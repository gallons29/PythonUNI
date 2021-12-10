from boardgame import BoardGame
from boardgamegui import gui_play

LINE, FLAG, PLUS, FREE = ["-", "|"], "x", "+", " "
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def add(p1, p2: (int, int)) -> (int, int):
    return p1[0] + p2[0], p1[1] + p2[1]

class Slitherlink(BoardGame):

    def __init__(self, cols, rows, board):
        self._cols = cols
        self._rows = rows
        self._board = board
        self._pos_track = []

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
        else:
            self._auto_complete(x, y)

    def _auto_complete(self, x, y):
        if x % 2 == 0 and y % 2 == 0:
        #autocompletamento quando schiaccia +
            cl, cb, cx = self._whats_around(x, y)
            if cb == 1 and cl == 1:
                for d in DIRS:
                    if self.value_at(*add((x, y), d)) == FREE:
                        dx, dy = d
                        if (x + dx) % 2 == 0 and (y + dy) % 2 != 0:
                            self._board[(y + dy) * self._cols + x + dx] = LINE[1]
                        else:
                            self._board[(y + dy) * self._cols + x + dx] = LINE[0]
            elif cb == 1 and cx == 1:
                for d in DIRS:
                    if self.value_at(*add((x, y), d)) == FREE:
                        dx, dy = d
                        self._board[(y + dy) * self._cols + x + dx] = FLAG
            elif cl == 2:
                for d in DIRS:
                    if self.value_at(*add((x, y), d)) == FREE:
                        dx, dy = d
                        self._board[(y + dy) * self._cols + x + dx] = FLAG

        
        elif self._board[y * self._cols + x] in "0123":
        #autocompletamento quando schiaccia un numero
            num = int(self._board[y * self._cols + x])
            cl, cb, cx = self._whats_around(x, y)

            if cl == num:
            #ci sono già le linee giuste -> tutte x
                for d in DIRS:
                    if self.value_at(*add((x, y), d)) == FREE:
                        dx, dy = d
                        self._board[(y + dy) * self._cols + x + dx] = FLAG
            
            elif cb == num - cl:
                for d in DIRS:
                    if self.value_at(*add((x, y), d)) == FREE:
                        dx, dy = d
                        if (x + dx) % 2 == 0 and (y + dy) % 2 != 0:
                            self._board[(y + dy) * self._cols + x + dx] = LINE[1]
                        else:
                            self._board[(y + dy) * self._cols + x + dx] = LINE[0]

                    
    def _whats_around(self, x, y):
        '''
        Data una posizione, ritorna una tupla contenente il numero di linee, di free e di flag che quella posizione ha intorno.
        '''
        cl = 0 #counter line around
        cb = 0 #counter blank around
        cx = 0 #counter x around
        for val in self._around((x, y)):
            if val == LINE[0] or val == LINE[1]:
                cl += 1
            elif val == FLAG:
                cx += 1
            elif val == FREE:
                cb += 1
        return cl, cb, cx


    def value_at(self, x: int, y: int) -> str:
        if 0 <= x < self._cols and 0 <= y < self._rows:
            return self._board[y * self._cols + x]
        return ""

    def flag_at(self, x: int, y: int): 
        if (x % 2 == 0 and y % 2 != 0) or (x % 2 != 0 and y % 2 == 0):
            self._board[y * self._cols + x] = 'x'
    
    def cols(self) -> int: 
        return self._cols
    def rows(self) -> int: 
        return self._rows

    def message(self) -> str:
        return "Hai vinto!"

    def _around(self, pos: (int, int)) -> [str]:
        return [self.value_at(*add(pos, d)) for d in DIRS]

    def _follow(self, pos, end, prv: (int, int), n: int) -> int:
        if pos == end and n > 0: return n
        for d in DIRS:
            nxt = add(pos, d)
            if nxt != prv and self.value_at(*nxt) in LINE and (add(nxt, d) not in self._pos_track or add(nxt, d) == end):
                self._pos_track.append(pos)
                '''
                SPIEGAZIONE self._pos_track :
                    self._pos_track è una lista contenente tutte le pos dove il "tracciato passa".
                    Mi serve per evitare che il tracciato finisca in un loop continuo di ricorsioni.
                    Per fare ciò, prima di chiamare la nuova ricorsione, 
                    faccio un controllo
                    if [...] and (add(nxt, d) not in self._pos_track or add(nxt, d) == end)
                    per vedere se la pos futura non è già stata tracciata TRANNE nel caso coincida con "end" e che quindi la chiamata della funzione che andrò a fare sarà l'ultima.
                '''
                return self._follow(add(nxt, d), end, nxt, n + 1)

    def _check_nums(self):
        #Controllo se ogni numero ha intorno il numero di linee giuste
        for y in range(self._rows):
            for x in range(self._cols):
                if self._board[y * self._cols + x] in "0123":
                    la = int(self._board[y * self._cols + x])
                    cl, cb, cx = self._whats_around(x, y)
                    if cl != la:
                        return False

        return True

    def finished(self):
        lines = 0
        for line in LINE:
            lines += self._board.count(line)

        if lines == 0: return False
        if LINE[0] in self._board:
            i = self._board.index(LINE[0])
        else:
            i = self._board.index(LINE[1])
        x, y = (i % self._cols, i // self._cols)
        pos = (x + x % 2, y + y % 2)
        self._pos_track = []
        return self._follow(pos, pos, (x, y), 0) == lines and self._check_nums()


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