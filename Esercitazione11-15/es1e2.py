from boardgame import BoardGame
from random import randint
from boardgamegui import BoardGameGui, gui_play
import g2d

W, H = 40, 40
def abstract():
    raise NotImplementedError("Abstract method")

class Ordine(BoardGame):
    
    def __init__(self, rows, cols, min_val, max_val):
        self._rows = rows
        self._cols = cols
        self._min = min_val
        self._max = max_val
        self._matrice = []
        for i in range(rows*cols):
            self._matrice.append(randint(self._min, self._max+1))
        self._errori = 0
        
    def value_at(self, x: int, y: int) -> str:
        return self._matrice[y * self._cols + x]

    def play_at(self, x: int, y: int):
        massimo = 0
        skip = False
        for val in self._matrice:
            if val == " ":
                skip == True
            elif val >= massimo:
                massimo = val
        if not skip:
            if self.value_at(x, y) == massimo:
                self._matrice[y * self._cols + x] = " "
            else:
                self._errori += 1

    def flag_at(self, x: int, y: int): 
        pass
    
    def cols(self) -> int: 
        return self._cols
    def rows(self) -> int: 
        return self._rows

    def finished(self) -> bool: 
        for val in self._matrice:
            if val != " ":
                return False
        return True

    def message(self) -> str: 
        return f"Errori commessi: {self._errori}"


ordine = Ordine(3,4,5,10)

print(ordine._matrice)
print(ordine.value_at(2,2))

gui_play(ordine)