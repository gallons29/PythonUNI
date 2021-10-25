import g2d
CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
g2d.init_canvas((CANVAS_WIDTH, CANVAS_HEIGHT))

# for j in range(1, 11):
#     for i in range(1, 11):
#         print(i*j, end="\t")
#     print()

lato_cella = CANVAS_WIDTH / 10
pos_x, pos_y = lato_cella/2, lato_cella/2 #dato che il testo sarà centrato, devo partire da metà cella (al suo centro) per centrarlo alla cella

pos_line_x, pos_line_y = lato_cella, lato_cella

for j in range(1, 11):
    for i in range(1, 11):
        numero = str(i*j)
        size_numero = CANVAS_WIDTH/12
        g2d.draw_text_centered(numero, (pos_x, pos_y), size_numero)
        pos_x += lato_cella

        g2d.draw_line((pos_line_x, pos_line_y-lato_cella), (pos_line_x, pos_line_y))
        g2d.draw_line((pos_line_x-lato_cella, pos_line_y), (pos_line_x, pos_line_y))
        pos_line_x += lato_cella
    pos_y += lato_cella
    pos_x = lato_cella/2
    pos_line_x = lato_cella
    pos_line_y += lato_cella

g2d.main_loop()