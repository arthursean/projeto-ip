import pygame
import math
import torre

class inimigo: #definindo a classe dos inimigos, depois farei a subclasse de cada tipo


    def __init__(self, path, vida, velocidade, img_path):

        self.path = path
        self.path_index = 0
        self.x, self.y = self.path[0]
        self.vida=vida
        self.velocidade=velocidade
        self.img_path = img_path
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.vivo = True
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
<<<<<<< HEAD
            print("morreu")
=======
>>>>>>> teste_imp
            self.vivo = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    #Se o inimigo morrer, ele irá retornar true para que a sprite possa ser apagada 

class rapido(inimigo):
    def __init__(self, path):
        super().__init__(path, velocidade=4, vida=50, img_path="pixilart-drawing (4).png")

class tank(inimigo):
    def __init__(self, path):
        super().__init__(path, velocidade=2, vida=200, img_path="pixilart-drawing (4).png")

class supertank(inimigo):
    def __init__(self, path):
        super().__init__(path, velocidade=0.5, vida=400, img_path="pixilart-drawing (4).png")
<<<<<<< HEAD
=======

def create_tower(x, y):
            grid_x, grid_y = x//64, y//64
            flag = False
            for t in torretas:
                if(grid_x == t.tile[0] and grid_y == t.tile[1]):
                    flag = True
                    break
            if(not flag):
                torretas.add(torre.Torre((grid_x, grid_y)))
#pra rodar no pygame so tirar o # desse trecho aq embaixo
PATH = [
(0, 192),    # entra pela esquerda
(192, 192),  # vai para direita
(192, 128),  # sobe
(320, 128),  # vai para direita
(320, 256),  # desce
(384, 256),
(448, 256),
(448, 320),
(704, 320),  # vai para direita (saída)
]


pygame.init()
torretas = pygame.sprite.Group()

screen = pygame.display.set_mode((1280, 704))
clock = pygame.time.Clock()



#Lista de inimigos -> comentario!!!!!!
enemies = [
    rapido(PATH),
    tank(PATH),
    supertank(PATH),
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            create_tower(x, y)
    
    #torretas.update(inimigos)

    screen.fill((30, 30, 30))

    for t in torretas:
        t.draw(screen)
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
>>>>>>> teste_imp
