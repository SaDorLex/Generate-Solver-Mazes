from maze import Maze
from aldous_broder_algorithm import aldous_broder
from solver_bfs import bfs

laberinto = Maze(10,10)

def reconstructPath(maze, star, destination):
    count = 0

    currentTile = destination
    destination.inPath = True

    while not currentTile == star:
        currentTile = maze.matrix[currentTile.parentTile.row][currentTile.parentTile.column]
        currentTile.inPath = True
    count += 1

laberinto.resetTiles()
generador = aldous_broder(laberinto)
camino = generador.camino(laberinto)
for i in range(laberinto.rows):
    for j in range(laberinto.columns):
        tile = laberinto.matrix[i][j]
        print(tile.type, end=" ")
    print("\n")
solver = bfs()
solver.encontrar(laberinto, laberinto.matrix[1][1], laberinto.matrix[9][9])
reconstructPath(laberinto, laberinto.matrix[1][1], laberinto.matrix[9][9])
for i in range(laberinto.rows):
    for j in range(laberinto.columns):
        tile = laberinto.matrix[i][j]
        print(tile.inPath, end=" ")
    print("\n")