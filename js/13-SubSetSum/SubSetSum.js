
function prueba(a, b, target) {
    return (a + b) > target
}

function suma(arr) {
    arr.reduce((a, b) => a + b, 0);
}
/*
[ 1,  3, 6,  9, 22, 34, 51]


["x",  "x"                        ]      []


[ 1   "x"                         ]      [0]


["x",  3                          ]      [1]


[ 1    3                          ]      [0, 1]


*/


function subsetSum(nums, target, indiceActual = 0, sumaActual = 0, indices = [], resultado = []) {
    // Your code here:

    for (var i = indiceActual; i < nums.length; i++) {

        //si decido no argegarlo
        if (i < sums.lenght - 1) subsetSums(nums, target, i + 1, sumaActual, indices, resultado)

        //si decide agregarlo al array
        if (i > target) return;
        else if (sumaActual + i === target) {
            sumaActual = i + sumaActual;
            indices.push(i);
            resultado.push(indices);
            return
        }
        else {
            sumaActual = i + sumaActual;
            indices.push(i);
            subsetSums(nums, target, i, sumaActual, indices, resultado)
            return
        }

    }

    console.log(resultado)

}

module.exports = subsetSum;


/*

const subsetSumRec = (nums, target, index = 0) => {
    if (target === 0) return true;
    if (target < 0) return false;
    if (index > nums.length) return false;
    const whenExcluded = subsetSumRec(nums, target, index + 1)
    const whenIncluded = subsetSumRec(nums, target - nums[index], index + 1);
    return whenExcluded || whenIncluded
}

console.log(subsetSumRec([1, 10, 5, 3], 9))

*/
/*
function subsetSum(nums, target) {
    // Your code here:
    //subsetSum([1, 10, 5, 3], 9)
    //[0, 1, 5, 6, 3, 4, 8]
      const sums = [0];
      return nums.some((num) => {//itera y a su vez devuelve un booleano
          const copySums = [...sums];//spread operator
          return copySums.some(sum => {
              const newSum = sum + num;
              if (target === newSum) return true;
              if (newSum < target) sums.push(newSum);
          });
      });
    }

    console.log(subsetSum([1, 10, 5, 3], 9))
}
*/

