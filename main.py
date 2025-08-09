import pygame
import torre
import enemies
def create_tower(x, y):
            grid_x, grid_y = x//64, y//64
            flag = False
            for t in torretas:
                if(grid_x == t.tile[0] and grid_y == t.tile[1]):
                    flag = True
                    break
            if(not flag):
                torretas.add(torre.Torre((grid_x, grid_y)))
#pra rodar no pygame so tirar o # desse trecho aq embaixo
PATH = [
(0, 192),    # entra pela esquerda
(192, 192),  # vai para direita
(192, 128),  # sobe
(320, 128),  # vai para direita
(320, 256),  # desce
(384, 256),
(448, 256),
(448, 320),
(704, 320),  # vai para direita (saída)
]


pygame.init()
torretas = pygame.sprite.Group()

screen = pygame.display.set_mode((1280, 704))
clock = pygame.time.Clock()
mapa = pygame.image.load("map3.png").convert_alpha()


#Lista de inimigos -> comentario!!!!!!
enemies = [
    enemies.rapido(PATH),
    enemies.tank(PATH),
    enemies.supertank(PATH),
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            create_tower(x, y)
    
    #torretas.update(inimigos)

    screen.fill((0,0,0))
    screen.blit(mapa, (0,0))

    for t in torretas:
        t.draw(screen)
        t.update(enemies)
        t.draw(screen)
    for enemy in enemies:
        enemy.movimentação()
        enemy.draw(screen)
        if not enemy.vivo:
            enemies.remove(enemy)
    pygame.display.flip()
    clock.tick(60)



pygame.quit()