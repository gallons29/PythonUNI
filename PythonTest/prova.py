import g2d
g2d.init_canvas((600, 400))

g2d.set_color((0, 255, 0))

for i in range(1,10):
    g2d.draw_line((i, 50), (300 + i, 200))
    i = i + 1


g2d.draw_line((150, 100), (400, 300))   # pt1, pt2

g2d.set_color((150, 150, 20))
g2d.fill_rect((0, 0), (50, 100))

g2d.set_color((255, 0, 0))
g2d.draw_text("Prova", (150, 100), 45)  # text, left-top, font-size

g2d.main_loop()