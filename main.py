import pygame
import random
from src import torre
from src import enemies
from src import button
from src import constantes as c
from src import coletaveis as cl
from src import load_images as l
def create_tower(x, y, money):
            if grid_x > c.mapWidth - 1:
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
            return money - c.turret_price

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
    
def reset():
    global money, vida, frame_count, wave_count, torretas, coletaveis, cur_enemies
    global qtd_forca, qtd_distancia, qtd_cooldown, timeline, remaining_waves
    global cur_wave, remaining_times, qnt_rounds, next_spawn
    money = 60
    vida = 100
    frame_count = 0
    wave_count = 1
    torretas.empty()
    coletaveis.empty()
    cur_enemies.clear()
    qtd_forca = 0
    qtd_distancia = 0
    qtd_cooldown = 0
    timeline = [c.levelData.createTimeline(i) for i in c.levelData.jsonInfo["enemySpawnTimes"]]
    remaining_waves = timeline.copy()
    cur_wave = remaining_waves.pop(0)
    remaining_times = list(cur_wave.keys())
    qnt_rounds = len(timeline)
    next_spawn = remaining_times[0] if len(remaining_times) > 0 else -1

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

pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load("assets/sons/Manguetown.mp3")
pygame.mixer.music.play(-1)



map_path = c.placebleTiles

money = 60
vida = 100

cur_enemies = []

running = True
pygame.font.init()
font = pygame.font.SysFont('Arial', 30) #Arial 30


reset()
end_con = ""
state = "title_screen"

times_speed = 1

while running:
    dt = clock.tick(c.clk * times_speed) / 1000
    if state == "title_screen":
        screen.blit(l.tela_inicial_formatada, (0,0))
        screen.blit(l.titulo, (c.screen_width//2 - 320, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if l.play_button_sprite.draw(screen):
            state = "game_screen"

        pygame.display.flip()
    elif state == "game_screen":
        #SEÇÃO DE DESENHO
        screen.fill((128,128,128))
        screen.blit(l.tela_hud_formatada,(832,0))
        screen.blit(l.mapa, (0,0))
        screen.blit(l.heart, (-30, 35))
        screen.blit(l.dinheiro, (10, 105))
        screen.blit(l.forca, (900, 600-210))
        screen.blit(l.distancia, (975, 600-210))
        screen.blit(l.cooldown, (1050, 600-210))
        screen.blit(l.madeira, (816, 0))         
        #desenha o botão de compra
        if l.buy_button_sprite.draw(screen):
                placing_torres = True
            #se estiver colocando torres, aparece o botão de cancelar
        if money < c.turret_price:
            placing_torres = False
        if placing_torres:
            #mostrar a torre na tela
            cursor_rect = l.exercito.get_rect()
            cursor_pos = pygame.mouse.get_pos()
            cursor_rect.center = cursor_pos
            if cursor_pos[0] <= 890:
                screen.blit(l.exercito, cursor_rect)
            if l.cancel_button_sprite.draw(screen):
                placing_torres = False
        if torre_marcada:
            l.selling_button_sprite.draw(screen)
            l.dmg_upgrade_sprite.draw(screen)
            l.range_upgrade_sprite.draw(screen)
            l.speed_upgrade_sprite.draw(screen)
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

                if torre_marcada and l.selling_button_sprite.draw(screen):
                        torretas.remove(torre_marcada)
                        money += 10
                        torre_marcada = None
                elif torre_marcada and l.dmg_upgrade_sprite.draw(screen):
                    if qtd_forca > 0:
                        atributo = 'dano'
                        qtd_forca -= torre_marcada.upgrade(atributo)
                    else:
                        print("Você não tem coletáveis suficientes")
                elif torre_marcada and l.range_upgrade_sprite.draw(screen):
                    if qtd_distancia > 0:
                        atributo = 'range'
                        qtd_distancia -= torre_marcada.upgrade(atributo)
                    else:
                        print("Você não tem coletáveis suficientes")
                elif torre_marcada and l.speed_upgrade_sprite.draw(screen):
                    if qtd_cooldown > 0:
                        atributo = 'cooldown'
                        qtd_cooldown -= torre_marcada.upgrade(atributo)
                    else:
                        print("Você não tem coletáveis suficientes")
                else:
                    if placing_torres:
                        money = create_tower(grid_x, grid_y, money)
                    else:
                        torre_marcada = sel_torres(grid_x, grid_y, None)

        times_speed = c.speed_mult if l.times_speed_sprite.draw(screen) else 1
     
        if l.pause_sprite.draw(screen):
            state = "paused"
            pygame.mixer.music.pause()
        torretas.update(cur_enemies, times_speed)
        for t in torretas:
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
            vida = enemy.movimentação(vida, times_speed)
            enemy.update()
            enemy.draw(screen)
            if not enemy.vivo:
                if enemy.eliminado:
                    money += 2
                cur_enemies.remove(enemy)
                if enemy.vida <= 0:
                    if random.random() < 0.45:
                        nome = random.choice(list(cl.COLETAVEIS.keys()))
                        imagem = cl.COLETAVEIS[nome]
                        coletavel = cl.Coletavel(enemy.x, enemy.y, imagem, nome)  # Passe o nome!
                        coletaveis.add(coletavel)

        tela_vida = font.render(f'{max(vida, 0)}', True, (255, 255, 255)) 
        tela_dinheiro = font.render(f'{max(money, 0)}', True, (255, 255, 255))
        tela_forca = font.render(f'{qtd_forca}',True,(255,255,255) )
        tela_cooldown = font.render(f'{qtd_cooldown}', True, (255,255,255))
        tela_distancia = font.render(f'{qtd_distancia}', True,(255,255,255))
        tela_rounds = font.render(f'Round {wave_count}/{qnt_rounds}', True, (255, 255, 255))
        
        #Colocando na tela as variáves que mudam conforme são recebidas
        screen.blit(tela_vida, (50, 50))
        screen.blit(tela_dinheiro, (50, 105))
        screen.blit(tela_forca,(900,580-128-40))
        screen.blit(tela_cooldown,(1050, 580-128-40))
        screen.blit(tela_distancia,(975, 580-128-40))
        screen.blit(tela_rounds, (400, 10))

        coletaveis.update()
        coletaveis.draw(screen)

        frame_count += 1
        if(vida <= 0):
            state = "end_screen"
            end_con = "O mangue foi destruído! Não desista agora!"
        elif(len(remaining_times)==0 and not cur_enemies):
            if len(remaining_waves)<= 0:
                state = "end_screen"
                end_con = "Você salvou o mangue!"
            else:
                if l.continue_sprite.draw(screen):
                    cur_wave = remaining_waves.pop(0)
                    remaining_times = list(cur_wave.keys())
                    money += 10
                    next_spawn = remaining_times[0] if len(remaining_times)>0 else -1

                    wave_count += 1
                    frame_count = 0
                    
        pygame.display.flip()
    elif state == "paused":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if l.pause_sprite.draw(screen):
            state = "game_screen"
            pygame.mixer.music.unpause()

    elif state == "end_screen":

        tela_end = font.render(f'{end_con}', True, (255, 255, 255))
        moldura_preta = pygame.draw.rect(screen, (101, 67, 33), (1184//4 - 10, 702//4 - 10, 615, 368))
        if end_con == "Você salvou o mangue!":
            screen.blit(l.tela_vitoria_formatada,((1184//4), (702//4)))
        else:
            screen.blit(l.tela_derrota_formatada, ((1184//4),(702//4)))
        screen.blit(tela_end, (((1184//4), (702//4))))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                grid_x, grid_y = x//c.tileSize, y//c.tileSize
        
        if l.end_button_sprite.draw(screen):
            running = False
        elif l.restart_button_sprite.draw(screen):
            running = True
            reset()
            state = "title_screen"
        pygame.display.flip()
    #print(frame_count/60)
    clock.tick(c.clk*times_speed)

pygame.quit()