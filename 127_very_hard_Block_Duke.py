"""
Block Dude
In Block Dude, the main character can climb boxes, but only if they are stacked in a particular way so that he is able to climb them one at a time. More specifically, he can only climb UP or DOWN one box at a time.

Let 1s represent the boxes, and 0 represent the background. Write a function that returns True if block dude can travel from the left side to the right side of the screen given his constraints.

For example, the sample layout below should return True.

[
  [0, 0, 0, 0, X, 0, 0, 0, 0],
  [0, 0, 0, X, 1, X, X, 0, 0],
  [0, X, X, 1, 1, 1, 1, X, 0],
  [X, 1, 1, 1, 1, 1, 1, 1, X]
]
Since block dude can travel across these boxes (Note: X's are just to show walking path and are not part of the actual input). On the other hand:

[
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 0, 0],
  [0, X, X, 1, 1, 1, 1, 0, 0],
  [X, 1, 1, 1, 1, 1, 1, 1, 0]
]
Should return False, since block dude is stuck at column 3, being unable to climb 2 boxes at once.

Examples
can_traverse([
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 0, 0, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 1, 0]
]) ➞ False

# Block dude can't jump down 2 blocks.

can_traverse([
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 1],
  [0, 0, 1, 1, 1, 0, 1, 1, 1],
  [0, 1, 1, 1, 1, 1, 1, 1, 1]
]) ➞ True

# Note: Sometimes the exit is at the top!

can_traverse([
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 1, 0]
]) ➞ True

can_traverse([
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 0, 0],
  [0, 1, 1, 1, 1, 1, 1, 1, 0]
]) ➞ False

# Block dude can't climb 2 blocks.
"""
def can_climb(current, next_):
    diff = abs(current - next_)
    return current == next_ or diff == 1

def can_traverse(x):

    transposed = list(zip(*x))
    step = 0
    current_block = transposed[step].count(1)

    for col in transposed[1:]:
        count_next_col = col.count(1)
        if not can_climb(current_block, count_next_col):
            return False
        else:
            step += 1
            current_block = count_next_col
    return step == len(x[0]) - 1




# import collections
# import numpy as np
#
# def can_traverse(x):
#
#     l_2d_x = np.array(x).T.tolist()
#
#     step = 0
#     current_block = collections.Counter(l_2d_x[step])
#     for i in l_2d_x[1:]:
#         count_l_2d_x = collections.Counter(i)
#         current_zero = [i for i in current_block.values()][0]
#         diff_zero = abs(current_zero - count_l_2d_x[0])
#
#         if current_block == count_l_2d_x:
#             step += 1
#             current_block = count_l_2d_x
#         elif diff_zero == 1:
#             step += 1
#             current_block = count_l_2d_x
#         else:
#             return False
#
#     return True if step == 8 else False




print(can_traverse([
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 1, 1, 1, 0, 1, 0, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 0]
]))

print(can_traverse([
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 1, 1, 0, 0, 1, 0, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 0]
]))

print(can_traverse([
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 1, 1, 1, 0, 1, 0, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 0]
]))

print(can_traverse([
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 0, 1, 1, 1, 1, 1, 0, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 0]
]))


print(can_traverse([
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0, 0, 0],
	[0, 1, 1, 1, 1, 1, 1, 0, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 0]
]))

print(can_traverse([
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 1, 0, 0, 0, 0],
	[0, 0, 1, 1, 1, 1, 1, 0, 0],
	[0, 1, 1, 1, 1, 1, 1, 1, 0]
]))

print(can_traverse([
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 1, 0, 0, 0, 1, 0, 0],
	[0, 1, 1, 1, 0, 1, 1, 1, 0]
]))

print(can_traverse([
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 1, 1, 1, 0, 1, 1, 1, 0]
]))

print(can_traverse([
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0, 0, 1],
	[0, 0, 1, 1, 1, 0, 1, 1, 1],
	[0, 1, 1, 1, 1, 1, 1, 1, 1]
]))

print(can_traverse([
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0, 0, 1],
	[0, 0, 1, 1, 1, 0, 1, 0, 1],
	[0, 1, 1, 1, 1, 1, 1, 1, 1]
]))