function isExactlyThree(n) {
    let factors = [];
    let sqrtN = Math.floor(Math.sqrt(n) + 1);
    for (let i=1; i<sqrtN; i++){
        if (n % i == 0){
            factors.push(i);
            let complement = n / i;
            if (complement !== i){
                factors.push(complement);
            }
        }
        if (factors.length > 3){
            return false
        }
    }
    return factors.length == 3;
}


console.log(isExactlyThree(4));   // false
console.log(isExactlyThree(12));  // true
console.log(isExactlyThree(25));  // false
console.log(isExactlyThree(44398433));  // true
console.log(isExactlyThree(27550356289));  // true

