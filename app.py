from flask import Flask, flash, redirect, render_template, request, session, url_for
import json
from depth_first_search import depth_first_search
from solver_dfs import dfs
from solver_bfs import bfs
from tile import Tile
from maze import Maze
from priorityQueue import PriorityQueue, QueueElement
from aldous_broder_algorithm import aldous_broder
from solver_a_star import A_star
from prims import prims
from kruskal import kruskal

app = Flask(__name__)
app.secret_key = 'clave_secreta'
laberinto_main = []

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('Principal.html')

@app.route('/crear_matriz', methods=['GET','POST'])
def crear_matriz():
    filas = 0
    columnas = 0

    if request.method == 'POST':
        filas = int(request.form['filas'])
        columnas = int(request.form['columnas'])
    return render_template('Principal.html', filas=filas, columnas=columnas)

@app.route('/subir_matriz',methods=['GET','POST'])
def resolver_matriz():
    if request.method == 'POST':
        matriz = json.loads(request.form['matriz'])
    return render_template('laberinto.html', matriz=matriz)

@app.route('/generador_dfs')
def generador_dfs():
    return render_template('generate_dfs.html')

@app.route('/generador_prims')
def generador_prims():
    return render_template('generate_prims.html')

@app.route('/generador_abbr')
def generador_abbr():
    return render_template('generate_ab_br.html')

@app.route('/generador_kruskal')
def generador_kruskal():
    return render_template('generate_kruskal.html')

@app.route('/solver_dfs')
def solver_dfs():
    return render_template('solver_dfs.html')

@app.route('/solver_bfs')
def solver_bfs():
    return render_template('solver_bfs.html')

@app.route('/solver_a_star')
def solver_a_star():
    return render_template('solver_a_star.html')

@app.route('/resolver_maze', methods=['GET','POST'])
def resolver_maze():
    if request.method == 'POST':
        option = request.form['selected']
        lista_lab = json.loads(request.form['lab'])
        startTile = json.loads(request.form['startTile'])
        destinationTile = json.loads(request.form['destinationTile'])
        filas = lista_lab[0]['rows']
        columnas = lista_lab[0]['columns']
        laberinto = Maze(filas, columnas)
        laberinto.resetTiles()
        lista_lab.pop(0)
        for i in range(len(lista_lab)):
            tile_text = lista_lab[i]
            laberinto.matrix[tile_text['row']][tile_text['column']].row = tile_text['row']
            laberinto.matrix[tile_text['row']][tile_text['column']].column = tile_text['column']
            laberinto.matrix[tile_text['row']][tile_text['column']].type = tile_text['type']
            laberinto.matrix[tile_text['row']][tile_text['column']].checked = tile_text['checked']
            laberinto.matrix[tile_text['row']][tile_text['column']].visited = tile_text['visited']
            laberinto.matrix[tile_text['row']][tile_text['column']].inPath = tile_text['inPath']
            laberinto.matrix[tile_text['row']][tile_text['column']].distance = tile_text['distance']
            laberinto.matrix[tile_text['row']][tile_text['column']].parentTile = tile_text['parentTile']
        matriz = [[None] * columnas for _ in range(filas)]
        for i in range(laberinto.rows):
            for j in range(laberinto.columns):
                matriz[i][j] = laberinto.matrix[i][j].type
        if option == 'dfs':
            solver = dfs()
        elif option == 'bfs':
            solver = bfs()
        elif option == 'a-star':
            solver = A_star()
        elif option == 'comparar':
            solver_dfs = dfs()
            solver_bfs = bfs()
            solver_a_star = A_star()
            camino_dfs = solver_dfs.encontrar(laberinto, laberinto.matrix[startTile['row']][startTile['column']], laberinto.matrix[destinationTile['row']][destinationTile['column']])
            laberinto.resetTiles()
            camino_bfs = solver_bfs.encontrar(laberinto, laberinto.matrix[startTile['row']][startTile['column']], laberinto.matrix[destinationTile['row']][destinationTile['column']])
            laberinto.resetTiles()
            camino_a_star = solver_a_star.encontrar(laberinto, laberinto.matrix[startTile['row']][startTile['column']], laberinto.matrix[destinationTile['row']][destinationTile['column']])
            solucion = reconstructPath(laberinto, laberinto.matrix[startTile['row']][startTile['column']], laberinto.matrix[destinationTile['row']][destinationTile['column']])
            camino_json_dfs = []
            camino_json_bfs = []
            camino_json_a_star = []
            for i in camino_dfs:
                i.parentTile = None
                camino_json_dfs.append(i.to_dict())
            camino_json_dfs = json.dumps(camino_json_dfs)
            for i in camino_bfs:
                i.parentTile = None
                camino_json_bfs.append(i.to_dict())
            camino_json_bfs = json.dumps(camino_json_bfs)
            for i in camino_a_star:
                i.parentTile = None
                camino_json_a_star.append(i.to_dict())
            camino_json_a_star = json.dumps(camino_json_a_star)
            path_json = []
            for i in solucion:
                i.parentTile = None
                path_json.append(i.to_dict())
            path_json = json.dumps(path_json)
            return render_template('comparacion.html', matriz = matriz, camino_dfs = camino_json_dfs, camino_bfs = camino_json_bfs, camino_a_star = camino_json_a_star, path = path_json)
        camino = solver.encontrar(laberinto, laberinto.matrix[startTile['row']][startTile['column']], laberinto.matrix[destinationTile['row']][destinationTile['column']])
        solucion = reconstructPath(laberinto, laberinto.matrix[startTile['row']][startTile['column']], laberinto.matrix[destinationTile['row']][destinationTile['column']])
        camino_json = []
        for i in camino:
            i.parentTile = None
            camino_json.append(i.to_dict())
        camino_json = json.dumps(camino_json)
        path_json = []
        for i in solucion:
            i.parentTile = None
            path_json.append(i.to_dict())
        path_json = json.dumps(path_json)
        if option == 'dfs':
            return render_template('solver_dfs.html', matriz = matriz, camino = camino_json, path = path_json)
        elif option == 'bfs':
            return render_template('solver_bfs.html', matriz = matriz, camino = camino_json, path = path_json)
        elif option == 'a-star':
            return render_template('solver_a_star.html', matriz = matriz, camino = camino_json, path = path_json)

@app.route('/generar_maze_abbr', methods=['GET','POST'])
def generar_abbr():
    if request.method == 'POST':
        filas = int(request.form['filas']) 
        columnas = int(request.form['columnas'])
        matriz = [[None] * columnas for _ in range(filas)]
        laberinto = Maze(filas,columnas)
        laberinto.resetTiles()
        laberinto_json = []
        laberinto_json.append(laberinto.to_dict())
        generar = aldous_broder(laberinto)
        camino = generar.camino(laberinto)
        camino_json = []
        laberinto.resetTiles()
        for i in range(laberinto.rows):
            for j in range(laberinto.columns):
                laberinto_json.append(laberinto.matrix[i][j].to_dict())
                matriz[i][j] = laberinto.matrix[i][j].type
        for i in camino:
            camino_json.append(i.to_dict())
        camino_json = json.dumps(camino_json)
        laberinto_json = json.dumps(laberinto_json)
    return render_template('generate_ab_br.html', matriz=matriz, camino = camino_json, lab = laberinto_json)

#Generación de DFS
@app.route('/generar_maze_dfs', methods=['GET','POST'])
def generar_dfs():
    if request.method == 'POST':
        filas = int(request.form['filas']) 
        columnas = int(request.form['columnas'])
        matriz = [[None] * columnas for _ in range(filas)]
        laberinto = Maze(filas,columnas)
        laberinto.resetTiles()
        laberinto_json = []
        laberinto_json.append(laberinto.to_dict())
        generar = depth_first_search(laberinto)
        camino = generar.camino(laberinto)
        camino_json = []
        laberinto.resetTiles()
        for i in range(laberinto.rows):
            for j in range(laberinto.columns):
                laberinto.matrix[i][j].parentTile = None
                laberinto_json.append(laberinto.matrix[i][j].to_dict())
                matriz[i][j] = laberinto.matrix[i][j].type
        for i in camino:
            i.parentTile = None
            camino_json.append(i.to_dict())
        camino_json = json.dumps(camino_json)
        laberinto_json = json.dumps(laberinto_json)
    return render_template('generate_dfs.html', matriz=matriz, camino = camino_json, lab = laberinto_json)


@app.route('/generar_maze_prims', methods=['GET','POST'])
def generar_prims():
    if request.method == 'POST':
        filas = int(request.form['filas']) 
        columnas = int(request.form['columnas'])
        matriz = [[None] * columnas for _ in range(filas)]
        laberinto = Maze(filas,columnas)
        laberinto.resetTiles()
        laberinto_json = []
        laberinto_json.append(laberinto.to_dict())
        generar = prims(laberinto)
        camino = generar.camino(laberinto)
        camino_json = []
        laberinto.resetTiles()
        for i in range(laberinto.rows):
            for j in range(laberinto.columns):
                laberinto.matrix[i][j].parentTile = None
                laberinto_json.append(laberinto.matrix[i][j].to_dict())
                matriz[i][j] = laberinto.matrix[i][j].type
        for i in camino:
            i.parentTile = None
            camino_json.append(i.to_dict())
        camino_json = json.dumps(camino_json)
        laberinto_json = json.dumps(laberinto_json)
    return render_template('generate_prims.html', matriz=matriz, camino = camino_json, lab = laberinto_json)

@app.route('/generar_maze_kruskal', methods=['GET','POST'])
def generar_kruskal():
    if request.method == 'POST':
        filas = int(request.form['filas']) 
        columnas = int(request.form['columnas'])
        matriz = [[None] * columnas for _ in range(filas)]
        laberinto = Maze(filas,columnas)
        laberinto.resetTiles()
        laberinto_json = []
        laberinto_json.append(laberinto.to_dict())
        generar = kruskal(laberinto)
        camino = generar.camino(laberinto)
        camino_json = []
        laberinto.resetTiles()
        for i in range(laberinto.rows):
            for j in range(laberinto.columns):
                laberinto.matrix[i][j].parentTile = None
                laberinto_json.append(laberinto.matrix[i][j].to_dict())
                matriz[i][j] = laberinto.matrix[i][j].type
        for i in camino:
            i.parentTile = None
            camino_json.append(i.to_dict())
        camino_json = json.dumps(camino_json)
        laberinto_json = json.dumps(laberinto_json)
    return render_template('generate_kruskal.html', matriz=matriz, camino = camino_json, lab = laberinto_json)

def reconstructPath(maze, star, destination):
    path = []
    count = 0

    currentTile = destination
    destination.inPath = True
    path.append(currentTile)
    while not currentTile == star:
        currentTile = maze.matrix[currentTile.parentTile.row][currentTile.parentTile.column]
        currentTile.inPath = True   
        path.append(currentTile)
        count += 1
    return path

if __name__ == '__main__':
    app.run(debug=True)