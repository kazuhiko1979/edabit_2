function diamondSum(n){

    let total = 0;
    let nList = Array.from({ length: n }, (_, j) =>
         Array.from({ length: n }, (_, i) => 
         i + 1 + j * n));

    // 中央の値を加算
    total += nList[0][Math.floor(n / 2)];
    total += nList[n-1][Math.floor(n / 2)];

    let leftSide = Math.floor(n / 2);
    let rightSide = Math.floor(n / 2);

    // 左右の対角線の値を加算
    for (let row = 1; row < n -1; row++){
        if (row <= Math.floor(n / 2)){
            leftSide--;
            rightSide++;
        } else {
            leftSide++;
            rightSide--;
        }
        total += nList[row][leftSide];
        total += nList[row][rightSide];
    }
    return total;
}

// テスト
console.log(diamondSum(1));  // 1
console.log(diamondSum(3));  // 20
console.log(diamondSum(5));  // 104
console.log(diamondSum(7));  // 300
console.log(diamondSum(9));  // 656