// Maximum Score From Two Parts of a String
// Given a string s formed from zeros and ones, return the maximum score after splitting the string into two non-empty substrings (left and right).

// The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

// Examples
// max_score("00111") ➞ 5
// # left = "00", right = "111" ➞ 2 + 3 ➞ 5

// max_score("1111") ➞ 3

// max_score("01001") ➞ 4

// max_score("010101010101010101") ➞ 10

function maxScore(s) {
    let zeros = 0;
    let ones = Array.from(s).filter(c => c === '1').length;
    let maxSum = zeros + ones;

    for (let char of s) {
      if (char === '0') {
        zeros += 1;
        ones -= 1;
      } else {
        let temp = zeros+ ones;
        maxSum = Math.max(maxSum, temp);
      }
    }
  return maxSum;
}


// 例のテストケース
console.log(maxScore("011101")); // 4
console.log(maxScore("00111")); // 5
console.log(maxScore("1111")); // 3
console.log(maxScore("00")); // 0
console.log(maxScore("01001")); // 4
console.log(maxScore("010101010101010101")); // 10
console.log(maxScore("01")); // 1
console.log(maxScore("1110010101")); // 5
console.log(maxScore("10")); // 1
console.log(maxScore("1100110010010111100000111001000111101111100011100111001101010100011001000000001111000000010000111101"));



