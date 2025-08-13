from levelData import LevelData

screen_width = 1088
screen_height = 702
clk = 60
side_panel = 96
turret_price = 20

levelData = LevelData("map.json")

path = levelData.path
placebleTiles = levelData.placebleTiles

exercito_img = "imagens/teste.png"
heart_img = "imagens/heart.png"
dinheiro_img = "imagens/moeda.png"
play_button_img = "imagens/jogar.png" 
forca_img = "imagens/laursa.png"
distancia_img = "imagens/oculos.png"
cooldown_img = "imagens/pitu.png"
buy_button_img = "imagens/comprar.png"
cancel_button_img = "imagens/cancelar.png"
end_button_img = "imagens/sair.png"
selling_button_img = "imagens/vender.png"
upgrade_speed_img = "imagens/Speed.png"
upgrade_damage_img = "imagens/Damage.png"
upgrade_range_img = "imagens/Range.png"
tela_inicial_img = "imagens/tela_inicial.png"
HUD_img = "imagens/HUD_imagem2.png"
mapa_img = levelData.backgroundPath
vitoria_img = "imagens/tela_vitoria.png"
derrota_img = "imagens/Imagem_derrota.png"
times_speed_button_img = "imagens/acelerar.png"
pause_button_img = "imagens/pause.png"
continue_button_img = "imagens/continuar.png"


mapHeight = levelData.mapHeight
mapWidth = levelData.mapWidth
tileSize = levelData.tileSize

enemySpawnTimes = levelData.enemySpawnTimes

speed_mult = 3

max_upg_torre = 2