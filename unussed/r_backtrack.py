import random

class backtrack:

    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.maze = [[1] * width for _ in range(height)]
        self.visited = set()

    def choose_neighbour(self,position):
        x, y = position
        neighbours = [(x-2, y), (x+2, y), (x, y-2), (x, y+2)]
        valid_neighbours = [n for n in neighbours if 0 <= n[0] < self.width and 0 <= n[1] < self.height and n not in self.visited]
        return random.choice(valid_neighbours) if valid_neighbours else None
    
    def move(self,position):
        x, y = position
        self.maze[y][x] = 0
        self.visited.add(position)

        while True:
            neighbour = self.choose_neighbour(position)
            if not neighbour:
                return
            nx, ny = neighbour
            wall_x = (x + nx) // 2
            wall_y = (y + ny) // 2
            self.maze[wall_y][wall_x] = 0

            self.move(neighbour)
    
    def generate_maze(self):
        position = (random.randrange(0, self.width, 2), random.randrange(0, self.height, 2))
        self.move(position)
        return self.maze