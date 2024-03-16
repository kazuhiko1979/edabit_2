function calculateBowlingScore(rolls){
    let totalScore = 0;
    let rollIndex = 0;
    let frame = 1;

    while (frame <= 10){ // 10フレームまで繰り返す
        if (rolls[rollIndex] === 10){ // ストライクの場合
            totalScore += 10;
            totalScore += rolls[rollIndex + 1] + rolls[rollIndex + 2];
            rollIndex += 1;
        } else if (rolls[rollIndex] + rolls[rollIndex + 1] === 10) { // スペアの場合
            totalScore += 10;
            totalScore += rolls[rollIndex + 2];
            rollIndex += 2;
        } else {
            totalScore += rolls[rollIndex] + rolls[rollIndex + 1];
            rollIndex += 2
        }
        frame ++;
    }
    return totalScore;
}

// テストケースの実行
console.log(calculateBowlingScore([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]));  // ➞ 300
console.log(calculateBowlingScore([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]));  // ➞ 80
console.log(calculateBowlingScore([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]));  // ➞ 150
console.log(calculateBowlingScore([10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10]));  // ➞ 200
console.log(calculateBowlingScore([10, 0, 10, 7, 2, 10, 10, 10, 8, 2, 9, 1, 7, 2, 10, 10, 5]));  // ➞ 194
console.log(calculateBowlingScore([8, 0, 8, 2, 10, 10, 7, 3, 9, 1, 7, 2, 10, 10, 9, 0]));  // ➞ 177