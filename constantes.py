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
buy_button_img = "imagens/comprar.png"
cancel_button_img = "imagens/cancelar.png"
end_button_img = "imagens/sair.png"
selling_button_img = "imagens/vender.png"


mapa_img = levelData.backgroundPath

mapHeight = levelData.mapHeight
mapWidth = levelData.mapWidth
tileSize = levelData.tileSize

enemySpawnTimes = levelData.enemySpawnTimes