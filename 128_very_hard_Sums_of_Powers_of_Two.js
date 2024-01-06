function sums_of_powers_of_two(n) {
    let result = [];
    let power = 0;

    while (n > 0) {
        if (n & 1) {
            result.push(Math.pow(2, power))
        }
        power ++;
        n >>= 1;
    }
    return result
}

console.log(sums_of_powers_of_two(21)); // [1, 4, 16]
console.log(sums_of_powers_of_two(8));  // [8]
console.log(sums_of_powers_of_two(63)); // [1, 2, 4, 8, 16, 32]
console.log(sums_of_powers_of_two(1));  // [1]
console.log(sums_of_powers_of_two(556846320));
// [16, 32, 64, 128, 1024, 2048, 16384, 32768, 1048576, 2097152, 16777216, 536870912]