// fuerza bruta
function intersection(arr1, arr2) {
    // Your code here:
    var arr3 = [];
    for (var i = 0; i < arr1.lenght; i++) {
        for (var j = 0; j < arr2.length; j++) {
            if (arr1[i] === arr2[j]) arr3.push(i)
        }
    }
    return arr3;
}

// búsqueda inteligente, asumiendo que los dos arrays están ordenados.
// O(n*m)
// O(n)

function intersection2(arr1, arr2) {
    // Your code here:
    let result = [];
    while (arr1.length && arr2.length) {
        if (arr1[0] === arr2[0]) {
            result.push(arr1.shift());
            arr2.shift();
            continue;
        }
        if (arr1[0] > arr2[0]) arr2.shift();
        if (arr2[0] > arr1[0]) arr1.shift();
    }
    return result
}

//O(n+m)
//O(n)

// Asumiendo que ambos arrelos están desordeados:

// Usar memorización.
// Usar reduce y filter.



function intersection4(arr1, arr2) {
    // Escribir la funcion
    let newArr = [];

    for (let i = 0; i < arr1.length; i++) {
        for (let j = 0; j < arr2.length; j++) {
            if (arr1[i] === arr2[j]) newArr.push(arr1[i]);
        }
    }

    return newArr;
}



module.exports = intersection;
