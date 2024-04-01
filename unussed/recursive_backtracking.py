import pygame
import random
import time

visited = []
walls = []
invalid_walls = []

width = 500
height = 500
cell = 25
background_color = (0,0,0)
wall_color = (255, 255, 255)
trace_color = (50, 50, 50)
head_color = (112,9,156)

x_pos, y_pos = random.randint(0,(width//cell)-1), random.randint(0,(height//cell)-1)
start_position = (x_pos, y_pos)

window = pygame.display.set_mode((width+1,height+1))
window.fill(background_color)

#Generate Grid
for i in range(0, width+cell, cell):
    pygame.draw.line(window, wall_color, (0, i), (width, i))
    pygame.draw.line(window, wall_color, (i, 0), (i, height))
    c = 0
    for x in range(width//cell):
        if i == 0 or i == width:
            invalid_walls.append([(c,i),(c+cell,i)]) #Horizontal walls
            invalid_walls.append([(i,c),(i,c+cell)]) #Vertical walls
            c += cell
        else:
            walls.append([(c,i),(c+cell,i)]) #Horizontal walls
            walls.append([(i,c),(i,c+cell)]) #Vertical walls
            c += cell
pygame.display.update()


#This function will return a valid neighbour, or False if there is not a valid one
def choose_neighbour(position, v_wall_left, v_wall_right, h_wall_top, h_wall_bottom):
    valid_neighbours = []
    x_pos = position[0]
    y_pos = position[1]
    if (v_wall_left not in invalid_walls) and ((x_pos-1, y_pos) not in visited):
        valid_neighbours.append([(x_pos-1 ,y_pos), v_wall_left])
    if (v_wall_right not in invalid_walls) and ((x_pos+1, y_pos) not in visited):
        valid_neighbours.append([(x_pos+1 ,y_pos), v_wall_right])
    if (h_wall_top not in invalid_walls) and ((x_pos, y_pos-1) not in visited):
        valid_neighbours.append([(x_pos ,y_pos-1), h_wall_top])
    if (h_wall_bottom not in invalid_walls) and ((x_pos, y_pos+1) not in visited):
        valid_neighbours.append([(x_pos ,y_pos+1), h_wall_bottom])

    if len(valid_neighbours) == 0:
        return False
    else:
        return random.choice(valid_neighbours)

#Recursive function for moving the head
def move(position):
    x_pos = position[0]
    y_pos = position[1]

    #Draw Starting position
    rect = pygame.Rect((x_pos*cell)+1,(y_pos*cell)+1, cell-1, cell-1)
    pygame.draw.rect(window, trace_color, rect)
    visited.append(start_position)

    v_wall_left = [((x_pos*cell), (y_pos*cell)), ((x_pos*cell), (y_pos*cell)+cell)]
    v_wall_right = [((x_pos*cell)+cell, (y_pos*cell)), ((x_pos*cell)+cell, (y_pos*cell)+cell)]
    h_wall_top = [((x_pos*cell), (y_pos*cell)), ((x_pos*cell)+cell, (y_pos*cell))]
    h_wall_bottom = [((x_pos*cell), (y_pos*cell)+cell), ((x_pos*cell)+cell, (y_pos*cell)+cell)]

    while choose_neighbour(position, v_wall_left, v_wall_right, h_wall_top, h_wall_bottom) != False:
        new_cell_position, wall = choose_neighbour(position, v_wall_left, v_wall_right, h_wall_top, h_wall_bottom)

        #Draw Head and erase walls
        head_rect = pygame.Rect((new_cell_position[0]*cell)+1,(new_cell_position[1]*cell)+1, cell-1, cell-1)
        pygame.draw.rect(window, trace_color, head_rect) #Change head color for trace color to alternate
        pygame.draw.line(window, trace_color, wall[0], wall[1])

        #Fill black spaces between erased walls
        window.set_at((wall[0][0], wall[0][1]), wall_color)
        window.set_at((wall[0][0], wall[1][1]), wall_color)
        window.set_at((wall[1][0], wall[0][1]), wall_color)
        window.set_at((wall[1][0], wall[1][1]), wall_color)

        pygame.display.update()
        visited.append(new_cell_position)
        invalid_walls.append(wall)

        #Slow Down
        time.sleep(0.03)

        move(new_cell_position)

    return False
time.sleep(5)
#Call recursive function
move(start_position)

while pygame.event.wait().type != pygame.QUIT:
    pass
