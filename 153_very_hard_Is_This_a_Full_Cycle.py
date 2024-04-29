"""
Is This a Full Cycle?
Say you want to traverse a list of integers starting at the first item and using each value as a pointer of what item to visit next. For example, you would traverse the list [1, 4, 3, 0, 2] in the following manner:

List

Because you visit every item once and go back to the starting point, the list [1, 4, 3, 0, 2] is a "full cycle".

Create a function that returns True if the input list is a full cycle, or False otherwise.

Examples
full_cycle([1, 4, 3, 0, 2]) ➞ True

full_cycle([1, 4, 0, 3, 2]) ➞ False

full_cycle([5, 3, 4, 2, 0, 1]) ➞ True
Notes
Test lists won't include any negative integers.
"""

def full_cycle(lst):
    list_index = [i[0] for i in enumerate(lst)]
    next_index = lst[0]
    while list_index:
        if next_index in list_index:
            list_index.remove(next_index)
            next_index = lst[next_index]
        else:
            return False
    return not list_index





print(full_cycle([1, 2, 0, 3]))
print(full_cycle([1, 4, 0, 0, 2]))
print(full_cycle([3, 0, 4, 2]))
print(full_cycle([3, 2, 0, 1]))
print(full_cycle([3, 2, 0, 1, 3]))
print(full_cycle([4, 1, 2, 3, 0]))
print(full_cycle([2, 0, 4, 1, 3]))