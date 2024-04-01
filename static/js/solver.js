json = document.querySelector('#camino').getAttribute('value')
jsondata = JSON.parse(json)
json_path = document.querySelector('#path').getAttribute('value')
json_path_data = JSON.parse(json_path)
camino = jsondata.map(elemento =>{
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
var filas = document.querySelectorAll('.box')
async function mostrarCamino(){
    var time = 0
    for(var i = 0; i < camino.length; i++){
        time = time + 60
        path = camino[i]
        row = path.row
        column = path.column
        fila = filas[row]
        bloques = fila.querySelectorAll('.box2')
        if(path.type == 0){
            bloque = bloques[column]
            bloque.style.backgroundColor = 'orange'
        }
        document.getElementById('tiempo').innerText = time/1000
        await sleep(50)
    }
}

async function mostrarPath(){
    for(var i = 0; i < paths.length; i++){
        ruta = paths[i]
        row = ruta.row
        column = ruta.column
        fila = filas[row]
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

mostrarCamino().then(() =>{
    return mostrarPath();
})