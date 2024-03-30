function combinator(lst, separator='') {
    let temp = lst.map(i => !Array.isArray(i) ? [i] : i.filter(j => j !== ' '));
    let combinations = cartesian(temp);
    let result = combinations.map(pair => Array.isArray(pair) ? (pair.every(item => item.length <= 2) ? pair.join('') : pair.join(separator)) : pair);
    return result;
}

function cartesian(arr) {
    return arr.reduce((a, b) => a.flatMap(x => b.map(y => Array.isArray(x) ? x.concat(y) : [x, y])));
}

console.log(combinator([['a']]));
console.log(combinator([['ab'], ['ba']]));
console.log(combinator([['a', 'b']]));
console.log(combinator([["a", "b"], ["c", "d"]]));
console.log(combinator([["a"], ["a", "b"], "abc"]));
console.log(combinator([["foo", "bar"], ["baz", "bamboo"]], ' '));
console.log(combinator(['abcd', 'efgh', 'ijkl']));
console.log(combinator([[]]));
console.log(combinator([['a', 'b'], [], ['e', 'f']]));
console.log(combinator([[], ['e', 'f']]));
