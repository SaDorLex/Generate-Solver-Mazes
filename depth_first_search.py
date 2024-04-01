import numpy as np
import random
import math

class depth_first_search:
    
    def __init__(self,maze):

        for i in range(len(maze.matrix)):
            for j in range(len(maze.matrix[i])):
                maze.matrix[i][j].type = 3

    def camino(self,maze):
        stack = []
        camino = []

        randomRow = math.floor(random.random() * maze.rows)
        randomCol = math.floor(random.random() * maze.columns)
        initialTile = maze.matrix[randomRow][randomCol]

        initialTile.checked = True
        initialTile.type = 0
        stack.append(initialTile)

        while len(stack) > 0:
            currentTile = stack.pop()
            currentTile.visited = True
            
            adjTiles = []
            Tiles = maze.getAdjacent(currentTile, 2)
            for tile in Tiles:
                if tile.type != 0:
                    adjTiles.append(tile)

            if len(adjTiles) > 0:
                stack.append(currentTile)

                randomIndex = math.floor(random.random() * len(adjTiles))
                randomTile = adjTiles[randomIndex]

                for adjTile in adjTiles:
                    adjTile.checked = True
                    camino.append(adjTile)
                
                editedTiles = maze.editTilesBetween(currentTile, randomTile, 0)
                stack.append(randomTile)

                for editedTile in editedTiles:
                    editedTile.visited = True
                    camino.append(editedTile)
        return camino
