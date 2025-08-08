import pygame
import math
from dados_torreta import DADOS
class Torre:
    def __init__(self, pos):
        self.path = "teste.png"
        self.location = pos
        self.range = DADOS['range']
        self.dano = DADOS['dmg']
        self.cd = DADOS['cooldown']
    def draw(self, screen):
        self.img = pygame.image.load(self.path)
        self.img_location = self.img.get_rect()
        self.img_location.center = self.location
        screen.blit(self.img, self.img_location)
    def atacar(self, inimigos):
        for inimigo in inimigos:
            dist_x = (inimigo.x - self.location[0]) ** 2
            dist_y = (inimigo.y - self.location[1]) ** 2
            dist = math.sqrt(dist_x + dist_y)
            if(dist < self.range):
                inimigo.vida -= self.dano

