"""
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
"""

def coins_combinations(money, coins):

    ways = [0] * (money + 1)
    ways[0] = 1  # 0円を作る方法は1つ

    # 各コインについて
    for coin in coins:
        for amount in range(coin, money + 1):
            ways[amount] += ways[amount - coin]

    return ways[money]

print(coins_combinations(4, [1,2])) #, 3)
print(coins_combinations(10, [5,2,3])) #, 4)
print(coins_combinations(11, [5,7])) #, 0)
print(coins_combinations(300, [5,10,20,50,100,200,500])) #, 1022)
print(coins_combinations(300, [500,5,50,100,20,200,10])) #, 1022)
print(coins_combinations(301, [5,10,20,50,100,200,500])) #, 0)
print(coins_combinations(199, [3,5,9,15])) #, 760)
print(coins_combinations(98, [3,14,8])) #, 19)
print(coins_combinations(419, [2,5,10,20,50])) #, 18515)
