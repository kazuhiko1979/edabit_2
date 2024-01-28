function num_then_char(lst){
    let nums = [];
    let letters = [];

    // 数字と文字を分類
    for (let L of lst) {
        for (let a of L){
            if (typeof a === "string"){
                letters.push(a);
            } else{
                nums.push(a)
            }
        }
    }

    // ソート
    nums.sort((a, b) => a - b);
    letters.sort();

    let L = nums.concat(letters);

    // リストを更新
    for (let i = 0; i < lst.length; i++){
        for (let j = 0; j < lst[i].length; j++){
            lst[i][j] = L.shift();
        }
    }

    return lst;
}


// テストケース
console.log(num_then_char([
    [1, 2, 4, 3, "a", "b"],
    [6, "c", 5], [7, "d"],
    ["f", "e", 8]
  ]));
  
  console.log(num_then_char([
    [1, 2, 4.4, "f", "a", "b"],
    [0], [0.5, "d","X",3,"s"],
    ["f", "e", 8],
    ["p","Y","Z"],
    [12,18]
  ]));
  
  console.log(num_then_char([
      [10, 2],
      ["a",3],
      [2.2, "d","h",6,"s",14,1],
      ["f", "e"],
      ["p","y","z","V"],
      [5]
  ]));
  
  console.log(num_then_char([
      [10, 2,6,6.5,8.1,"q","w","a","s"],
      ["f",4],
      [2, 3,"h",6,"x",1,0],
      ["g"],
      ["p",7,"j","k","l"],
      [5,"C","A","B"],
      ["L",9]
  ]));