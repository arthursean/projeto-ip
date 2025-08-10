import pygame
import torre
import enemies
import random
import button
import constantes as c
from coletaveis import COLETAVEIS
from coletaveis import Coletavel
def create_tower(x, y, money):
            grid_x, grid_y = x//64, y//64
            flag = False
            if grid_x > 13:
                print("fora dos limites")
                return money
            for t in torretas:
                if(grid_x == t.tile[0] and grid_y == t.tile[1]):
                    flag = True
                    print("Já tem uma torreta aqui")
                    return money
            if(map_path[grid_y][grid_x] == 1):
                flag = True
                print("Isso é um caminho")
                return money
            if(not flag):
                print(f"Torre criada em ({x},{y}) nos blocos {grid_x} e {grid_y}")
                torretas.add(torre.Torre((grid_x, grid_y)))
                return money - 10
#pra rodar no pygame so tirar o # desse trecho aq embaixo
PATH = [
    (0, 224),   # entrada (primeiro tile à esquerda, centro)
    (416, 224),
    (416, 96),
    (288, 96),  # segue para a direita
    (288, 480),
    (160, 480),
    (160, 352),  # vira para baixo (loop esquerdo)
    (608, 352),  # segue para a direita (trecho central)
    (608, 96),   # sobe (trecho direito superior)
    (736, 96),   # vira para a direita
    (736, 544),  # desce grande trecho (trecho direito inferior)
    (480, 544),  # volta à esquerda (curva para baixo)
    (480, 704),  # saída (último tile, centro)
]
pygame.init()
torretas = pygame.sprite.Group()


screen = pygame.display.set_mode((c.screen_width + c.side_panel , c.screen_height))
coletaveis = pygame.sprite.Group()
clock = pygame.time.Clock()

#variáveis de jogo
placing_torres = False


#carrega imagens
exercito = pygame.image.load("imagens/teste.png").convert_alpha()
heart = pygame.image.load("imagens/heart.png").convert_alpha()
heart = pygame.transform.scale_by(heart, 2)
dinheiro = pygame.image.load("imagens/moeda.png").convert_alpha()
dinheiro = pygame.transform.scale_by(dinheiro, 2)
mapa = pygame.image.load("imagens/map3.png").convert_alpha()
buy_button = pygame.image.load("imagens/pixil-frame-0 (1).png").convert_alpha()
buy_button = pygame.transform.scale_by(buy_button, 4)
cancel_button = pygame.image.load("imagens/pixil-frame-0 (2).png").convert_alpha()
cancel_button = pygame.transform.scale_by(cancel_button, 4)


map_path = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
]


#Lista de inimigos -> comentario!!!!!!
money = 100
vida = 100
enemies = [
    enemies.rapido(PATH),
    enemies.tank(PATH),
    enemies.supertank(PATH),
]
#cria o botão de compra
buy_button_sprite = button.Button(c.screen_width - 160, 10, buy_button,True)
cancel_button_sprite = button.Button(c.screen_width - 166, 100, cancel_button, True)
running = True
pygame.font.init()
font = pygame.font.SysFont('Arial', 30) # Example: Arial font, size 30

while running:


    #SEÇÃO DE DESENHO
    screen.fill((128,128,128))
    screen.blit(mapa, (0,0))
    tela_vida = font.render(f'{vida}', True, (255, 255, 255)) 
    tela_dinheiro = font.render(f'{money}', True, (255, 255, 255))
    screen.blit(heart, (-30, 35))
    screen.blit(tela_vida, (50, 50))
    screen.blit(dinheiro, (10, 105))
    screen.blit(tela_dinheiro, (50, 105))
    #desenha o botão de compra
    if buy_button_sprite.draw(screen):
        placing_torres = True
        #se estiver colocando torres, aparece o botão de cancelar
    if placing_torres:
        #mostrar a torre na tela
        cursor_rect = exercito.get_rect()
        cursor_pos = pygame.mouse.get_pos()
        cursor_rect.center = cursor_pos
        if cursor_pos[0] <= 890:
            screen.blit(exercito, cursor_rect)
        if cancel_button_sprite.draw(screen):
            placing_torres = False

    #SEÇÃO DE EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if placing_torres and money >= 10:
                x, y = pygame.mouse.get_pos()
                money = create_tower(x, y, money)
    
    
    for t in torretas:
        t.update(enemies)
        t.draw(screen)
    for enemy in enemies:
        vida = enemy.movimentação(vida)
        enemy.draw(screen)
        if not enemy.vivo:
            if enemy.eliminado:
                money += 10
            enemies.remove(enemy)
            if enemy.vida <= 0:
                 if random.random() < 0.9:
                    nome = random.choice(list(COLETAVEIS.keys()))
                    imagem = COLETAVEIS[nome]
                    coletavel = Coletavel(enemy.x, enemy.y, imagem)
                    coletaveis.add(coletavel)
    coletaveis.draw(screen)
    pygame.display.flip()
    if(vida <= 0):
        running = False
        print("Loser")
    elif(not enemies):
        running = False
        print("Você ganhou o jogo!")
    clock.tick(c.clk)
pygame.quit()