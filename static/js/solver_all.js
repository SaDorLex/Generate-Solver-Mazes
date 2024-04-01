json_dfs = document.querySelector('#camino_dfs').getAttribute('value')
jsondata_dfs = JSON.parse(json_dfs)
json_bfs = document.querySelector('#camino_bfs').getAttribute('value')
jsondata_bfs = JSON.parse(json_bfs)
json_a_star = document.querySelector('#camino_a_star').getAttribute('value')
jsondata_a_star = JSON.parse(json_a_star)
json_path = document.querySelector('#path').getAttribute('value')
json_path_data = JSON.parse(json_path)
camino_dfs = jsondata_dfs.map(elemento =>{
    return {
        row: elemento.row,
        column: elemento.column,
        type: elemento.type,
        checked: elemento.checked
    }
})
camino_bfs = jsondata_bfs.map(elemento =>{
    return {
        row: elemento.row,
        column: elemento.column,
        type: elemento.type,
        checked: elemento.checked
    }
})
camino_a_star = jsondata_a_star.map(elemento =>{
    return {
        row: elemento.row,
        column: elemento.column,
        type: elemento.type,
        checked: elemento.checked
    }
})
paths = json_path_data.map(element =>{
    return {
        row: element.row,
        column: element.column,
        type: element.type,
        checked: element.checked
    }
})

var filas_a_star = document.querySelectorAll('.box.a_star')
var filas_bfs = document.querySelectorAll('.box.bfs')
var filas_dfs = document.querySelectorAll('.box.dfs')
async function mostrarCamino_a_star(){
    const inicio = new Date()
    var time = 0
    for(var i = 0; i < camino_a_star.length; i++){
        time = time + 60
        path = camino_a_star[i]
        row = path.row
        column = path.column
        fila = filas_a_star[row]
        bloques = fila.querySelectorAll('.box2')
        if(path.type == 0){
            bloque = bloques[column]
            bloque.style.backgroundColor = 'orange'
        }
        document.getElementById('tiempo_a_star').innerText = time/1000
        await sleep(50)
    }
    const fin = new Date()
    const tiempo = fin - inicio
    //document.getElementById('tiempo_a_star').innerText = tiempo/1000
}

async function mostrarCamino_bfs(){
    const inicio = new Date()
    var time = 0
    for(var i = 0; i < camino_bfs.length; i++){
        time = time + 60
        path = camino_bfs[i]
        row = path.row
        column = path.column
        fila = filas_bfs[row]
        bloques = fila.querySelectorAll('.box2')
        if(path.type == 0){
            bloque = bloques[column]
            bloque.style.backgroundColor = 'orange'
        }
        document.getElementById('tiempo_bfs').innerText = time/1000
        await sleep(50)
    }
    const fin = new Date()
    const tiempo = fin - inicio
    //document.getElementById('tiempo_bfs').innerText = tiempo/1000
}

async function mostrarCamino_dfs(){
    const inicio = new Date()
    var time = 0
    for(var i = 0; i < camino_dfs.length; i++){
        time = time + 60
        path = camino_dfs[i]
        row = path.row
        column = path.column
        fila = filas_dfs[row]
        bloques = fila.querySelectorAll('.box2')
        if(path.type == 0){
            bloque = bloques[column]
            bloque.style.backgroundColor = 'orange'
        }
        document.getElementById('tiempo_dfs').innerText = time/1000
        await sleep(50)
    }
    const fin = new Date()
    const tiempo = fin - inicio
    //document.getElementById('tiempo_dfs').innerText = tiempo/1000
}

async function mostrarPath(){
    for(var i = 0; i < paths.length; i++){
        ruta = paths[i]
        row = ruta.row
        column = ruta.column
        fila = filas_a_star[row]
        bloques = fila.querySelectorAll('.box2')
        if(ruta.type == 0){
            bloque = bloques[column]
            bloque.style.backgroundColor = 'purple'
        }
        fila = filas_bfs[row]
        bloques = fila.querySelectorAll('.box2')
        if(ruta.type == 0){
            bloque = bloques[column]
            bloque.style.backgroundColor = 'purple'
        }
        fila = filas_dfs[row]
        bloques = fila.querySelectorAll('.box2')
        if(ruta.type == 0){
            bloque = bloques[column]
            bloque.style.backgroundColor = 'purple'
        }
        await sleep(50)
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

Promise.all([mostrarCamino_a_star(),mostrarCamino_bfs(),mostrarCamino_dfs()]).then(() =>{
    return mostrarPath();
})