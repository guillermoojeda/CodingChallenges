/*
function FindWordStartingWith(book, query) {
    // Your code here:
    
    //Para este caso, podemos asumir que no habrán caracteres especiales además de espacio.
    

}

text = 'Erase una vez un libro de palabras que era un poco aburrido pero tenia muchas'
const book = {
    id: 1,
    text: 'Erase una vez un libro de palabras que era un poco aburrido pero tenia muchas'
}
*/

FindWordStartingWith(book, "un") // [8, 14, 43]



/*
    var book = book.toLowerCase();
    var query = query.toLowerCase();

    var indexArr = []

    for (var i = 0; i < book.lenght; i++) {
        if (book[i] = " " || i === 0) {
            for (j = i)
        }
    }

}


*/
module.exports = FindWordStartingWith;

// Solución del profesor

function findWordsStartingWith(text, str) {
    // Escribir la funcion
    text = text.toLowerCase();
    let indexArr = [];

    const obj = {
        '¡': true,
        '¿': true,
        '.': true,
        '"': true,
        "'": true,
        ',': true,
        '!': true,
        '?': true,
    };
    for (let i = 0; i < text.length; i++) {
        if (i === 0 || text[i - 1] === ' ' || obj[text[i - 1]]) {
            for (let j = 0; j < str.length; j++) {
                if (str[j] !== text[i + j]) {
                    i += j;
                    break;
                };
                if (j === str.length - 1) {
                    indexArr.push(i);
                    i += j;
                }
            }
        }
    }

    return indexArr;
};
//Complejiidad: O(n)

console.log(FindWordStartingWith(book, "un"));