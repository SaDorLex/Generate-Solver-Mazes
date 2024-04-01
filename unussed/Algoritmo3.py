import numpy as np
import random

filas = 31
columnas = 31
casillas = np.zeros((filas,columnas))
act_x = 1
act_y = 1
stack = []
iteraciones = int(((filas - 1)/2)*((columnas - 1)/2))


def check_vecinos(x,y):
    vecinos = [
        (x, y - 2),
        (x + 2, y),
        (x, y + 2),
        (x - 2, y)
    ]
    vecinos_val=[]
    for i in vecinos:
        if validar_vecinos(i) and i not in stack:
            vecinos_val.append(i)
    if not vecinos_val:
        i = stack.pop()
        print(i)
        vecinos_val.append(stack.pop())
        return vecinos_val
    else:
        stack.append((x,y))
        return vecinos_val

def validar_vecinos(a):
    if a[0] < 0 or a[0] > filas - 1 or a[1] < 0 or a[1] > columnas - 1:
        return False
    else:
        return True



def crearLaberinto(x,y):
    act_x = x
    act_y = y
    i = 0
    while len(stack) < iteraciones:
        casillas[act_x][act_y] = 1
        
        vecinos = check_vecinos(act_x,act_y)

        rand = random.randrange(0,len(vecinos))

        if(validar_vecinos(vecinos[rand])):
            a = vecinos[rand]
            if act_x == a[0] and act_y < a[1]:
                casillas[a[0]][a[1]] = 1
                casillas[a[0]][a[1]-1] = 1
            if act_x == a[0] and act_y > a[1]:
                casillas[a[0]][a[1]] = 1
                casillas[a[0]][a[1]+1] = 1
            if act_y == a[1] and act_x < a[0]:
                casillas[a[0]][a[1]] = 1
                casillas[a[0]-1][a[1]] = 1
            if act_y == a[1] and act_x > a[0]:
                casillas[a[0]][a[1]] = 1
                casillas[a[0]+1][a[1]] = 1
            act_x = a[0]
            act_y = a[1]
        print(casillas)
crearLaberinto(1,1)
print(casillas)
print(stack)