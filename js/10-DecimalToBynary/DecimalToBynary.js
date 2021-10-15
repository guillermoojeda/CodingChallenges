

function DecimalToBynary(num) {
    // Your code here:
    var res = '';
    while (num > 0) {
        res = num % 2 + res;
        num = Math.floor(num / 2)
    }

    return res;
}

console.log(DecimalToBynary(26)); // 11010

function dtbRec(num, str = '') {

    if (num) {
        var newNum = Math.floor(num / 2);
        str = num % 2 + str;
        return dtbRec(newNum, str);
    }

    return str
}

console.log(dtbRec(26)); // 11010


var dtbRec2 = num => {
    if (num) return dtbRec2(Math.floor(num / 2)) + num % 2;
    return '';
}

console.log(dtbRec2(26)); // 11010

/*
Complejidad temporal para los 3 algoritmos: O(log(n)), o más precisamente O log2 N
Complejidad espacial para los 3 algoritmos: O(1) o O(log(n)), así que no sé...

*/

module.exports = DecimalToBynary;
