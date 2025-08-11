import pygame
import torre
import enemies
import random
import button
import constantes as c
from coletaveis import COLETAVEIS
from coletaveis import Coletavel

def create_tower(x, y, money):
            if grid_x > c.mapWidth - 2:
                print("fora dos limites")
                return money
            for t in torretas:
                if(grid_x == t.tile[0] and grid_y == t.tile[1]):
                    print("Já tem uma torreta aqui")
                    return money
            if(map_path[grid_y][grid_x] == 1):
                flag = True
                print("Isso é um caminho")
                return money
            print(f"Torre criada nos blocos {grid_x} e {grid_y}")
            torretas.add(torre.Torre((grid_x, grid_y)))
            return money - 10

def sel_torres(x, y, torre_marcada):
    if torre_marcada and grid_x > c.mapWidth - 2:
        torre_marcada.selecionado = False
        return None
    for t in torretas:
        if(grid_x == t.tile[0] and grid_y == t.tile[1]):
            t.selecionado = True
            torre_marcada = t
        else:
            t.selecionado = False
    return torre_marcada
    
PATH = c.path
pygame.init()
torretas = pygame.sprite.Group()


screen = pygame.display.set_mode((c.screen_width + c.side_panel , c.screen_height))
coletaveis = pygame.sprite.Group()
clock = pygame.time.Clock()

#variáveis de jogo
placing_torres = False
selling_torres = False
torre_marcada = None

qtd_forca = 0
qtd_distancia = 0
qtd_cooldown = 0
#Carrega Música Manguetown
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load("Manguetown.mp3")
pygame.mixer.music.play(-1)

#Renderiza as quantidades de coletáveis coletados

#carrega imagens
tela_derrota = pygame.image.load(c.derrota_img)
tela_derrota_formatada = pygame.transform.scale(tela_derrota, (592,351))
tela_vitoria = pygame.image.load(c.vitoria_img)
tela_vitoria_formatada = pygame.transform.scale(tela_vitoria,(592,351))
tela_hud = pygame.image.load(c.HUD_img)
tela_hud_formatada = pygame.transform.scale(tela_hud,(352,704))
tela_inicial = pygame.image.load(c.tela_inicial_img)
tela_inicial_formatada = pygame.transform.scale(tela_inicial,(1184,702))
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
times_speed_button = pygame.image.load(c.times_speed_button_img).convert_alpha()
times_speed_button = pygame.transform.scale_by(times_speed_button, 4)
pause_button = pygame.image.load(c.pause_button_img).convert_alpha()
pause_button = pygame.transform.scale_by(pause_button, 4)
continue_button = pygame.image.load(c.continue_button_img).convert_alpha()
continue_button = pygame.transform.scale_by(continue_button, 4)
selling_button = pygame.image.load(c.selling_button_img).convert_alpha()
selling_button = pygame.transform.scale_by(selling_button, 2)
dmg_upgrade = pygame.image.load(c.upgrade_damage_img).convert_alpha()
dmg_upgrade = pygame.transform.scale_by(dmg_upgrade, 4)
range_upgrade = pygame.image.load(c.upgrade_range_img).convert_alpha()
range_upgrade = pygame.transform.scale_by(range_upgrade, 4)
speed_upgrade = pygame.image.load(c.upgrade_speed_img).convert_alpha()
speed_upgrade = pygame.transform.scale_by(speed_upgrade, 4)

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
cancel_button_sprite = button.Button(c.screen_width - 166, 130, cancel_button, True)
end_button_sprite = button.Button((c.screen_width//2) -40, (c.screen_height//2) -20, end_button, True)
play_button_sprite = button.Button((c.screen_width//2) -40, (c.screen_height//2) -20, play_button, True)
selling_button_sprite = button.Button(c.screen_width - 160, 60, selling_button,True)
dmg_upgrade_sprite = button.Button(c.screen_width - 160, 120, dmg_upgrade, True)
range_upgrade_sprite = button.Button(c.screen_width - 160, 160, range_upgrade, True)
speed_upgrade_sprite = button.Button(c.screen_width - 160, 200, speed_upgrade, True)
times_speed_sprite = button.Button(c.screen_width- 215, c.screen_height-128-20, times_speed_button, False)
pause_sprite = button.Button(c.screen_width - 215 +128+15, c.screen_height-128-20, pause_button, True)
continue_sprite = button.Button(c.screen_width- 215, c.screen_height-128-20-50, continue_button, True)
running = True
pygame.font.init()
font = pygame.font.SysFont('Arial', 30) #Arial 30

timeline = c.enemySpawnTimes
remaining_waves = timeline
cur_wave = remaining_waves.pop(0)
remaining_times = list(cur_wave.keys())

next_spawn = remaining_times[0] if len(remaining_times)>0 else -1

frame_count = 0
end_con = ""
state = "title_screen"

times_speed = 1

while running:
    if state == "title_screen":
        screen.blit(tela_inicial_formatada, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if play_button_sprite.draw(screen):
            state = "game_screen"

        pygame.display.flip()
    elif state == "game_screen":
        #SEÇÃO DE DESENHO
        screen.fill((128,128,128))
        screen.blit(tela_hud_formatada,(832,0))
        screen.blit(mapa, (0,0))
        screen.blit(heart, (-30, 35))
        screen.blit(dinheiro, (10, 105))
        screen.blit(forca, (900, 590-128-40))
        screen.blit(distancia, (975, 600-128-40))
        screen.blit(cooldown, (1050, 600-128-40))
         
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
        if torre_marcada:
            selling_button_sprite.draw(screen)
            dmg_upgrade_sprite.draw(screen)
            range_upgrade_sprite.draw(screen)
            speed_upgrade_sprite.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                grid_x, grid_y = x//c.tileSize, y//c.tileSize

                for coletavel in coletaveis:
                    if coletavel.rect.collidepoint(x, y):
                        if coletavel.nome == "velocidade":
                            qtd_cooldown += 1
                        elif coletavel.nome == "força":
                            qtd_forca += 1
                        else:
                            qtd_distancia += 1
                        coletaveis.remove(coletavel)
                        break

                if torre_marcada and selling_button_sprite.draw(screen):
                        torretas.remove(torre_marcada)
                        money += 5
                        torre_marcada = None
                elif torre_marcada and dmg_upgrade_sprite.draw(screen):
                    if qtd_forca > 0:
                        atributo = 'dano'
                        torre_marcada.upgrade(atributo)
                        qtd_forca -= 1
                    else:
                        print("Você não tem coletáveis suficientes")
                elif torre_marcada and range_upgrade_sprite.draw(screen):
                    if qtd_distancia > 0:
                        atributo = 'range'
                        torre_marcada.upgrade(atributo)
                        qtd_distancia -= 1
                    else:
                        print("Você não tem coletáveis suficientes")
                elif torre_marcada and speed_upgrade_sprite.draw(screen):
                    if qtd_cooldown > 0:
                        atributo = 'cooldown'
                        torre_marcada.upgrade(atributo)
                        qtd_cooldown -= 1
                    else:
                        print("Você não tem coletáveis suficientes")
                else:
                    if placing_torres and money >= 10:
                        money = create_tower(grid_x, grid_y, money)
                    else:
                        torre_marcada = sel_torres(grid_x, grid_y, None)

        times_speed = c.speed_mult if times_speed_sprite.draw(screen) else 1
     
        if pause_sprite.draw(screen):
            state = "paused"

        for t in torretas:
            t.update(cur_enemies)
            t.draw(screen)

        if frame_count == next_spawn:
            for en in cur_wave[next_spawn]:
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
                    if random.random() < 0.9:
                        nome = random.choice(list(COLETAVEIS.keys()))
                        imagem = COLETAVEIS[nome]
                        coletavel = Coletavel(enemy.x, enemy.y, imagem, nome)  # Passe o nome!
                        coletaveis.add(coletavel)

        tela_vida = font.render(f'{max(vida, 0)}', True, (255, 255, 255)) 
        tela_dinheiro = font.render(f'{max(money, 0)}', True, (255, 255, 255))
        tela_forca = font.render(f'{qtd_forca}',True,(255,255,255) )
        tela_cooldown = font.render(f'{qtd_cooldown}', True, (255,255,255))
        tela_distancia = font.render(f'{qtd_distancia}', True,(255,255,255))
        
        #Colocando na tela as variáves que mudam conforme são recebidas
        screen.blit(tela_vida, (50, 50))
        screen.blit(tela_dinheiro, (50, 105))
        screen.blit(tela_forca,(900,580-128-40))
        screen.blit(tela_cooldown,(1050, 580-128-40))
        screen.blit(tela_distancia,(975, 580-128-40))

        coletaveis.draw(screen)

        frame_count += 1

        if(vida <= 0):
            state = "end_screen"
            end_con = "GAME OVER"
        elif(len(remaining_times)==0 and not cur_enemies):
            if len(remaining_waves)<= 0:
                state = "end_screen"
                end_con = "Você ganhou o jogo!"
            else:
                if continue_sprite.draw(screen):
                    cur_wave = remaining_waves.pop(0)
                    remaining_times = list(cur_wave.keys())

                    next_spawn = remaining_times[0] if len(remaining_times)>0 else -1

                    frame_count = 0
                    
        pygame.display.flip()
    elif state == "paused":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if pause_sprite.draw(screen):
            state = "game_screen"

    elif state == "end_screen":

        tela_end = font.render(f'{end_con}', True, (255, 255, 255))
        moldura_preta = pygame.draw.rect(screen, (101, 67, 33), (1184//4 - 10, 702//4 - 10, 615, 368))
        if end_con == "Você ganhou o jogo!":
            screen.blit(tela_vitoria_formatada,((1184//4), (702//4)))
        else:
            screen.blit(tela_derrota_formatada, ((1184//4),(702//4)))
        screen.blit(tela_end, (((1184//4), (702//4))))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                grid_x, grid_y = x//c.tileSize, y//c.tileSize
        
        if end_button_sprite.draw(screen):
            running = False
        pygame.display.flip()
    #print(frame_count/60)
    clock.tick(c.clk*times_speed)

pygame.quit()