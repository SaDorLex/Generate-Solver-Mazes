from tile import Tile
import sys

class Maze:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[None] * columns for _ in range(rows)]
        self.clear()

    def getTile(self, tileType):
        for i in len(self.matrix):
            for j in len(self.matrix[i]):
                if self.matrix[i][j].type == tileType:
                    return self.matrix[i][j]
        return None
    
    def getNumTileType(self, tileType):
        count = 0
        for i in len(self.matrix):
            for j in len(self.matrix[i]):
                if self.matrix[i][j].type == tileType:
                    count =+ 1
        return count
    
    def getAdjacent(self, tile, d):
        r = tile.row
        c = tile.column
        adjacentTiles = []

        if self.tileValid(r, c) and tile.type != 3:
            if self.tileValid(r, c - d):
                adjacentTiles.append(self.matrix[r][c - d])
            if self.tileValid(r, c + d):
                adjacentTiles.append(self.matrix[r][c + d])
            if self.tileValid(r - d, c):
                adjacentTiles.append(self.matrix[r - d][c])
            if self.tileValid(r + d, c):
                adjacentTiles.append(self.matrix[r + d][c])
        
        return adjacentTiles
    
    def editTilesBetween(self, tile1, tile2, tileType):
        diff_x = tile2.column - tile1.column
        diff_y = tile2.row - tile1.row

        if diff_x != 0 and diff_y != 0:
            return []
        
        i = 0
        j = 0
        editingRow = False

        if diff_x > 0:
            i = tile1.column
            j = tile2.column
            editingRow = True
        elif diff_x < 0:
            i = tile2.column
            j = tile1.column
            editingRow = True
        elif diff_y > 0:
            i = tile1.row
            j = tile2.row
            editingRow = False
        elif diff_y < 0:
            i = tile2.row
            j = tile1.row
            editingRow = False

        editedTiles = []

        if editingRow:
            for index in range(i,j + 1):
                self.matrix[tile1.row][index].type = tileType
                #print(self.matrix[tile1.row][index].row,self.matrix[tile1.row][index].column,self.matrix[tile1.row][index].type)
                editedTiles.append(self.matrix[tile1.row][index])
        else:
            for index in range(i,j + 1):
                self.matrix[index][tile1.column].type = tileType
                #print(self.matrix[index][tile1.column],self.matrix[index][tile1.column].type)
                editedTiles.append(self.matrix[index][tile1.column])
        
        return editedTiles
            

    def tileValid(self, r, c):
        return (r >= 0 and c >= 0 and r < self.rows and c < self.columns)
    
    def clear(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix[i][j] = Tile(i,j,0)

    def resetTiles(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j].checked = False
                self.matrix[i][j].visited = False
                self.matrix[i][j].inPath = False
                self.matrix[i][j].distance = sys.maxsize
                self.matrix[i][j].parentTile = None
    
    def to_dict(self):
        return {
            'rows': self.rows,
            'columns': self.columns
        }
    
