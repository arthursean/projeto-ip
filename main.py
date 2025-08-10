import pygame
import torre
import enemies
import random
import button
import constantes as c
from coletaveis import COLETAVEIS
from coletaveis import Coletavel

def create_tower(x, y, money):
            grid_x, grid_y = x//c.tileSize, y//c.tileSize
            flag = False
            if grid_x > c.mapWidth - 1:
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


PATH = c.path
pygame.init()
torretas = pygame.sprite.Group()


screen = pygame.display.set_mode((c.screen_width + c.side_panel , c.screen_height))
coletaveis = pygame.sprite.Group()
clock = pygame.time.Clock()

#variáveis de jogo
placing_torres = False
qtd_forca = 0
qtd_distancia = 0
qtd_cooldown = 0

#Renderiza as quantidades de coletáveis coletados

#carrega imagens
forca = pygame.image.load(c.forca_img)
distancia = pygame.image.load(c.distancia_img)
cooldown = pygame.image.load(c.cooldown_img)
exercito = pygame.image.load(c.exercito_img).convert_alpha()
heart = pygame.image.load(c.heart_img).convert_alpha()
heart = pygame.transform.scale_by(heart, 2)
dinheiro = pygame.image.load(c.dinheiro_img).convert_alpha()
dinheiro = pygame.transform.scale_by(dinheiro, 2)
mapa = pygame.image.load(c.mapa_img).convert_alpha()
buy_button = pygame.image.load(c.buy_button_img).convert_alpha()
buy_button = pygame.transform.scale_by(buy_button, 4)
cancel_button = pygame.image.load(c.cancel_button_img).convert_alpha()
cancel_button = pygame.transform.scale_by(cancel_button, 4)
end_button = pygame.image.load(c.end_button_img).convert_alpha()
end_button = pygame.transform.scale_by(end_button, 4)
play_button = pygame.image.load(c.play_button_img).convert_alpha()
play_button = pygame.transform.scale_by(play_button, 4)

map_path = c.placebleTiles

#Lista de inimigos -> comentario!!!!!!
money = 100
vida = 100
'''cur_enemies = [
    enemies.rapido(PATH),
    enemies.tank(PATH),
    enemies.supertank(PATH),
]'''

cur_enemies = []
#cria o botão de compra
buy_button_sprite = button.Button(c.screen_width - 160, 10, buy_button,True)
cancel_button_sprite = button.Button(c.screen_width - 166, 100, cancel_button, True)
end_button_sprite = button.Button((c.screen_width//2) -40, (c.screen_height//2) -20, end_button, True)
play_button_sprite = button.Button((c.screen_width//2) -40, (c.screen_height//2) -20, play_button, True)
running = True
pygame.font.init()
font = pygame.font.SysFont('Arial', 30) # Example: Arial font, size 30

timeline = c.enemySpawnTimes
remaining_times = list(timeline.keys())

next_spawn = remaining_times[0] if len(remaining_times)>0 else -1

frame_count = 0
end_con = ""
state = "title_screen" 

while running:
    if state == "title_screen":
        rect_w = 400
        rect_h = 300
        start_rect = pygame.Rect((c.screen_width-rect_w)//2, (c.screen_height-rect_h)//2, rect_w, rect_h)

        pygame.draw.rect(screen, (255, 0, 0), start_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if play_button_sprite.draw(screen):
            state = "game_screen"

        pygame.display.flip()
    elif state == "game_screen":
        #SEÇÃO DE DESENHO
        screen.fill((128,128,128))
        screen.blit(mapa, (0,0))
        screen.blit(heart, (-30, 35))
        screen.blit(dinheiro, (10, 105))
        screen.blit(forca, (900, 590))
        screen.blit(distancia, (975, 600))
        screen.blit(cooldown, (1050, 600)) 
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
                x, y = pygame.mouse.get_pos()
            if placing_torres and money >= 10:
                money = create_tower(x, y, money)
            # Verifica se clicou em algum coletável (upgrade)
            coletavel_clicado = None
            for colect in coletaveis:
                if colect.rect.collidepoint(x, y):
                    coletavel_clicado = colect
                    break
            if coletavel_clicado:
                if coletavel_clicado.nome == 'velocidade':
                    for t in torretas:
                        t.upgrade_velocidade()
                    print("Velocidade aumentada")
                elif coletavel_clicado.nome == 'força':
                    for t in torretas:
                        t.upgrade_dano()
                    print("Dano aumentado")
                elif coletavel_clicado.nome == 'distancia':
                    for t in torretas:
                        t.upgrade_range()
                    print("Alcance aumentado")
                coletaveis.remove(coletavel_clicado)
        
        
        for t in torretas:
            t.update(cur_enemies)
            t.draw(screen)

        if frame_count == next_spawn:
            for en in timeline[next_spawn]:
                if en == "rapido":
                    cur_enemies.append(enemies.rapido(PATH))
                elif en == "supertank":
                    cur_enemies.append(enemies.supertank(PATH))
                elif en == "tank":
                    cur_enemies.append(enemies.tank(PATH))
            
            remaining_times.pop(0)
            next_spawn = remaining_times[0] if len(remaining_times)>0 else -1

        for enemy in cur_enemies:
            vida = enemy.movimentação(vida)
            enemy.draw(screen)
            if not enemy.vivo:
                if enemy.eliminado:
                    money += 10
                cur_enemies.remove(enemy)
                if enemy.vida <= 0:
                    if random.random() < 0.9:#Chance de spawnar o Upgrade
                        nome = random.choice(list(COLETAVEIS.keys()))
                        if nome == "velocidade":#Contando a quantidade de coletáveis conforme o
                            qtd_cooldown +=1    #drop, o ideal é contar conforme o click no coletável(pode ser ajustado ainda)
                        elif nome == "força":
                            qtd_forca += 1
                        else:
                            qtd_distancia += 1
                        imagem = COLETAVEIS[nome]
                        coletavel = Coletavel(enemy.x, enemy.y, imagem, nome)
                        coletaveis.add(coletavel)

        tela_vida = font.render(f'{max(vida, 0)}', True, (255, 255, 255)) 
        tela_dinheiro = font.render(f'{max(money, 0)}', True, (255, 255, 255))
        tela_forca = font.render(f'{qtd_forca}',True,(255,255,255) )
        tela_cooldown = font.render(f'{qtd_cooldown}', True, (255,255,255))
        tela_distancia = font.render(f'{qtd_distancia}', True,(255,255,255))
        
        #Colocando na tela as variáves que mudam conforme são recebidas
        screen.blit(tela_vida, (50, 50))
        screen.blit(tela_dinheiro, (50, 105))
        screen.blit(tela_forca,(900,580))
        screen.blit(tela_cooldown,(1050, 580))
        screen.blit(tela_distancia,(975, 580))

        coletaveis.draw(screen)
        pygame.display.flip()
        if(vida <= 0):
            state = "end_screen"
            end_con = "Loser"
        elif(len(remaining_times)==0 and not cur_enemies):
            state = "end_screen"
            end_con = "Você ganhou o jogo!"

        frame_count += 1

    elif state == "end_screen":
        
        end_w = 400
        end_h = 300
        end_rect = pygame.Rect((c.screen_width-end_w)//2, (c.screen_height-end_h)//2, end_w, end_h)

        pygame.draw.rect(screen, (255, 0, 0), end_rect)
        tela_end = font.render(f'{end_con}', True, (255, 255, 255))

        screen.blit(tela_end, ((c.screen_width-end_w)//2, (c.screen_height-end_h)//2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if end_button_sprite.draw(screen):
            running = False

        pygame.display.flip()
    #print(frame_count/60)
    clock.tick(c.clk)

pygame.quit()