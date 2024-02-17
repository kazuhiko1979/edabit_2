"""
Diamond Sum
Given an nxn grid of consecutive numbers, return the grid's Diamond Sum. The diamond sum is defined as the sum of the numbers making up the diagonals between adjacent sides.

Examples
diamond_sum(1) ➞ 1

[1]
diamond_sum(3) ➞ 20

[
  [1, _, 3],
  [_, 5, _],
  [7, _, 9]
]

# The numbers behind the underscores make up the Diamond Sum.
# 2 + 4 + 6 + 8 = 20
diamond_sum(5) ➞ 104

[
  [1, 2, _, 4, 5],
  [6, _, 8, _, 10],
  [_, 12, 13, 14, _],
  [16, _, 18, _, 20],
  [21, 22, _, 24, 25]
]

# 3 + 7 + 9 + 11 + 15 + 17 + 19 + 23 = 104
Notes
n is always an odd number.
Bonus points for solving it mathematically!
"""

# def diamond_sum(n):
#
#     total = 0
#     n_list = [list(range(i, i + n)) for i in range(1, n * n + 1, n)]
#
#     n_pivot = n // 2
#     total += n_list[0][n_pivot]
#     total += n_list[len(n_list)-1][n_pivot]
#
#     left_side = n // 2
#     right_side = n // 2
#
#     for row in range(1, n-1):
#         for column in range(1, n-1):
#             if column == n_pivot and row <= n_pivot:
#                 left_side -= 1
#                 right_side += 1
#                 total += n_list[row][left_side]
#                 total += n_list[row][right_side]
#             if column == n_pivot and row > n_pivot:
#                 left_side += 1
#                 right_side -= 1
#                 total += n_list[row][left_side]
#                 total += n_list[row][right_side]
#
#     return total


def diamond_sum(n):

    total = 0
    n_list = [[i + j * n for i in range(1, n + 1)] for j in range(n)]

    # 中央の値を加算
    total += n_list[0][n // 2]
    total += n_list[n - 1][n // 2]

    left_side = n // 2
    right_side = n // 2

    # 左右の対角線の値を加算
    for row in range(1, n - 1):
        if row <= n // 2:
            left_side -= 1
            right_side += 1
        else:
            left_side += 1
            right_side -= 1

        total += n_list[row][left_side]
        total += n_list[row][right_side]

    return total if n > 1 else 1

print(diamond_sum(1))
print(diamond_sum(3))
print(diamond_sum(5))
print(diamond_sum(7))
print(diamond_sum(9))