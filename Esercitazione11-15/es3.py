#incompleto
import g2d

def triangolo(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x12 = (x1 + x2) / 2
    x22 = (x2 + x3) / 2
    x32 = (x3 + x1) / 2
    y12 = (y1 + y2) / 2
    y22 = (y2 + y3) / 2
    y32 = (y3 + y1) / 2
    if not (abs(x12-x22)**2 + abs(y12-y22)**2)**0.5 < 10:
        g2d.draw_line((x12, y12), (x22, y22))
        g2d.draw_line((x22, y22), (x32, y32))
        g2d.draw_line((x32, y32), (x12, y12))

        triangolo((x1,y1), (x12, y12), (x22, y22))
        triangolo((x12,y12), (x2, y2), (x32, y32))
        triangolo((x22,y22), (x32, y32), (x3, y3))

    

def main():
    g2d.init_canvas((600, 520))
    triangolo((300, 0), (0, 520), (600, 520))
    g2d.main_loop()
main()