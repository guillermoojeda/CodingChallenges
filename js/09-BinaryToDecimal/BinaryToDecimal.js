
function BinaryToDecimal(binary) {
    // Your code here:

    /*
    if (typeof (binary) !== "string") {
        var str = binary.toString();
    } else {
        var str = binary;
    }

    for (var i = 0; i < str.length; i++) {
        var posicion = str.length - i - 1;
        var toAdd = Number(str[i]) * (2 ** posicion);
        console.log(toAdd);
        result = result + toAdd;

    }

    console.log(result);
    */

    //  recursion

    /*
    if (typeof (binary) !== "string") {
        var str = binary.toString();
    } else {
        var str = binary;
    }

    if (str.length === 1) {
        return Number(str);
    }
    else {
        var posicion = str.length - 1;
        var newStr = str.slice(1);
        return Number(str[0]) * (2 ** posicion) + BinaryToDecimal(newStr)
    }
    */



    // Con una sóla línea
    // Debo asumir, entonces, que se ingresa un String...
    /*
    return binary.split("").reverse().reduce((acumulador, num, currentIndex) => { return Number(num) * (2 ** currentIndex) + acumulador }, 0)
    */
    // Con una sóla línea y ternario_

    var num = binary
    const BinarioaDecimal = num => num.split('').reverse().reduce((acc, el, i) => (el === '1') ? acc + Math.pow(2, i) : acc, 0);
    console.log(BinaryToDecimal)



    /*
        // 11001                    0 ---> 0
        
        01 ----- 1
        10 ----- 2
        11 ----- 3  --- (  numero1 * 2 ^ posicion(1)  +  numero1 * ( 2 ^ posicion(0) ) =  2 + 1  = 3   )
        100 ---- 4 ---- (  numero1 * 2 ^ posicion(2)  +          0         +         0    =   4  )
        110 ---- 6 ---- (  numero1 * 2 ^ posicion(2)  +  numero(1) * ( 2 ^ posicion(1) ) +  0    =      )                                                     )
    
    
        // (poscion*numero) ^ 2 
    
    */

}

console.log(BinaryToDecimal("1011"));

module.exports = BinaryToDecimal;
