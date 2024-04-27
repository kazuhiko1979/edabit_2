"""
Decrypt the String from Digits to Letters
Given a string s consisting from digits and #, translate s to English lowercase characters as follows:

Characters ("a" to "i") are represented by ("1" to "9").
Characters ("j" to "z") are represented by ("10#" to "26#").
Examples
decrypt("10#11#12") ➞ "jkab"

decrypt("1326#") ➞ "acz"

decrypt("25#") ➞ "y"
"""

# def decrypt(s):
#
#     one_digits = '@abcdefghi'
#     two_digits = 'jklmnopqrstuvwxyz'
#
#     index = len(s)
#     s =  '@' + s
#     temp = ''
#     while index > 0:
#         if s[index] != '#':
#             temp += one_digits[int(s[index])]
#             index -= 1
#         else:
#             num_two = int(s[index - 2] + s[index - 1])
#             temp += two_digits[num_two-10]
#             index -= 3
#     return temp[::-1]



def decrypt(s: str) -> str:
    """
    Decrypts the given string `s` using the provided rules.

    Args:
        s (str): The string to be decrypted.

    Returns:
        str: The decrypted string.
    """
    single_digits = 'abcdefghi'
    double_digits = 'jklmnopqrstuvwxyz'

    result = ''
    i = len(s) - 1

    while i >= 0:
        if s[i] != '#':
            result += single_digits[int(s[i]) - 1]
            i -= 1
        else:
            num = int(s[i - 2:i])
            result += double_digits[num - 10]
            i -= 3

    return result[::-1]


print(decrypt("10#11#12"))
print(decrypt("1326#"))
print(decrypt("25#"))