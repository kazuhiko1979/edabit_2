function median(lst) {
    const length = lst.length;
    if (length % 2 === 0) {
        return (lst[length / 2 - 1] + lst[length / 2]) / 2;
    } else {
        return lst[Math.floor(length / 2)];
    }
}

function iqr(lst) {
    const sortedList = lst.slice().sort((a, b) => a - b);
    const length = sortedList.length;

    let q1, q3;
    if (length % 2 === 0) {
        q1 = median(sortedList.slice(0, length / 2));
        q3 = median(sortedList.slice(length / 2));
    } else {
        q1 = median(sortedList.slice(0, Math.floor(length / 2)));
        q3 = median(sortedList.slice(Math.floor(length / 2) + 1));
    }

    return q3 - q1;
}

console.log(iqr([1, 1, 3, 4, 4, 5, 5, 5, 6, 7, 9])); // 3
console.log(iqr([6, 4, 4, 4, 3, 3, 2, 1])); // 1.5
console.log(iqr([6, 5, 2.6, 8, 4.9, 5, 7.9])); // 3.0
console.log(iqr([14, 28, 0, 15, 12, 15, 15, 15])); // 2.0
console.log(iqr([-3.1, -3.8, -14, 23, 0])); // 20.4
console.log(iqr([-12, 0, 0, 0, 3])); // 7.5
console.log(iqr([-3, 0, 0, 0, 0, 4.7])); // 0.0
console.log(iqr([0, 0, 0, 0, 0, 0])); // 0.0
console.log(iqr([0, 0, 0, 0, 0, 0, 0])); // 0.0
