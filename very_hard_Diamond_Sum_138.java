public class very_hard_Diamond_Sum_138 {
    public static int diamondSum(int n){
        int total = 0;
        int[][] nList = new int[n][n];


    for (int j = 0; j < n; j++){
        for (int i = 0; i < n; i++) {
            nList[j][i] = i + 1 + j * n;
        }
    }

    // 中央の値を加算
    total += nList[0][n / 2];
    total += nList[n-1][n / 2];

    int rightSide = n / 2;
    int leftSide = n / 2;

    for (int row = 1; row < n-1; row++){
        if (row <= n / 2){
            leftSide--;
            rightSide++;
        } else {
            leftSide++;
            rightSide--;
        }

        total += nList[row][leftSide];
        total += nList[row][rightSide];
    }

    return total;

}


public static void main(String[] args) {
    System.out.println(diamondSum(1));  // 1
    System.out.println(diamondSum(3));  // 20
    System.out.println(diamondSum(5));  // 104
    System.out.println(diamondSum(7));  // 300
    System.out.println(diamondSum(9));  // 656
}
}