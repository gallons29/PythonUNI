#!/usr/bin/env python3
'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

import g2d

def sierpinski(position: (int, int), size: (int, int)):
    x, y = position
    w, h = size
    w3, h3 = w // 3, h // 3
    if w3 < 1 or h3 < 1:
        return
    for row in range(3):
        for col in range(3):
            pos = x + col * w3, y + row * h3
            if row == 1 and col == 1:
                g2d.fill_rect(pos, (w3, h3))
            else:
                sierpinski(pos, (w3, h3))

def main():
    g2d.init_canvas((243, 243))
    g2d.set_color((127, 0, 0))
    sierpinski((0, 0), (243, 243))
    g2d.main_loop()

main()
