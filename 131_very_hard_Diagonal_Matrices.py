"""
Diagonal Matrices
Write a function that diagonally orders numbers in a n x n matrix, depending on which of the four corners you originate from: upper-left (ul), upper-right (ur), lower-left (ll), lower-right (lr).

Examples
diagonalize(3, "ul") ➞ [
  [0, 1, 2],
  [1, 2, 3],
  [2, 3, 4]
]

diagonalize(4, "ur") ➞ [
  [3, 2, 1, 0],
  [4, 3, 2, 1],
  [5, 4, 3, 2],
  [6, 5, 4, 3]
]

diagonalize(3, "ll") ➞ [
  [2, 3, 4],
  [1, 2, 3],
  [0, 1, 2]
]

diagonalize(5, "lr") ➞ [
  [8, 7, 6, 5, 4],
  [7, 6, 5, 4, 3],
  [6, 5, 4, 3, 2],
  [5, 4, 3, 2, 1],
  [4, 3, 2, 1, 0]
]
"""


def diagonalize(n, d):

    result = [list(range(i, i + n)) for i in range(n)]

    if d == "ul":
        return result
    elif d == "lr":
        return [i[::-1] for i in reversed(result)]
    elif d == "ur":
        return [i[::-1] for i in reversed(result[::-1])]
    elif d == "ll":
        return [i for i in reversed(result)]


print(diagonalize(3, "ul"))
print(diagonalize(4, "ur"))
print(diagonalize(3, "ll"))
print(diagonalize(5, "lr"))


