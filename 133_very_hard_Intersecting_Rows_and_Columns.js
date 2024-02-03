function transformMatrix(matrix){
    
    const rows = matrix.length;
    const cols = matrix[0].length;

    const result = new Array(rows).fill(0).map(() => new Array(cols).fill(0));

    for (let i=0; i<rows; i++){
        for (let j=0; j<cols; j++){

            const rowSum = matrix[i].reduce((acc, val) => acc + val, 0) - matrix[i][j];
            const colSum = matrix.reduce((acc, row) => acc + row[j], 0) - matrix[i][j];

            result[i][j] = rowSum + colSum;
        }
    }
    return result;
}


// テストケース
console.log(transformMatrix([
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0]
]));

console.log(transformMatrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]));

console.log(transformMatrix([
    [1, 1, 1],
    [0, 0, 1],
    [0, 0, 1]
]));

console.log(transformMatrix([
    [1, 1, 1],
    [0, 1, 1],
    [0, 0, 1]
]));