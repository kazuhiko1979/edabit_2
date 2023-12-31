"""
Interquartile Range (IQR)
The median of a data sample is the value that separates the higher half and the lower half of the data. For example, the median of [1, 2, 3] is 2, and the median of [1, 2, 3, 4] is 2.5 (because (2 + 3) / 2 = 2.5). Another way of saying "median" is to say "Q2" (it's the second quartile). Q1 and Q3 are the medians of the values above or below the Q2. The IQR is equal to Q3 - Q1. Here's an example:

Let's say your data sample is: 1, 2, 3, 4

The median (Q2) is: (2+3)/2 =2.5
The lower half is: 1, 2
The upper half is: 3, 4
Q1 (median of the first half): (1+2)/2 = 1.5
Q3 (median of the second half): (3+4)/2 = 3.5
IQR = Q3 - Q1 = 3.5 - 1.5 = 2
If the length of the data sample is odd, as in: 1, 2, 3, 4, 5

The median (Q2) is: 3 (the number is in the middle, so no need to average).
3 is the number that separates the upper and lower data, so we exclude it.
The lower half is: 1, 2
The upper half is: 4, 5
Q1 (median of the first half): (1+2)/2 = 1.5
Q3 (median of the second half): (4+5)/2 = 4.5
IQR = Q3 - Q1 = 4.5 - 1.5 = 3
For a more detailed explanation, please check the Resources tab.

Make a function that takes a list of floats and/or integers and returns the IQR for that list. The return type can be float or int. It doesn't matter.

Examples
iqr([1, 2, 3, 4]) ➞ 2.0

iqr([5, 4, 3, 2, 1]) ➞ 3.0

iqr([-3.1, -3.8, -14, 23, 0]) ➞ 20.4
"""

def iqr(lst):
    sorted_lst = sorted(lst)
    length = len(lst)

    if length % 2 == 0:
        q1 = median(sorted_lst[:length // 2])
        q3 = median(sorted_lst[length // 2:])
    else:
        q1 = median(sorted_lst[:length // 2])
        q3 = median(sorted_lst[length // 2 + 1:])

    return q3 - q1

def median(lst):
    length = len(lst)
    if length % 2 == 0:
        # print((lst[length // 2 - 1] + lst[length // 2]) / 2)
        return (lst[length // 2 - 1] + lst[length // 2]) / 2
    else:
        # print(lst[length // 2])
        return lst[length // 2]

# def iqr(lst):
#
#     flag = False
#
#     if len(lst) % 2 == 0:
#         flag = True
#         return helper_iqr(lst, flag)
#     else:
#         return helper_iqr(lst, flag)
#
# def helper_iqr(lst, flag):
#
#     half_length = int((len(lst) / 2))
#     lower_half = sum(sorted(lst)[:half_length]) / half_length
#     upper_half = sum(sorted(lst)[-half_length:]) / half_length
#     if flag:
#         return upper_half - lower_half
#     else:
#         return round(upper_half) - round(lower_half)


# print(iqr([1, 1, 3, 4, 4, 5, 5, 5, 6, 7, 9])) # 3
print(iqr([6, 4, 4, 4, 3, 3, 2, 1])) # 1.5
# print(iqr([6, 5, 2.6, 8, 4.9, 5, 7.9])) # 3.0
# print(iqr([14, 28, 0, 15, 12, 15, 15, 15])) #, 2.0)
# print(iqr([-3.1, -3.8, -14, 23, 0])) #, 20.4)
# print(iqr([-12, 0, 0, 0, 3])) # , 7.5)
# print(iqr([-3, 0, 0, 0, 0, 4.7])) #, 0.0)
# print(iqr([0, 0, 0, 0, 0, 0])) # , 0.0)
# print(iqr([0, 0, 0, 0, 0, 0, 0])) # , 0.0)


