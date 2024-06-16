"""
Alpha-Range
As you know, the function range() returns a range of numbers, but it doesn't work on alphabets. In this challenge, we try to fill this gap.

Write a function alpha-range() which takes three arguments start, stop, and step (which its default value is one). The function must return a list of alphabetical characters, ranging from start character to stop character based on step value.

The function must follow these conditions:

If step is zero or more than 26 or less than -26, return "step must be a non-zero value between -26 and 26, exclusive".

Both start and stop must share the same case, otherwise, return "both start and stop must share the same case".

Like range() function:

step must not be zero.
Unlike range() function:

returned list must be inclusive.
the order of characters doesn't affect the output (i.e. the output of alpha_range("a", "f") is the same as alpha_range("f", "a"), see examples).
Examples
alpha_range("a", "f") ➞ ["a", "b", "c", "d", "e", "f"]

alpha_range("f", "a") ➞ ["a", "b", "c", "d", "e", "f"]

alpha_range("a", "f", -1) ➞ ["f", "e", "d", "c", "b", "a"]

alpha_range("f", "a", -1) ➞ ["f", "e", "d", "c", "b", "a"]

alpha_range("A", "F", -1) ➞ ["F", "E", "D", "C", "B", "A"]

alpha_range("A", "F", 0) ➞ "step must be a non-zero value between -26 and 26, exclusive"

alpha_range("A", "F", -26) ➞ "step must be a non-zero value between -26 and 26, exclusive"

alpha_range("a", "F", -1) ➞ "both start and stop must share the same case"
Notes
All the start and stop values in the tests are valid alphabetical characters.
"""
# Final
def alpha_range(start, stop, step=1):

    if ord(start)>ord(stop) and step>0 or ord(start)<ord(stop) and step<0:
        start,stop = stop,start

    if start.islower() and stop.isupper() or start.isupper() and stop.islower():
        return 'both start and stop must share the same case'

    if abs(step)>=26 or step==0:
        return 'step must be a non-zero value between -26 and 26, exclusive'

    final = []
    for i in range(ord(start),ord(stop)-(1 if step<0 else -1),step):
        final.append(chr(i))
    return final

# リファクタリング：
# import string
#
# def alpha_range(start, stop, step=1):
#     if step == 0 or abs(step) >= 26:
#         return "step must be a non-zero value between -26 and 26, exclusive"
#
#     if start.islower() and stop.islower():
#         alphabet = string.ascii_lowercase
#     elif start.isupper() and stop.isupper():
#         alphabet = string.ascii_uppercase
#     else:
#         return "both start and stop must share the same case"
#
#     start_index, stop_index = alphabet.index(start), alphabet.index(stop)
#
#     if start_index > stop_index:
#         step = -step
#         result = alphabet[stop_index:start_index+1][::abs(step)][::-1]
#     else:
#         result = alphabet[start_index:stop_index+1][::step]
#
#     if not result:
#         return "step must be a non-zero value between -26 and 26, exclusive"
#
#     return list(result)

# import string
#
# def alpha_range(start, stop, step=1):
#
#     lowercase = string.ascii_lowercase
#     uppercase = string.ascii_uppercase
#
#     if start.isupper() and stop.isupper():
#         start_index, stop_index = uppercase.index(start), uppercase.index(stop)
#         if start_index > stop_index:
#             start_index, stop_index = stop_index, start_index
#             try:
#                 if -26 < step < 0:
#                     result = list(uppercase[start_index:stop_index+1:-step])
#                     return result[::-1]
#                 else:
#                     result = list(uppercase[start_index:stop_index+1:step])
#                     if result != []:
#                         return result
#                     else:
#                         return "step must be a non-zero value between -26 and 26, exclusive"
#             except ValueError:
#                 return "step must be a non-zero value between -26 and 26, exclusive"
#         else:
#             try:
#                 if -26 < step < 0:
#                     result = list(uppercase[start_index:stop_index + 1:-step])
#                     return result[::-1]
#                 else:
#                     result = list(uppercase[start_index:stop_index + 1:step])
#                     if result != []:
#                         return result
#                     else:
#                         return "step must be a non-zero value between -26 and 26, exclusive"
#                 # return result
#             except ValueError:
#                 return "step must be a non-zero value between -26 and 26, exclusive"
#
#     elif start.islower() and stop.islower():
#         start_index, stop_index = lowercase.index(start), lowercase.index(stop)
#         if start_index > stop_index:
#             start_index, stop_index = stop_index, start_index
#             try:
#                 if -26 < step < 0:
#                     result = list(lowercase[start_index:stop_index + 1:-step])
#                     return result[::-1]
#                 else:
#                     result = list(lowercase[start_index:stop_index + 1:step])
#                     if result != []:
#                         return result
#                     else:
#                         return "step must be a non-zero value between -26 and 26, exclusive"
#                 # return result
#             except ValueError:
#                 return "step must be a non-zero value between -26 and 26, exclusive"
#         else:
#             try:
#                 if -26 < step < 0:
#                     result = list(lowercase[start_index:stop_index+1:-step])
#                     return result[::-1]
#                 else:
#                     result = list(lowercase[start_index:stop_index+1:step])
#                     if result != []:
#                         return result
#                     else:
#                         return "step must be a non-zero value between -26 and 26, exclusive"
#                 # return result
#             except ValueError:
#                 return "step must be a non-zero value between -26 and 26, exclusive"
#     return "both start and stop must share the same case"


print(alpha_range('i', 'z'))
print(alpha_range("H", "I"))
print(alpha_range("g", "o"))
print(alpha_range("L", "Y"))
print(alpha_range('m', 'd'))
print(alpha_range('M', 'S'))
print(alpha_range('d', 'a'))
print(alpha_range('S', 'D'))
print(alpha_range('k', 'd'))
print(alpha_range('I', 'X'))
print(alpha_range('b', 'g', -1))
print(alpha_range('D', 'B', -1))
print(alpha_range('n', 'o', -1))
print(alpha_range('S', 'U', -1))
print(alpha_range('a', 'l', -1))
print(alpha_range('D', 'P', -1))
print(alpha_range('m', 'k', -1))
print(alpha_range('Z', 'P', -1))
print(alpha_range('j', 'u', -1))
print(alpha_range('X', 'A', -1))
print(alpha_range('g', 'v', -1))
print(alpha_range('z', 'h', -2))
print(alpha_range('w', 'e', 1))
print(alpha_range('G', 'V', 0))
print(alpha_range('t', 'p', 2))
print(alpha_range('N', 'I', -30))
print(alpha_range('n', 'c', -29))
print(alpha_range('F', 'L', -29))
print(alpha_range('z', 'o', -7))
print(alpha_range('k', 'g', 1))
print(alpha_range('b', 'f', -4))
print(alpha_range('H', 'Z', -13))
print(alpha_range('R', 'B', 5))
print(alpha_range('X', 'w', 6))