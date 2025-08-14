import pygame
import math
from src import torre
import src.constantes as c

class inimigo: #definindo a classe dos inimigos, depois farei a subclasse de cada tipo


    def __init__(self, path, vida, velocidade, img_path_array, dmg):
        super().__init__()
        self.path = path
        self.path_index = 0
        self.x, self.y = self.path[0]
        self.vida=vida
        self.vida_init = vida
        self.velocidade=velocidade
        self.img_path_array = img_path_array
        self.img_path = self.img_path_array[0]
        self.image = pygame.image.load(self.img_path)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.vivo = True
        self.eliminado = False
        self.dmg = dmg
    def movimentação(self, vida, times_speed):
        # Se não chegou ao final do caminho
        if self.path_index < len(self.path) - 1:
            
         
            target_x, target_y = self.path[self.path_index + 1]
            dx = target_x - self.x
            dy = target_y - self.y
            dist = math.hypot(dx, dy)

            if dist != 0:
                dx, dy = dx / dist, dy / dist  # normaliza direção
                self.x += dx * self.velocidade* times_speed
                self.y += dy * self.velocidade* times_speed
                self.rect.center = (self.x, self.y)

            if dist < self.velocidade * times_speed:
                self.path_index += 1
            return vida

        else:
            print("Saiu vivo")
            self.vivo = False
            return vida - self.dmg

    def dano (self, dmg):
        self.vida-=dmg
        if self.vida<=0:
            print("morreu")
            self.vivo = False
            self.eliminado = True
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def update(self):
        if(self.vida <= self.vida_init * 0.5):
            self.img_path = self.img_path_array[1]
            self.image = pygame.image.load(self.img_path)
            self.rect = self.image.get_rect(center=(self.x, self.y))

class rapido(inimigo):
    def __init__(self, path):
        super().__init__(path, velocidade=4, vida=60, img_path_array=["assets/imagens/lixo_rapido.png", "assets/imagens/lixo_rapido_dan.png"], dmg = 5)

class tank(inimigo):
    def __init__(self, path):
        super().__init__(path, velocidade=2, vida=75, img_path_array= ["assets/imagens/lixo_normal.png", "assets/imagens/lixo_normal_dan.png"], dmg = 10)

class supertank(inimigo):
    def __init__(self, path):
        super().__init__(path, velocidade=1.2, vida=250, img_path_array=["assets/imagens/lixo_pesado.png", "assets/imagens/lixo_pesado_dan.png"], dmg = 20)