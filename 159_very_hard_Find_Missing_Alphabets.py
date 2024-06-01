"""
Find Missing Alphabets
Create a function that takes a string txt containing only letters from a to z in lowercase and returns the missing letter(s) in alphabetical order a-z.

A set of letters is given by abcdefghijklmnopqrstuvwxyz.
Two sets of alphabets means two or more alphabets.
Examples
missing_alphabets("abcdefghijklmnopqrstuvwxy") ➞ "z"
# "z" is missing.

missing_alphabets("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy") ➞ "zz"
# Given string has a set of two alphabets so output will be "zz"

missing_alphabets("edabit") ➞ "cfghjklmnopqrsuvwxyz"
Notes
If the string contains all letters from a-z, return an empty string "".
"""
from string import ascii_lowercase
def missing_alphabets(s):
    repeat = max(s.count(i) for i in set(s))
    res = ''
    for i in ascii_lowercase:
        res += i * (repeat - s.count(i))
    return res

# import string
# import collections
#
# def missing_alphabets(txt):
#
#     count_alpha_set = collections.Counter(string.ascii_lowercase)
#     count_txt = collections.Counter(txt)
#     max_count = max(count_txt.values())
#
#     temp = ''
#     for value, count in count_alpha_set.items():
#         if value not in count_txt:
#             temp += value * max_count
#         elif value in count_txt:
#             if count_txt[value] < max_count:
#                 temp += value * (max_count - count)
#     return ''.join(sorted(temp))


print(missing_alphabets("abcdefghijklmnopqrstuvwxy"))
print(missing_alphabets("abcdefghijklmnopqrstuvwxyz"))
print(missing_alphabets("aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyy"))
print(missing_alphabets("abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxy"))
print(missing_alphabets("edabit"))
print(missing_alphabets("aaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyzzzz"))
print(missing_alphabets("mubashir"))
print(missing_alphabets("aaaa"))