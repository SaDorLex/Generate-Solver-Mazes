#Con Dolor y Sufrimiento trato de hacer que funcione el algoritmo de Prims en mi laberinto
#Si alguien le esto que sepa que le puse mucho cariño a este proyecto

import random
import math

class prims:
    def __init__(self,maze):
        

        for i in range(len(maze.matrix)):
            for j in range(len(maze.matrix[i])):
                maze.matrix[i][j].type = 3
    
    def camino(self,maze):
        camino = []
        tileList = []

        randomRow = math.floor(random.random() * maze.rows)
        randomCol = math.floor(random.random() * maze.columns)
        initialTile = maze.matrix[randomRow][randomCol]
        initialTile.type = 0
        initialTile.checked = True
        initialTile.visited = True

        for adjTile in maze.getAdjacent(initialTile,2):
            adjTile.checked = True
            adjTile.parentTile = initialTile
            tileList.append(adjTile)
        
        while len(tileList) > 0:
            randomIndex = math.floor(random.random() * len(tileList))
            randomTile = tileList.pop(randomIndex)

            if randomTile.visited:
                continue
            randomTile.visited = True

            editedTiles = maze.editTilesBetween(randomTile, randomTile.parentTile, 0)
            for editedTile in editedTiles:
                editedTile.visited = True
                camino.append(editedTile)

            adjTiles = []
            Tiles = maze.getAdjacent(randomTile, 2)
            for tile in Tiles:
                if tile.type == 3:
                    adjTiles.append(tile)  
            for adjTile in adjTiles:
                adjTile.checked = True
                adjTile.parentTile = randomTile
                tileList.append(adjTile)
        return camino
                
