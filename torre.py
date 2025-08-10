import pygame
import math
from dados_torreta import DADOS
import constantes as c

class Torre(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.path = "imagens/teste.png"
        self.tile = pos
        self.location = ((pos[0] + 0.5) * c.tileSize, (pos[1] + 0.5) * c.tileSize)
        self.range = DADOS['range']
        self.dano = DADOS['dmg']
        self.cd = DADOS['cooldown']
        self.ultimo_tiro = pygame.time.get_ticks()
        self.som = pygame.mixer.Sound('som_tiro.mp3')
        self.angulo = 0
        self.selecionado = False
        
    def draw(self, screen):
        self.img = pygame.image.load(self.path)
        self.img = pygame.transform.scale_by(self.img, 1.1)
        self.img = pygame.transform.rotate(self.img, self.angulo)
        self.img_location = self.img.get_rect()
        self.img_location.center = self.location
        screen.blit(self.img, self.img_location)
        if self.selecionado:
            pygame.draw.circle(screen, (0, 0, 0), self.location, self.range, 1)
    def atacar(self, inimigos):
        for inimigo in inimigos:
            dist_x = (inimigo.x - self.location[0])
            dist_y = (inimigo.y - self.location[1]) 
            dist = math.sqrt(dist_x**2 + dist_y**2)
            if(dist < self.range and inimigo.vivo):
                if(inimigo.vida > 0):
                    inimigo.dano(self.dano)
                    self.ultimo_tiro = pygame.time.get_ticks()
                    self.som.play()
                    self.angulo = math.degrees(math.atan2(-dist_y, dist_x) - 90) #subtrai - 90 pois a imagem original é pra cima
                    break
    def update(self, inimigos):
        if pygame.time.get_ticks() - self.ultimo_tiro >= self.cd:
                self.atacar(inimigos)
        elif pygame.time.get_ticks() - self.ultimo_tiro > 500:
            self.angulo = 0
    

