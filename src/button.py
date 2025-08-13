import pygame as pg

class Button(pg.sprite.Sprite):
    def __init__(self, x, y, image, single_click):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.single_click = single_click

    def draw(self, surface):
        action = False
        #pegar a posição do mouse
        mouse_pos = pg.mouse.get_pos()
        #check mouseover and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False: 
                action = True
                #se o botão for de clique único, ele registrar como true  
                if self.single_click:
                    self.clicked = True
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image, self.rect)
        return action