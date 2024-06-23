"""
Dividing into Chunks of Maximum Sum N
Write a function that divides a list into chunks such that the sum of each chunk is <= n. Start from the left side of the list and move to the right.

Examples
divide([1, 2, 3, 4, 1, 0, 2, 2], 5)
➞ [[1, 2], [3], [4, 1, 0], [2, 2]]

divide([1, 0, 1, 1, -1, 0, 0], 1)
➞ [[1, 0], [1], [1, -1, 0, 0]]

divide([2, 1, 0, -1, 0, 0, 2, 1, 3], 3)
➞ [[2, 1, 0, -1, 0, 0], [2, 1], [3]]
Notes
The max of the list will always be smaller than or equal to n.
Use the greedy approach when solving the problem (e.g. fit as many elements you can into a chunk as long as you satisfy the sum constraint).
"""

def divide(lst, n):

    result = []
    temp = []

    for i in lst:
        if sum(temp) + i > n:
            result.append(temp)
            temp = [i]
        else:
            temp.append(i)
    if temp:
        result.append(temp)
    return result

print(divide([1, 2, 3, 4, 1, 0, 2, 2], 5)) #[[1, 2], [3], [4, 1, 0], [2, 2]])
print(divide([1, 2, 3, 4, 1, 0, 2, 2], 4))  #[[1, 2], [3], [4], [1, 0, 2], [2]])
print(divide([1, 3, 2, -1, 2, 1, 1, 3, 1], 3)) # [[1], [3], [2, -1, 2], [1, 1], [3], [1]])
print(divide([1, 2, 2, -1, 2, 0, 1, 0, 1], 2)) # [[1], [2], [2, -1], [2, 0], [1, 0, 1]])
print(divide([1, 2, 2, -1, 2, 0, 1, 0, 1], 3)) # [[1, 2], [2, -1, 2, 0], [1, 0, 1]])
print(divide([1, 2, 2, -1, 2, 0, 1, 0, 1], 5)) # [[1, 2, 2, -1], [2, 0, 1, 0, 1]])
print(divide([2, 1, 0, -1, 0, 0, 2, 1, 3], 3)) # [[2, 1, 0, -1, 0, 0], [2, 1], [3]])
print(divide([2, 1, 0, -1, 0, 0, 2, 1, 3], 4)) # [[2, 1, 0, -1, 0, 0, 2], [1, 3]])
print(divide([1, 0, 1, 1, -1, 0, 0], 1)) # [[1, 0], [1], [1, -1, 0, 0]])
print(divide([1, 0, 1, 1, -1, 0, 0], 2)) # [[1, 0, 1], [1, -1, 0, 0]])
print(divide([1, 0, 1, 1, -1, 0, 0], 3)) # [[1, 0, 1, 1, -1, 0, 0]])