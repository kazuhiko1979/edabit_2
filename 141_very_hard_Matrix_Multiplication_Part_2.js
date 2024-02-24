function matrix_multiply(a, b){

    if (a[0].length != b.length){
        return "invalid";
    }

    // Initialzie the result matrix with zeros
    let result = new Array(a.length);
    for (let i = 0; i < a.length; i++){
        result[i] = new Array(b[0].length).fill(0);
    }

    // Perform matrix multiplication
    for(let i = 0; i < a.length; i++){
        for (let j = 0; j < b[0].length; j++){
            for (let k = 0; k < b.length; k++){
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }

    return result;
}

// Test cases
console.log(matrix_multiply([[1, 2]], [[3], [4]])); // ➞ [[11]]
console.log(matrix_multiply([[0, 0], [0, 1]], [[1, 2], [3, 4], [5, 6]])); // ➞ "invalid"
console.log(matrix_multiply([[4, 2], [3, 1]], [[5, 6], [3, 8]])); // ➞ [[26, 40], [18, 26]]