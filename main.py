import pygame
import torre 
pygame.init()

class Inimigo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.vida = 50
        self.vel = 2
def create_tower(x, y):
            grid_x, grid_y = x//64, y//64
            flag = False
            for t in torretas:
                if(grid_x == t.tile[0] and grid_y == t.tile[1]):
                    flag = True
                    break;
            if(not flag):
                torretas.add(torre.Torre((grid_x, grid_y)))
screen = pygame.display.set_mode((1280, 704))
torretas = pygame.sprite.Group()
inimigos = pygame.sprite.Group()
inimigos.add(Inimigo(1000 ,640))
map_image = pygame.image.load("map3.png").convert_alpha()
teste = pygame.image.load("teste.png").convert_alpha() 
run = True
while run:
    pygame.time.Clock().tick(60)
    screen.blit(map_image, (0, 0)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            create_tower(x, y)
    for t in torretas:
        t.draw(screen)
    torretas.update(inimigos)
    pygame.display.update()
pygame.exit()


            