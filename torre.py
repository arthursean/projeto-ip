import pygame
import math
from dados_torreta import DADOS

class Torre(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.path = "teste.png"
        self.tile = pos
        self.location = ((pos[0] + 0.5) * 64, (pos[1] + 0.5) *64)
        self.range = DADOS['range']
        self.dano = DADOS['dmg']
        self.cd = DADOS['cooldown']
        self.ultimo_tiro = pygame.time.get_ticks()
        self.som = pygame.mixer.Sound('som_tiro.mp3')
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
            if(dist < self.range and inimigo.vivo):
                if(inimigo.vida > 0):
                    inimigo.dano(self.dano)
                    self.ultimo_tiro = pygame.time.get_ticks()
                    self.som.play()
                    break
    def update(self, inimigos):
        if pygame.time.get_ticks() - self.ultimo_tiro >= self.cd:
                self.atacar(inimigos)
    

