import g2d
def triangle(p1, p2, p3):
    g2d.draw_line(p1, p2)
    g2d.draw_line(p2, p3)
    g2d.draw_line(p3, p1)
    x1, y1= p1
    x2, y2 = p2
    x3, y3 = p3
    if not (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5 < 10 and not (abs(x2-x3)**2 + abs(y2-y3)**2)**0.5 < 10 and not (abs(x3-x1)**2 + abs(y3-y1)**2)**0.5 < 10: #teorema di pitagora per calcolare la lunghezza del lato (ipotenusa del triangolo che ha per cateti la distanza delle x e la distanza della y)
        return triangle(((x1+x2)//2, (y1+y2)//2), ((x2+x3)//2, (y2+y3)//2), ((x3+x1)//2, (y3+y1)//2))

def main():
    g2d.init_canvas((600, 520))
    triangle((100,25), (400, 50), (250, 400))
    g2d.main_loop()

main()