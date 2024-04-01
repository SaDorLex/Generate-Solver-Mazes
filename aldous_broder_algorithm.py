from maze import Maze
import math
import random

class aldous_broder:
    def __init__(self, maze):
        
        for i in range(len(maze.matrix)):
            for j in range(len(maze.matrix[i])):
                maze.matrix[i][j].type = 3
                
    def camino(self,maze):
        camino = []
        randomRow = math.floor(random.random() * maze.rows)
        randomCol = math.floor(random.random() * maze.columns)
        initialTile = maze.matrix[randomRow][randomCol]
        initialTile.type = 0
        initialTile.visited = True
        initialTile.checked = True

        numRowTiles = 0
        numColTiles = 0
        for i in range(randomRow, -1, -2):
            numRowTiles += 1
        for i in range(randomRow + 2, maze.rows, +2):
            numRowTiles += 1
        for i in range(randomCol, -1, -2):
            numColTiles += 1
        for i in range(randomCol + 2, maze.columns, +2):
            numColTiles += 1
        unvisitedTiles = (numRowTiles * numColTiles) - 1
        currentTile = initialTile

        while(unvisitedTiles > 0):
            adjTiles = maze.getAdjacent(currentTile, 2)
            randomIndex = math.floor(random.random() * len(adjTiles))
            randomTile = adjTiles[randomIndex]
            if randomTile.type != 0:
                editedTiles = maze.editTilesBetween(currentTile, randomTile, 0)
                unvisitedTiles -= 1
                for i in range(len(editedTiles)):
                    camino.append(editedTiles[i])
            currentTile = randomTile
        return camino
