import math
import random

class kruskal:
    
    def __init__(self, maze):
        for i in range(len(maze.matrix)):
            for j in range(len(maze.matrix[i])):
                maze.matrix[i][j].type = 3
                maze.matrix[i][j].parentTile = maze.matrix[i][j]
    
    def camino(self, maze):
        camino = []
        numDistinctSets = math.ceil(maze.rows / 2) * math.ceil(maze.columns / 2)

        while numDistinctSets > 1:
            randomRow = math.floor(random.random() * math.ceil(maze.rows / 2)) * 2
            randomCol = math.floor(random.random() * math.ceil(maze.columns / 2)) * 2
            randomTile = maze.matrix[randomRow][randomCol]

            tileType = randomTile.type
            randomTile.type = 0
            adjTiles = []
            Tiles = maze.getAdjacent(randomTile, 2)
            for tile in Tiles:
                if self.isDistinct(randomTile, tile):
                    adjTiles.append(tile)
            randomTile.type = tileType

            if len(adjTiles) > 0:
                randomIndex = math.floor(random.random() * len(adjTiles))
                otherTile = adjTiles[randomIndex]

                editedTiles = maze.editTilesBetween(randomTile, otherTile, 0)
                for editedTile in editedTiles:
                    editedTile.visited = True
                    camino.append(editedTile)
            
                self.union(randomTile, otherTile)
                numDistinctSets = numDistinctSets - 1
        return camino
            
    def findHeadTile(self,tile):
        headTile = tile
        while not headTile.parentTile == headTile:
            headTile = headTile.parentTile
        return headTile
    
    def union(self, tile1, tile2):
        headTile1 = self.findHeadTile(tile1)
        headTile2 = self.findHeadTile(tile2)
        headTile2.parentTile = headTile1
    
    def isDistinct(self, tile1, tile2):
        headTile1 = self.findHeadTile(tile1)
        headTile2 = self.findHeadTile(tile2)
        return not (headTile1 == headTile2)
