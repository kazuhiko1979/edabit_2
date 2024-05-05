"""
Chocolates Parcel
Mubashir needs to assemble a parcel of ordered chocolates. He got two types of chocolates:

Small chocolates (2 grams each)
Big chocolates (5 grams each)
Create a function that takes three parameters: Number of small available chocolates n_small, number of big chocolates available n_big and desired weight (in grams) of the final parcel order.

The function should return the required number of small chocolates to achieve the goal. The function should return -1 if the goal cannot be achieved by any possible combinations of small and big chocolates.

Examples
chocolates_parcel(4, 1, 13) ➞ 4
# 4 small chocolates = 8 grams
# 1 big chocolate = 5 grams
# 8 + 5 = 13 grams
# Required number of small chocolates = 4

chocolates_parcel(4, 1, 14) ➞ -1
# You can not make any combination to reach 14 grams.

chocolates_parcel(2, 1, 7) ➞ 1
# 1 big chocolate = 5 grams
# 1 small chocolates = 2 grams
# 5 + 2 = 7 grams
# Required number of small chocolates = 1
Notes
Maximize the use of big chocolates that are available to achieve the desired goal. And only then should you proceed to use the small chocolates.
You can't break chocolates into small pieces.
"""

def chocolates_parcel(n_small, n_big, order):
    # Each big chocolate weighs 5 grams
    max_big_used = min(n_big, order // 5)

    # Remaining weight to be made up with small chocolates
    remaining_weight = order - (max_big_used * 5)

    if remaining_weight > n_small * 2:
        return -1  # Not enough small chocolates to cover the remaining weight

    if remaining_weight % 2 == 0:
        return remaining_weight // 2
    else:
        # If there's a remainder when the remaining weight is divided by 2, we cannot use only small chocolates to achieve the exact weight
        # In this case, consider reducing the use of big chocolates and reassess
        for reduced_big in range(max_big_used - 1, -1, -1):
            new_remaining = order - (reduced_big * 5)
            if new_remaining <= n_small * 2 and new_remaining % 2 == 0:
                return new_remaining // 2  # Possible configuration found

        # If no valid configuration is found
        return -1


print(chocolates_parcel(0, 1, 5))
print(chocolates_parcel(3, 1, 6))
print(chocolates_parcel(3, 0, 7))
print(chocolates_parcel(2, 1, 9))
print(chocolates_parcel(58, 156, 283))
print(chocolates_parcel(3, 1000, 5012))
print(chocolates_parcel(1, 1, 1))
print(chocolates_parcel(1, 1, 8))
print(chocolates_parcel(4, 1, 12))
print(chocolates_parcel(10, 400, 2004))


# print(chocolates_parcel(0, 1, 5), 0)
# print(chocolates_parcel(3, 1, 6), 3)
# print(chocolates_parcel(3, 0, 7), -1)
# print(chocolates_parcel(2, 1, 9), 2)
# print(chocolates_parcel(58, 156, 283), 4)
# print(chocolates_parcel(3, 1000, 5012), -1)
# print(chocolates_parcel(1, 1, 1), -1)
# print(chocolates_parcel(1, 1, 8), -1)
# print(chocolates_parcel(4, 1, 12), -1)
# print(chocolates_parcel(10, 400, 2004), 2)