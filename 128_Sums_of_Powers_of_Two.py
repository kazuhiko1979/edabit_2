"""
Sums of Powers of Two
Every number can be expressed as the sum between unique powers of two. For example, the number 21 can be expressed as 1 + 4 + 16, which can also be written as 2^0 + 2^2 + 2^4.

Create a function that returns a sorted list of powers of two, which add together to make n.

Examples
sums_of_powers_of_two(21) ➞ [1, 4, 16]

sums_of_powers_of_two(8) ➞ [8]

sums_of_powers_of_two(63) ➞ [1, 2, 4, 8, 16, 32]
Notes
Tests will only include positive whole numbers.
"""

def sums_of_powers_of_two(n):

    result = []
    power = 0

    while n > 0:
        # 奇数か偶数か判定（ビット）
        if n & 1:
            result.append(2 ** power)
        power += 1
        # ビット右にシフト（数値を2で割ると同等）
        n >>= 1
    return result




    # count = 0
    # temp = 0
    # result = []
    # while n >= temp:
    #     result.append(pow(2, count))
    #     temp = pow(2, count)
    #     count += 1
    # result = sorted(result[:-1], reverse=True)
    #
    # final = []
    # for i in result:
    #     if (n - i) >= 0:
    #         final.append(i)
    #         n = n - i
    #     else:
    #         continue
    # return sorted(final)



    
print(sums_of_powers_of_two(1))
print(sums_of_powers_of_two(5))
print(sums_of_powers_of_two(7))
print(sums_of_powers_of_two(8))
print(sums_of_powers_of_two(10))

print(sums_of_powers_of_two(556846320))
# [16, 32, 64, 128, 1024, 2048, 16384, 32768, 1048576, 2097152, 16777216, 536870912])

