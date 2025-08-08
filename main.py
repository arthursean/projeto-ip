import pygame
import torre 
pygame.init()

torretas = []
screen = pygame.display.set_mode((832, 832))
coord_usadas = []
map_image = pygame.image.load("map3.png").convert()  
run = True
screen.fill((20, 130, 10))
while run:
    screen.blit(map_image, (0, 0)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            grid_x, grid_y = x//64, y//64
            torretas.append(torre.Torre())
    for t in torretas:
        t.draw(screen)
    pygame.display.update()


            