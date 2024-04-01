var colores = ['white', 'black', 'yellow' , 'green']

var divs = document.querySelectorAll('#midiv');

divs.forEach(function(div){
    div.addEventListener('click',function(){
        color = div.style.backgroundColor;
        index = colores.indexOf(color);
        if(color == 'green'){
            index = 0;
            div.style.backgroundColor = colores[index]
            div.setAttribute('data-color', index)
        }else{
            div.style.backgroundColor = colores[index + 1]
            div.setAttribute('data-color', index + 1)
        }
        console.log(div.style.backgroundColor)
    });
});

$(document).ready(function() {
    $('.resolver').click(function(event) {
        event.preventDefault();
        
        var filas = document.querySelectorAll('.box')
        for(var i = 0; i < filas.length; i++){
            var fila = filas[i]
            var bloques = fila.querySelectorAll('.box2')
            for(var j = 0; j < bloques.length; j++){
                var bloque = bloques[j]
                if (bloque.style.backgroundColor == 'green'){
                    var startTile = { row: i, column: j};
                }
                if (bloque.style.backgroundColor == 'yellow'){
                    var destinationTile = { row: i, column: j};
                }
            }
        }
        
        $('<input>').attr({
            type: 'hidden',
            name: 'startTile',
            value: JSON.stringify(startTile)
        }).appendTo('form');
        $('<input>').attr({
            type: 'hidden',
            name: 'destinationTile',
            value: JSON.stringify(destinationTile)
        }).appendTo('form');
        $('form').submit();
    });
});

json = document.querySelector('#patron').getAttribute('value')
jsondata = JSON.parse(json)
console.log(jsondata)
camino = jsondata.map(elemento =>{
    return {
        row: elemento.row,
        column: elemento.column,
        type: elemento.type
    }
})
console.log(camino)
var filas = document.querySelectorAll('.box')
function cambiar(){
    for(var i = 0; i < filas.length; i++){
        var fila = filas[i];
        var bloques = fila.querySelectorAll('.box2');

        for(var j = 0; j < bloques.length; j++){
            var bloque = bloques[j];
            bloque.style.backgroundColor = 'black';
        }

    }
}

async function generarcamino(){
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
            bloque.style.backgroundColor = 'white'
        }
        document.getElementById('tiempo').innerText = time/1000
        await sleep(50)
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

cambiar()
generarcamino()



