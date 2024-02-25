function compress(chars){
    if (chars.length === 0){
        return "";
    }

    let compressed = "";
    let current_char = chars[0];
    let count = 1;

    for (let i = 1; i < chars.length; i++){
        if (chars[i] === current_char){
            count++;
        } else {
            compressed += current_char;
            if (count > 1) {
                compressed += count.toString();
            }
            current_char = chars[i]
            count = 1;
        }
    }

    compressed += current_char;
    if (count > 1){
        compressed += count.toString();
    }

    return compressed;
}

// テストケース
console.log(compress(["a", "a", "b", "b", "c", "c", "c"])); // ➞ "a2b2c3"
console.log(compress(["a"])); // ➞ "a"
console.log(compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])); // ➞ "ab12"
console.log(compress(["a", "a", "a", "b", "b", "a", "a"])); // ➞ "a3b2a2"