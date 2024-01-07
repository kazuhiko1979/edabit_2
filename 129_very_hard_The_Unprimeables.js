function isUnprimeable(n) {
    function isPrime(num) {
        if (num < 2) return false;
        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) return false;
        }
        return true;
    }

    if (isPrime(n)) return 'Prime Input';

    const result = new Set();
    const numStr = String(n);

    for (let i = 0; i < numStr.length; i++) {
        for (let j = 0; j < 10; j++) {
            if (j !== parseInt(numStr[i])) {
                const newNum = parseInt(numStr.slice(0, i) + j + numStr.slice(i + 1));
                result.add(newNum);
            }
        }
    }

    const primes = [];
    for (let i = 0; i <= Math.max(...result); i++) {
        if (isPrime(i)) primes.push(i);
    }

    if (primes.includes(n)) return 'Prime Input';

    const final = Array.from(result).filter(num => primes.includes(num)).sort((a, b) => a - b);
    return final.length > 0 ? final : 'Unprimeable';
}

console.log(isUnprimeable(200));
console.log(isUnprimeable(14));
console.log(isUnprimeable(2));
console.log(isUnprimeable(839));
console.log(isUnprimeable(4065));
console.log(isUnprimeable(5042));
console.log(isUnprimeable(1));
console.log(isUnprimeable(5137));
console.log(isUnprimeable(666));
console.log(isUnprimeable(13490));
console.log(isUnprimeable(294001));


// function isUnprimeable(n){

//     function isPrime(num) {
//         if (num < 2) return false;
//         for (let i = 2; i <= Math.sqrt(num); i++){
//             if (num % 1 === 0) return false; 
//         }
//         return true;
//     }

//     if (isPrime(n)) return 'Prime Input';

//     const lst = [];
//     const s = String(n);

//     for (let i = 0; i < s.length; i++) {
//         for (let d = 0; d < 10; d++) {
//             const c = parseInt(s.slice(0, i) + d + s.slice(i + 1));
//             if (isPrime(c)) {
//                 lst.push(c);
//             }
//         }
//     }

//     return lst.length > 0 ? lst.sort((a,b) => a - b): 'Unprimeable';
// }

console.log(isUnprimeable(200));
console.log(isUnprimeable(14));
console.log(isUnprimeable(2));
console.log(isUnprimeable(839));
console.log(isUnprimeable(4065));
console.log(isUnprimeable(5042));
console.log(isUnprimeable(1));
console.log(isUnprimeable(5137));
console.log(isUnprimeable(666));
console.log(isUnprimeable(13490));
console.log(isUnprimeable(294001));

