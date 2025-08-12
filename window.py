import pygame as pg
#inicializando pygame
pg.init()
#criando um clock
clock = pg.time.Clock()

largura_tela = 1200
altura_tela = 600
fps = 60

tela = pg.display.set_mode((largura_tela,altura_tela))

run = True
while run:
    clock.tick(fps)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

pg.quit()