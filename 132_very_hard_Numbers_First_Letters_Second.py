"""
Numbers First, Letters Second
Write a function that sorts list while keeping the list structure. Numbers should be first then letters both in ascending order.

Examples
num_then_char([
  [1, 2, 4, 3, "a", "b"],
  [6, "c", 5], [7, "d"],
  ["f", "e", 8]
]) ➞ [
  [1, 2, 3, 4, 5, 6],
  [7, 8, "a"],
  ["b", "c"], ["d", "e", "f"]
]

num_then_char([
  [1, 2, 4.4, "f", "a", "b"],
  [0], [0.5, "d","X",3,"s"],
  ["f", "e", 8],
  ["p","Y","Z"],
  [12,18]
]) ➞ [
  [0, 0.5, 1, 2, 3, 4.4],
  [8],
  [12, 18, "X", "Y", "Z"],
  ["a", "b", "d"],
  ["e", "f", "f"],
  ["p", "s"]
]
Notes
Test cases will contain integer and float numbers and single letters.
"""
from itertools import chain

def num_then_char(lsts):

    result = []
    upper_alpha = []
    lower_alpha = []
    numbers = []
    length_lst = []

    for lst in lsts:
        length_lst.append(len(lst))
        numbers.append([item for item in lst if isinstance(item, (int, float)) or (isinstance(item, str) and item.isdigit())])
        upper_alpha.append([char for item in lst if isinstance(item, str) for char in item if char.isalpha() and char.isupper()])
        lower_alpha.append([char for item in lst if isinstance(item, str) for char in item if char.isalpha() and char.islower()])

    sorted_lst = sorted(list(chain.from_iterable(numbers))) + sorted(list(chain.from_iterable(upper_alpha))) + sorted(list(chain.from_iterable(lower_alpha)))

    while len(sorted_lst) > 0:
        for n in length_lst:
            add_list = sorted_lst[0:n]
            result.append(add_list)
            sorted_lst = sorted_lst[n:]
    return result



print(num_then_char([
  [1, 2, 4, 3, "a", "b"],
  [6, "c", 5], [7, "d"],
  ["f", "e", 8]
]))

print(num_then_char([
  [1, 2, 4.4, "f", "a", "b"],
  [0], [0.5, "d","X",3,"s"],
  ["f", "e", 8],
  ["p","Y","Z"],
  [12,18]
]))


print(num_then_char([
    [10, 2],
    ["a",3],
    [2.2, "d","h",6,"s",14,1],
    ["f", "e"],
    ["p","y","z","V"],
    [5]
]))

print(num_then_char([
    [10, 2,6,6.5,8.1,"q","w","a","s"],
    ["f",4],
    [2, 3,"h",6,"x",1,0],
    ["g"],
    ["p",7,"j","k","l"],
    [5,"C","A","B"],
    ["L",9]
]))
