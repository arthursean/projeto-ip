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
            if(map_path[grid_y][grid_x] == 1):
                flag = True
                print("Isso é um caminho")
            if(not flag):
                print(f"Torre criada em ({x},{y}) nos blocos {grid_x} e {grid_y}")
                torretas.add(torre.Torre((grid_x, grid_y)))
#pra rodar no pygame so tirar o # desse trecho aq embaixo
PATH = [
(0, 224),    # entra pela esquerda
(352, 224),  # vai para direita
(352, 96),  # sobe
(480, 96),  # vai para direita
(480, 224),  # desce
(352, 224), #esquerda
(352, 480), #desce
(224, 480),
(224, 352),
(928, 352),
(928, 160),
(1120, 160),
(1120, 662)  # vai para direita (saída)
]


pygame.init()
torretas = pygame.sprite.Group()

screen = pygame.display.set_mode((1280, 704))
clock = pygame.time.Clock()
mapa = pygame.image.load("map3.png").convert_alpha()


map_path = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]


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
    
    screen.fill((0,0,0))
    screen.blit(mapa, (0,0))

    for t in torretas:
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