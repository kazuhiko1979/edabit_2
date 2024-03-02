function customSort(t, s){

    //文字列tに基づいて優先順位をマッピングするオブジェクト
    const priority = {}
    t.split('').forEach((char, index) => {
        priority[char] = index;
    });

    // 文字列sをフィルタリングしてorderとoriginを作成
    const order = s.split('').filter(char => t.includes(char));
    const origin = s.split('').filter(char => !t.includes(char));

    // orderをカスタムソート
    const sortedOrder = order.sort((a, b) => {
        return (priority[a] != undefined ? priority[a] : -1) - (priority[b] !== undefined ? priority[b] : -1);
    });

    // originを通常の方法でソート
    const sortedOrigin = origin.sort();

    // 結果を結合
    return sortedOrder.join('') + sortedOrigin.join('');

}

console.log(customSort("edc", "abcdefzyx"));
console.log(customSort("fby", "abcdefzyx"));
console.log(customSort("", "abcdefzyx"));
console.log(customSort('cteqh', 'xnjanztmhg'));
console.log(customSort('jv', 'cxkafinfiuhnnaracsztbrcwaifwattzavwohoqskauififucq'));