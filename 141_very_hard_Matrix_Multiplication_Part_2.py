"""
Matrix Multiplication (Part 2)
Create a function that multiplies two matrices (n x m) and (p x q) and returns:

"invalid" if the matrices are not multiplicable (i.e. if m is not equal to p).
The multiplication matrix (n x q) otherwise.
Examples
matrix_multiply([[1, 2]], [[3], [4]]) ➞ [[11]]

matrix_multiply([[0, 0], [0, 1]], [[1, 2], [3, 4], [5, 6]]) ➞ "invalid"

matrix_multiply([[4, 2], [3, 1]], [[5, 6], [3, 8]]) ➞ [[26, 40], [18, 26]]
"""

def matrix_multiply(a, b):

    if len(a[0]) != len(b):
        return "invalid"

    result = [[0] * len(b[0]) for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]

    return result

print(matrix_multiply([[0, 0], [0, 1]], [[1, 2], [3, 4], [5, 6]]))
print(matrix_multiply([[4, 2], [3, 1]], [[5, 6], [3, 8]]))
print(matrix_multiply([[1, 6], [6, 3]], [[5, 3, 5], [1, 6, 6]]))
