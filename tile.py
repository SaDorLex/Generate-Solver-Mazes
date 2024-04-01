import sys

class Tile:
    def __init__(self, row, column, type):
        self.row = row
        self.column = column
        self.type = type

        self.checked = False
        self.visited = False
        self.inPath = False
        self.distance = sys.maxsize
        self.parentTile = None

    def equals(self, other):
        return (self.row == other.row and self.column == other.column and self.type == other.type)
    
    def to_dict(self):
        parenTile = self.parentTile
        if parenTile != None:
            parent = parenTile.to_dict()
        else:
            parent = None
        return {
            'row': self.row,
            'column': self.column,
            'type': self.type,
            'checked': self.checked,
            'visited': self.visited,
            'inPath': self.inPath,
            'distance': self.distance,
            'parentTile': parent
        }
    
    def dict_to_tile(data):
        return Tile(data['row'], data['column'], data['type'], data['checked'], data['visited'], data['inPath'], data['distance'], data['parentTile'])

