from priorityQueue import PriorityQueue, QueueElement
import math
import sys

class A_star:

    def encontrar(self,maze,startTile,destinationTile):

        pq = PriorityQueue()
        camino = []
        pq.enqueue( QueueElement(startTile, self.getHeuristic(startTile, destinationTile)))
        startTile.checked = True
        startTile.distance = 0

        while not pq.isEmpty():
            currentTile = pq.dequeue().element
            if currentTile.visited:
                continue
            currentTile.visited = True

            adjTiles = []
            Tiles = maze.getAdjacent(currentTile, 1)
            for tile in Tiles:
                if tile.type != 3:
                    adjTiles.append(tile)
            for adjTile in adjTiles:
                if adjTile == destinationTile:
                    adjTile.parentTile = currentTile
                    camino.append(adjTile)
                    return camino
                elif adjTile.distance == sys.maxsize or currentTile.distance + 1 < adjTile.distance:
                    adjTile.distance = currentTile.distance + 1
                    value = adjTile.distance + self.getHeuristic(adjTile, destinationTile)

                    pq.enqueue( QueueElement(adjTile,value))
                    adjTile.checked = True
                    adjTile.parentTile = currentTile
                    camino.append(adjTile)
        return False

    def getHeuristic(self, tile, destinationTile):
        return (abs(tile.row - destinationTile.row) + abs(tile.column - destinationTile.column))
