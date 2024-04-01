from tile import Tile
class bfs:
    def __init__(self):
        self.__init__ = self
        
    def encontrar(self, maze, startTile, destinationTile):
        queue = []
        camino = []
        startTile.visited = True
        startTile.checked = True
        queue.append(startTile)

        while(len(queue) > 0):

            currenTile = queue.pop(0)
            currenTile.visited = True
            
            adjTiles = []
            Tiles = maze.getAdjacent(currenTile, 1)
            for tile in Tiles:
                if not tile.checked and tile.type != 3:
                    adjTiles.append(tile)
            for adjTile in adjTiles:
                if not adjTile.checked and adjTile.type != 3:
                    adjTile.parentTile = currenTile

                    if adjTile == destinationTile:
                        return camino
                    else:
                        adjTile.checked = True
                        camino.append(adjTile)
                        queue.append(adjTile)
        
        return False
