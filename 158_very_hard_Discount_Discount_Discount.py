"""
Discount! Discount! Discount!
We all love a little bargain.

Your function will get a price, and a load of discounts. Your job is to write the function so that it calculates the maximum possible discount.

The price is a Number.
The load of discounts is a string like: 15%, 8, 50%.
So, percentages, with %, and amounts, without %.
You have to think about the order of applying the discounts.
Round the output amount to the nearest hundreth.
Output a Number.
Examples
discount(64, "50%, 50%") ➞ 16
# Reduce 50% twice.

discount(24, "20, 2") ➞ 2
# Subtract 20 and 2.

discount(20, "10, 10%") ➞ 8
# Apply 10% discount first and then subtract 10.
"""
def discount(n, txt):
    if not txt:
        return n
    discounts = sorted(txt.split(', '), key=lambda x: not x.endswith('%'))
    for i in discounts:
        if i.endswith('%'):
            n *= (100 - float(i[:-1])) / 100
        else:
            n -= float(i)
    return round(n, 2)



# def discount(n, txt):
#
#     # リストを分割し、空白とカンマを削除
#     items = [item.strip() for item in txt.split(",")]
#
#     # パーセントと数字を分ける
#     percent_items = [item for item in items if '%' in item]
#     number_items = [item for item in items if '%' not in item]
#
#     # 各リストを降順にソート
#     percent_items.sort(key=lambda x: float(x[:-1]), reverse=True)
#     number_items.sort(reverse=True)
#
#     # 結果を結合
#     sorted_items = percent_items + number_items
#
#     if sorted_items != ['']:
#         for i in sorted_items:
#             if '%' in i:
#                 n -= n * float(i.strip('%')) / 100
#             elif '.' in i:
#                 n -= float(i)
#             else:
#                 n -= int(i)
#         return round(n, 2)
#     return n

print(discount(10, '1, 1%'))
print(discount(60, '',))
print(discount(64, "50%, 50%"))
print(discount(1000, '2%, 100, 50%, 16'))
print(discount(24, "20, 2"))
print(discount(20, "10, 10%"))
print(discount(111, '11, 11%'))
print(discount(237.037, '25%, 25%, 25%'))
print(discount(26.026, '1%, 1%, 1%, 1%'))
print(discount(	1000, '99.9%'))
print(discount(12345, '4%, 21, 33.6%, 87, 3%, 80.12'))