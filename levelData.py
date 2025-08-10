import json

class LevelData:
    def __init__(self, jsonPath):
        self.jsonPath = jsonPath
        with open(jsonPath, 'r') as file:
            self.jsonInfo = json.load(file)
        
        self.tileSize = self.jsonInfo["tileSize"]
        self.mapWidth = self.jsonInfo["mapWidth"]
        self.mapHeight = self.jsonInfo["mapHeight"]
        self.path = self.formatPath(self.jsonInfo["path"])
        self.enemySpawnTimes = self.createTimeline(self.jsonInfo["enemySpawnTimes"])
        self.backgroundPath = self.jsonInfo["backgroundPath"]
        self.placingTileId = self.jsonInfo["placingTileId"]
        self.placebleTiles = self.getPlaceableMatrix(self.jsonInfo["layers"][0]["tiles"],
                                                     self.mapWidth, self.mapHeight, 
                                                     self.placingTileId) 
    def getPlaceableMatrix(self, data, w, h, valId):
        matrix = [[0 for i in range(w)] for j in range(h)]

        for i in data:
            matrix[i["y"]][i["x"]] = 1 if i["id"] == valId else 0
        return matrix

    def formatPath(self, m_path):
        return [(i[0]*self.tileSize + (self.tileSize//2), i[1]*self.tileSize + (self.tileSize//2)) for i in m_path]
    
    def createTimeline(self, info):
        time_prog = sorted((i[1], i[0]) for i in info)

        time_prog_dict = {}
        for i in time_prog:
            time_prog_dict[i[0]] = time_prog_dict.get(i[0], [])
            time_prog_dict[i[0]].append(i[1])

        return time_prog_dict