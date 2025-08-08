import pygame
import math

class inimigo: #definindo a classe dos inimigos, depois farei a subclasse de cada tipo


    def __init__(self, path, vida, velocidade, img_path, forca):

        self.path = path
        self.path_index = 0
        self.x, self.y = self.path[0]
        self.vida=vida
        self.velocidade=velocidade
        self.img_path = img_path
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.vivo = True
        self.forca=forca
    def movimentação(self):
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

        else:
            self.vivo = False

    def dano (self, dmg):
        self.vida-=dmg
        if self.vida<=0:
            self.vivo = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    #Se o inimigo morrer, ele irá retornar true para que a sprite possa ser apagada 

class rapido(inimigo):
    def __init__(self, path):
        super().__init__(path, velocidade=4, vida=50, img_path="BFB.png")

class tank(inimigo):
    def __init__(self, path):
        super().__init__(path, velocidade=2, vida=200, img_path="BFB.png")


#pra rodar no pygame so tirar o # desse trecho aq embaixo

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

PATH = [
(0, 200),    # entra pela esquerda
(200, 200),  # vai para direita
(200, 100),  # sobe
(400, 100),  # vai para direita
(400, 300),  # desce
(600, 300),  # vai para direita (saída)
]

#Lista de inimigos -> comentario!!!!!!
enemies = [
    rapido(PATH),
    tank(PATH)
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    for enemy in enemies:
        enemy.movimentação()
        enemy.draw(screen)
        enemy.dano(0)
        if not enemy.vivo:
            enemies.remove(enemy)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
