from tile import Tile
class dfs:

    def __init__(self):
        self.__init__ = self
        
    def encontrar(self,maze,starTile, destinationTile):
        stack = []
        camino = []

        starTile.checked = True
        starTile.visited = True
        stack.append(starTile)
        camino.append(starTile)

        while len(stack) > 0:

            currentTile = stack.pop()
            currentTile.visited = True
            camino.append(currentTile)

            adjTiles = []
            Tiles = maze.getAdjacent(currentTile, 1)
            for tile in Tiles:
                if not tile.checked and tile.type != 3:
                    adjTiles.append(tile)
            for adjTile in adjTiles:
                adjTile.parentTile = currentTile

                if adjTile == destinationTile:
                    return camino
                else:
                    adjTile.checked = True
                    stack.append(adjTile)
                    camino.append(adjTile)
        return False
                
