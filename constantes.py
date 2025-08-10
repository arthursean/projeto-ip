from levelData import LevelData

screen_width = 1088
screen_height = 702
clk = 60
side_panel = 96

levelData = LevelData("map.json")

path = levelData.path
placebleTiles = levelData.placebleTiles

exercito_img = "imagens/teste.png"
heart_img = "imagens/heart.png"
dinheiro_img = "imagens/moeda.png"
buy_button_img = "imagens/pixil-frame-0 (1).png"
cancel_button_img = "imagens/pixil-frame-0 (2).png"
end_button_img = "imagens\pixil-frame-0 (3).png"


mapa_img = levelData.backgroundPath

mapHeight = levelData.mapHeight
mapWidth = levelData.mapWidth
tileSize = levelData.tileSize

enemySpawnTimes = levelData.enemySpawnTimes