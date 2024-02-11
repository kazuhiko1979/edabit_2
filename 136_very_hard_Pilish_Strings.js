function pilish_string(txt){
    const piDigits = "314159265358979";
    let words = [];
    let piIndex = 0;

    while (txt && piIndex < piDigits.length){
        const wordLength = parseInt(piDigits[piIndex]);
        if (txt.length >= wordLength){
            words.push(txt.slice(0, wordLength));
            txt = txt.slice(wordLength);

        } else {
            words.push(txt + txt.slice(-1).repeat(wordLength - txt.length));
            txt = "";
        }
        piIndex++;
    }

    return words.join(' ');
}


// Test cases
console.log(pilish_string("FORALOOP"));
console.log(pilish_string("CANIMAKEAGUESS"));
console.log(pilish_string("CANIMAKEAGUESSNOW"));
console.log(pilish_string("X"));
console.log(pilish_string("ARANDOMSEQUENCEOFLETTERS"));
console.log(pilish_string(""));
console.log(pilish_string("33314444155555999999999226666665555533355555888888889999999997777777999999999"));
console.log(pilish_string("###*@"));
console.log(pilish_string(".........."));
console.log(pilish_string("NowIfallAtiredsuburbianInliquidunderthetreesDriftingalongsideforestssimm"));
console.log(pilish_string("HOWINEEDADRINKALCOHOLICINNATUREAFTERTHEHEAVYLECTURESINVOLVINGQUANTUMMECHANICSANDALLTHESECRETSOFTHEUNIVERSE"));
console.log(pilish_string("HOWINEEDADRINKALCOHOLICINNATUREAFTERTHEHEAVYCODING"));
