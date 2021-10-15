
/*
Estamos haciendo un bracket validator. Es decir, debemnos qver que si hay un corchete de apertura,
esté su correspondioente corchete de cierre.

ejemplo:_: 
input: "{ ( ) }"
output: true

input: "{ [ ( ] }"
output: false

*/

var str = " String ({} de pru ) [ eba  ( ) ]"

var str2 = " Este (String [es falli}dop)"// porque no matchea tipos

var str3 = "Este (strin[g falla{} porq]ue no cierra TODOS los pares"

function HasBalancedBrackets(string) {
    // Your code here:
    var couples = {
        "[": "]",
        "(": ")",
        "{": "}"
    }

    var aperturas = Object.keys(couples);

    var cierres = Object.values(couples);

    var miPila = [];

    var arr1 = string.split("")

    var ultimoCierre = ""

    console.log(miPila);

    for (var i = 0; i < arr1.length; i++) {
        if (aperturas.includes(arr1[i])) {
            miPila.push(couples[arr1[i]]);
            console.log(miPila);
        }
        if (cierres.includes(arr1[i])) {
            ultimoCierre = miPila.pop()
            if (arr1[i] !== ultimoCierre) return false
            console.log(miPila);
        }

    }

    return !miPila[0];

}

console.log(HasBalancedBrackets(str)) // true;

console.log(HasBalancedBrackets(str2)) // false;

console.log(HasBalancedBrackets(str3)) // false;

module.exports = HasBalancedBrackets;

// Complejidad temporal = O(n)
// Complejidad espacial = O(n)


/* ES posible usar

for (char of string)

RESPUESTA DEL PROFE

function HasBalanceBrackets(str) {
  // Escribir la funcion
  if (str[0] === ')' || str[0] === ']' || str[0] === '}') return false;

  const obj = {
    '(': ')',
    '[': ']',
    '{': '}',
  };

  const pila = [];

  for (let el of str) {
    console.log(el);
    if (obj[el]) pila.push(el);
    else if (obj[pila.pop()] !== el) return false;
  }

  // return !pila[0];
  return pila.length;
}

*/