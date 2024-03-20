function order(lst){
    const key_sorted = lst.map((val, i) => 
        [val, i]).sort(([val1], [val2]) => val1 - val2);
        return key_sorted.map(([_, i]) => i);
}

// Examples
console.log(order([1, 3, 3, 9, 8]));
console.log(order([9, 1, 4, 5, 4]));
console.log(order([1, 1, 1, 1, 1]));
console.log(order([1, 2, 0, 3, 7, 1, 11, 1, 2]));
console.log(order([1, -4, 5.5, -1, 4, 7.5]));
console.log(order(["z", "c", "f", "b", "c"]));
console.log(order(["d", "f", "g", "a", "d", "a", "d", "y"]));
console.log(order(["order", "my", "words"]));
console.log(order(["a", "rose", "is", "a", "rose", "is", "a", "rose"]));
console.log(order(["z", "zz", "zzz"]));