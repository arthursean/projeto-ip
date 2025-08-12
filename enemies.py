import pygame
import math
import torre

class inimigo: #definindo a classe dos inimigos, depois farei a subclasse de cada tipo


    def __init__(self, path, vida, velocidade, img_path, dmg):
        super().__init__()
        self.path = path
        self.path_index = 0
        self.x, self.y = self.path[0]
        self.vida=vida
        self.velocidade=velocidade
        self.img_path = img_path
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.vivo = True
        self.eliminado = False
        self.dmg = dmg
    def movimentação(self, vida):
        # Se não chegou ao final do caminho
        if self.path_index < len(self.path) - 1:
            
         
            target_x, target_y = self.path[self.path_index + 1]
            dx = target_x - self.x
            dy = target_y - self.y
            dist = math.hypot(dx, dy)

            if dist != 0:
                dx, dy = dx / dist, dy / dist  # normaliza direção
                self.x += dx * self.velocidade
                self.y += dy * self.velocidade
                self.rect.center = (self.x, self.y)

            if dist < self.velocidade:
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
class rapido(inimigo):
    def __init__(self, path):
        super().__init__(path, velocidade=4, vida=50, img_path="imagens/inimigos.png", dmg = 50)

class tank(inimigo):
    def __init__(self, path):
        super().__init__(path, velocidade=2, vida=200, img_path="imagens/inimigos.png", dmg = 25)

class supertank(inimigo):
    def __init__(self, path):
        super().__init__(path, velocidade=0.5, vida=400, img_path="imagens/inimigos.png", dmg = 100)