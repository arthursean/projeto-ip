from src.levelData import LevelData

screen_width = 1088
screen_height = 702
clk = 60
side_panel = 96
turret_price = 20

levelData = LevelData("src/map.json")

path = levelData.path
placebleTiles = levelData.placebleTiles

exercito_img = "assets/imagens/teste.png"
heart_img = "assets/imagens/heart.png"
dinheiro_img = "assets/imagens/moeda.png"
play_button_img = "assets/imagens/jogar.png" 
forca_img = "assets/imagens/laursa.png"
distancia_img = "assets/imagens/oculos.png"
cooldown_img = "assets/imagens/pitu.png"
buy_button_img = "assets/imagens/comprar.png"
cancel_button_img = "assets/imagens/cancelar.png"
end_button_img = "assets/imagens/sair.png"
selling_button_img = "assets/imagens/vender.png"
upgrade_speed_img = "assets/imagens/Speed.png"
upgrade_damage_img = "assets/imagens/Damage.png"
upgrade_range_img = "assets/imagens/Range.png"
tela_inicial_img = "assets/imagens/tela_inicial.png"
HUD_img = "assets/imagens/HUD_imagem2.png"
mapa_img = levelData.backgroundPath
vitoria_img = "assets/imagens/tela_vitoria.png"
derrota_img = "assets/imagens/Imagem_derrota.png"
times_speed_button_img = "assets/imagens/acelerar.png"
pause_button_img = "assets/imagens/pause.png"
continue_button_img = "assets/imagens/continuar.png"
restart_button_img = "assets/imagens/restart.png"
titulo_img = "assets/imagens/titulo.png"
madeira_img = "assets/imagens/madeira.png"


mapHeight = levelData.mapHeight
mapWidth = levelData.mapWidth
tileSize = levelData.tileSize

enemySpawnTimes = levelData.enemySpawnTimes

speed_mult = 3

max_upg_torre = 2