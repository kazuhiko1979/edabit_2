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
def num_then_char(lst):

    num = []
    capital_l = []
    non_capital_l = []
    length_lst = []

    for i in lst:
        length_lst.append(len(i))
        for char in i:
            try:
                if char.isalpha() & char.isupper():
                    capital_l.append(char)
                else:
                    non_capital_l.append(char)
            except:
                num.append(char)

    result = []
    sorted_lst = sorted(num) + sorted(capital_l) + sorted(non_capital_l)

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
