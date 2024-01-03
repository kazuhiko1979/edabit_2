function canClimb(current, next) {
    const diff = Math.abs(current - next);
    return current === next || diff === 1;
}

function canTraverse(matrix) {
    const transposed = matrix[0].map((col, i) => matrix.map(row => row[i]));
    let step = 0;
    let currentBlock = transposed[step].filter(x => x === 1).length;
    
    for (let i = 1; i < transposed.length; i++) {
        const countNextCol = transposed[i].filter(x => x === 1).length;
        if (!canClimb(currentBlock, countNextCol)) {
            return false;
        }
        step++;
        currentBlock = countNextCol;
    }

    return step === matrix[0].length - 1;
}

// Test cases
console.log(canTraverse([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0]
]));

console.log(canTraverse([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0]
]));

// Other test cases...
