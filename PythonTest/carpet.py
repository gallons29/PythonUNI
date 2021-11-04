import g2d

def carpet(x, y, w, h):
    w3, h3 = w // 3, h // 3
    if w3 <= 1 or h3 <= 1:
        return
    pos = x + w3, y + h3
    size = w3, h3
    g2d.fill_rect(pos, size)

    carpet(x, y, w3, h3)
    carpet(x + w3, y, w3, h3)
    carpet(x + 2*w3, y, w3, h3)
    carpet(x, y + h3, w3, h3)
    carpet(x + 2*w3, y + h3, w3, h3)
    carpet(x, y + 2*h3, w3, h3)
    carpet(x + w3, y + 2*h3, w3, h3)
    carpet(x + 2*w3, y + 2*h3, w3, h3)


def main():
    g2d.init_canvas((600, 600))
    carpet(0, 0, 600, 600)
    g2d.main_loop()
main()