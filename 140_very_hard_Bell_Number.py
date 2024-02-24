"""
Bell Number
The Bell number is the number of ways a list of n items can be partitioned into non-empty sublists. See the resources section for an in-depth explanation.

Create a function that takes a number n and returns the corresponding Bell number.

Examples
bell(1) ➞ 1
# sample_lst = [1]
# possible_partitions = [[[1]]]

bell(2) ➞ 2
# sample_lst = [1, 2]
# possible_partitions = [[[1, 2]], [[1], [2]]]

bell(3) ➞ 5
# sample_lst = [1, 2, 3]
# possible_partitions = [[[1, 2, 3]], [[1, 2], [3]], [[1], [2, 3]], [[1, 3], [2]], [[1], [2], [3]]]
"""
def bell(n):
    bell_numbers = [[0] * (n+1) for _ in range(n+1)]
    bell_numbers[0][0] = 1

    for i in range(1, n+1):
        bell_numbers[i][0] = bell_numbers[i-1][i-1]
        for j in range(1, i+1):
            bell_numbers[i][j] = bell_numbers[i-1][j-1] + bell_numbers[i][j-1]

    print(bell_numbers)
    return bell_numbers[n][0]

# テスト
print(bell(1))   # ➞ 1
print(bell(2))   # ➞ 2
print(bell(3))   # ➞ 5
print(bell(4))   # ➞ 15
print(bell(5))   # ➞ 52
print(bell(6))   # ➞ 203
print(bell(7))   # ➞ 877









