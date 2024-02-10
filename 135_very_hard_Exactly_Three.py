"""
Exactly Three
You are given a number n. Determine whether n has exactly 3 divisors or not.

Examples
is_exactly_three(4) ➞ True
# 4 has only 3 divisors: 1, 2 and 4

is_exactly_three(12) ➞ False
# 12 has 6 divisors: 1, 2, 3, 4, 6, 12

is_exactly_three(25) ➞ True
# 25 has only 3 divisors: 1, 5, 25
"""

def is_exactly_three(n):

    factors = []
    sqrt_n = int(n ** 0.5) + 1

    for i in range(1, sqrt_n):
        if n % i == 0:
            factors.append(i)
            complement = n // i
            if complement != i:
                factors.append(complement)
        if len(factors) > 3:
            return False
    return len(factors) == 3


print(is_exactly_three(4))
print(is_exactly_three(12))
print(is_exactly_three(25))
print(is_exactly_three(27550356289))
print(is_exactly_three(275503325))



