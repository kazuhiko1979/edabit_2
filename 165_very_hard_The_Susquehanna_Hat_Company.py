"""
The Susquehanna Hat Company
This fabled hat company has 5 production lines running simultaneously. The speed of each production line varies depending on the style and quality of the hat being produced. You will be given the number of hats required and a list of production line speeds.

Your job is to devise a function that will find the number of minutes elapsed for exactly n hats to be finished. If exactly n hats cannot be made in any time frame, return None. The speeds given are the number of minutes required to make one hat.

Examples
hats([5, [1, 1, 1, 1, 1]]) ➞ "1 minute"
# If each line makes a hat in 1 min, it takes 1 min to make 5 hats.

hats([3, [23, 11, 19, 9, 36]]) ➞ "18 minutes"

hats([650, [23, 11, 19, 9, 36]]) ➞ "2001 minutes"

hats([9, [23, 11, 19, 9, 36]]) ➞ None
"""
def hats(lst):
    n = lst[0]
    speeds = lst[1]
    min_time = min(speeds)

    def calculate_time(time):
        count = sum(time // speed for speed in speeds)
        return count

    low, high = 1, min_time * n

    while low <= high:
        mid = (low + high) // 2
        if calculate_time(mid) >= n:
            high = mid - 1
        else:
            low = mid + 1

    if calculate_time(low) == n:
        if low == 1:
            return "{} minute".format(low)
        else:
            return "{} minutes".format(low)
    else:
        return None

# def hats(lst):
#     n = lst[0]  # hat数
#     start = lst[1]  # 初期リスト
#     temp = [start]  # 結果を格納するリスト
#
#     next = start
#     min_value = min(next)
#
#     min_count = next.count(min_value)
#     count = 0
#     count += min_count
#
#     if n == count:
#         return '{} minutes'.format(min_value)
#
#     origin = 0
#
#     while count <= n:
#         next = [i + j for i, j in zip(next, start)]
#         temp.append(next)
#         origin += min_value
#
#         count = 0
#         for sublist in temp:
#             for num in sublist:
#                 if num <= origin:
#                     count += 1
#         if count == n:
#             return '{} minutes'.format(origin)
#         elif count > n:
#             break
#     return None

print(hats([35, [1, 1, 1, 1, 1]]))
print(hats([11, [4, 18, 11, 29, 10]]))
print(hats([1, [11, 21, 1, 18, 2]]))
print(hats([1, [4, 18, 11, 29, 10]]))
print(hats([2001, [1, 2, 3, 4, 5]]))
print(hats([100, [6, 3, 18, 7, 87]]))
print(hats([200, [30, 45, 27, 78, 29]]))
print(hats([47, [12, 19, 12, 28, 17]]))
print(hats([999999999, [30, 45, 27, 78, 29]]))


