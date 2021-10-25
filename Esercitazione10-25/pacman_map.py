'''
@author Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''


board = ["#############################",
         "#             #             #",
         "# ------------# ------------#",
         "# -### -#### -# -#### -### -#",
         "# +### -#### -# -#### -### +#",
         "# -    -     -  -     -    -#",
         "# --------------------------#",
         "# -### -# -####### -# -### -#",
         "# -    -# -   #    -# -    -#",
         "# ------# ----# ----# ------#",
         "###### -####  #  #### -######",
         "###### -#           # -######",
         "###### -#           # -######",
         "###### -#  #######  # -######",
         "       -   #######    -      ",
         "       -   #######    -      ",
         "###### -#  #######  # -######",
         "###### -#           # -######",
         "###### -#           # -######",
         "###### -#  #######  # -######",
         "#      -      #       -     #",
         "# ------------# ------------#",
         "# -### -#### -# -#### -### -#",
         "# -  # -     -  -     -#   -#",
         "# +--# -------  -------# --+#",
         "### -# -# -####### -# -# -###",
         "#   -  -# -   #    -# -  -  #",
         "# ------# ----# ----# ------#",
         "# -######### -# -######### -#",
         "# -          -  -          -#",
         "# --------------------------#",
         "#############################"]


def in_wall(x: int, y: int) -> bool:
    r, c, w, h = x//8, y//8, 3 if x%8 else 2, 3 if y%8 else 2
    return "#" in "".join(line[c:c+w] for line in board[r:r+h])
    ##for line in board[r:r+h]:
    ##    if "#" in line[c:c+w]: return True
    ##return False
