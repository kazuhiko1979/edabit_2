/**
Coins Combinations
Given an amount of money and a list of coins denominations, create a function that counts how many different ways you can make change with the given money.

Examples
coins_combinations(4, [1, 2]) ➞ 3
# 1+1+1+1 = 4
# 1+1+2 = 4
# 2+2 = 4

coins_combinations(10, [5, 2, 3]) ➞ 4

coins_combinations(11, [5, 7]) ➞ 0
Notes
Order of coins does not matter (i.e. 1+1+2 == 2+1+1).
You have an infinite amount of coins.
**/

public class very_hard_Coins_Combinations_168 {
    public static int coinsCombinations(int money, int[] coins){
        int[] ways = new int[money + 1];
        ways[0] = 1; // 0円を作る方法は1つ

        // 各コインについて
        for (int coin : coins) {
            for (int amount = coin; amount <= money; amount++) {
                ways[amount] += ways[amount - coin];
            }
        }

        return ways[money];
    }
    public static void main(String[] args) {
        System.out.println(coinsCombinations(4, new int[]{1, 2})); // 3
        System.out.println(coinsCombinations(10, new int[]{5, 2, 3})); // 4
        System.out.println(coinsCombinations(11, new int[]{5, 7})); // 0
        System.out.println(coinsCombinations(300, new int[]{5, 10, 20, 50, 100, 200, 500})); // 1022
        System.out.println(coinsCombinations(300, new int[]{500, 5, 50, 100, 20, 200, 10})); // 1022
        System.out.println(coinsCombinations(301, new int[]{5, 10, 20, 50, 100, 200, 500})); // 0
        System.out.println(coinsCombinations(199, new int[]{3, 5, 9, 15})); // 760
        System.out.println(coinsCombinations(98, new int[]{3, 14, 8})); // 19
        System.out.println(coinsCombinations(419, new int[]{2, 5, 10, 20, 50})); // 18515
    }
}
