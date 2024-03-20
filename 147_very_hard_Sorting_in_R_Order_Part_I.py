"""
Sorting in R: Order (Part I)
R, a programming language used for Statistics and Data Analysis, has the function order, which returns a list with the indices needed to sort the original vector(∗).

For example:

my_list = [1, 3, 3, 9, 8]
# Ordered would be: [0, 1, 2, 4, 3]
In plain words, order tells you what elements to look at in your original vector to sort it. The list my_list[0] + my_list[1] + my_list[2] + my_list[4] + my_list[3] is equivalent to sorted(my_list).

If two or more elements have the same order, their original order is preserved. Here, [0, 1, 2, 4, 3] and [0, 2, 1, 4, 3] would both sort the vector, but only the first one preserves the original order for the two 3s.

Implement the function order() so that it works the same way it does in R.

Examples
order([9, 1, 4, 5, 4]) ➞ [1, 2, 4, 3, 0]

order(["z", "c", "f", "b", "c"]) ➞ [3, 1, 4, 2, 0]

order(["order", "my", "words"]) ➞ [1, 0, 2]
Notes
Expect numbers and lower-case alphabetic characters only.
Find Part II: Rank here.
Vectors in R are similar to a list. Although vectors in R are 1-indexed, your function should be 0-indexed. Other differences between vectors and lists will be ignored for the scope of this challenge.
If you implement your own algorithm, it must be stable, meaning that the order of identical elements doesn't get switched around.
"""
def order(lst):

    key_sorted = sorted([[val, i] for i, val in enumerate(lst)])
    return [x[1] for x in key_sorted]



# def order(lst):
#     result = []
#     lst = {key: value for key, value in enumerate(lst)}
#     while lst:
#         min_key = min(lst, key=lst.get)
#         result.append(min_key)
#         del lst[min_key]
#     return result

import collections
# def order(lst):
#
#     result = []
#     lst = {key: value for key, value in enumerate(lst)}
#
#     while len(lst) > 0:
#
#         min_value = min(lst.values())  # find min value
#
#         # find a min key
#         min_keys = [key for key, value in lst.items() if value == min_value]
#         min_key = min(min_keys)
#
#         lst.pop(min_key)
#         result.append(min_key)
#
#     return result
    
    
print(order([1, 3, 3, 9, 8]))
print(order([9, 1, 4, 5, 4]))
print(order([1, 1, 1, 1, 1]))
print(order([1, 2, 0, 3, 7, 1, 11, 1, 2]))
print(order([1, -4, 5.5, -1, 4, 7.5]))
print(order(["z", "c", "f", "b", "c"]))
print(order(["d", "f", "g", "a", "d", "a", "d", "y"]))
print(order(["order", "my", "words"]))
print(order(["a", "rose", "is", "a", "rose", "is", "a", "rose"]))
print(order(["z", "zz", "zzz"]))


# Test.assert_equals(order([1, 3, 3, 9, 8]), [0, 1, 2, 4, 3])
# Test.assert_equals(order([9, 1, 4, 5, 4]), [1, 2, 4, 3, 0])
# Test.assert_equals(order([1, 1, 1, 1, 1]), [0, 1, 2, 3, 4])
# Test.assert_equals(order([1, 2, 0, 3, 7, 1, 11, 1, 2]), [2, 0, 5, 7, 1, 8, 3, 4, 6])
# Test.assert_equals(order([1, -4, 5.5, -1, 4, 7.5]), [1, 3, 0, 4, 2, 5])
# Test.assert_equals(order(["z", "c", "f", "b", "c"]), [3, 1, 4, 2, 0])
# Test.assert_equals(order(["d", "f", "g", "a", "d", "a", "d", "y"]), [3, 5, 0, 4, 6, 1, 2, 7])
# Test.assert_equals(order(["order", "my", "words"]), [1, 0, 2])
# Test.assert_equals(order(["a", "rose", "is", "a", "rose", "is", "a", "rose"]), [0, 3, 6, 2, 5, 1, 4, 7])
# Test.assert_equals(order(["z", "zz", "zzz"]), [0, 1, 2])