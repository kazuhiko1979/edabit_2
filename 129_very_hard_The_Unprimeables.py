"""
The Unprimeables
In this challenge, you have to establish if an integer is an Unprimeable number. To be Unprimeable, when a single digit of a composite number is exchanged with any digit from 0 up to 9, the new number obtained must not be a prime:

number = 14

Numbers obtained changing the first digit (1):

04 (4), 14, 24, 34, 44, 54, 64, 74, 84, 94
# Leading zeros are not considered

Numbers obtained changing the second digit (4):

10, 11, 12, 13, 14, 15, 16, 17, 18, 19

# Among the two series, 11, 13, 17 and 19 are primes
# 14 is not an unprimeable number

number = 200

Numbers obtained changing the first digit (2):

000 (0), 100, 200, 300, 400, 500, 600, 700, 800, 900
# Leading zeros are not considered

Numbers obtained changing the second digit (0):

200, 210, 220, 230, 240, 250, 260, 270, 280, 290

Numbers obtained changing the third digit (0):

200, 201, 202, 203, 204, 205, 206, 207, 208, 209

# Among the three series, there aren't primes
# 200 is an unprimeable number (the first of the series)
Given a non-negative integer num, implement a function that returns:

The string "Prime Input" if num is prime.
The string "Unprimeable" if num is Unprimeable (accordingly to the above instructions).
If num is not Unprimeable, an array containing all the primes obtained after exchanging its digits, without duplicates and sorted ascendingly.
Examples
is_unprimeable(200) ➞ "Unprimeable"

is_unprimeable(14) ➞ [11, 13, 17, 19]

is_unprimeable(2) ➞ "Prime Input"
Notes
When changing the first digit, leading zeros are not considered part of the new number obtained.
Despite is still an unproofed theory, as far as we know every even number (except 2) is not prime. You are free to choose to use this discriminant when you check the number obtained after the change of a digit.
The same concept can be applied also to primes. Primes that do not return other primes when their single digits are changed (apart from the number itself) are called Weakly Primes: the first prime of this series is 294001.
"""

def is_unprimeable(num):

    num_str = (str(num))
    result = set()

    for i in range(len(str(num))):
        for j in range(10):
            if j != int(num_str[i]):
                new_num = int(num_str[:i] + str(j) + num_str[i+1:])
                result.add(new_num)

    prime_list = generate_primes(max(result))

    if num in prime_list:
        return "Prime Input"

    final = sorted([n for n in result if n in prime_list])

    return final if final else "Unprimeable"

def generate_primes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return [i for i in range(n + 1) if primes[i]]

    return prime_list


print(is_unprimeable(200))
print(is_unprimeable(14))
print(is_unprimeable(2))
print(is_unprimeable(839))
print(is_unprimeable(4065))
print(is_unprimeable(5042))
print(is_unprimeable(1))
print(is_unprimeable(5137))
print(is_unprimeable(666))
print(is_unprimeable(13490))
print(is_unprimeable(294001))


