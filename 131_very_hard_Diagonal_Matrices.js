function diagonalize(n, d) {
    const result = Array.from({length: n}, (_, i) => Array.from({ length: n }, (_, j) => i + j));

    if (d === "ul") {
        return result;
    } else if (d === "lr") {
        return result.map(row => row.slice().reverse()).reverse();
    } else if (d === "ur") {
        return result.map(row => row.slice().reverse()).reverse();
    } else if (d === "ll") {
        return result.slice().reverse();
    }
}



// Examples
console.log(diagonalize(3, "ul"));
console.log(diagonalize(4, "ur"));
console.log(diagonalize(3, "ll"));
console.log(diagonalize(5, "lr"));