"""
String Compression from Characters Array
The function is given an array of characters. Compress the array into a string using the following rules. For each group of consecutively repeating characters:

If the number of repeating characters is one, append the string with only this character.
If the number n of repeating characters x is greater than one, append the string with "x" + str(n).
Examples
compress(["a", "a", "b", "b", "c", "c", "c"]) ➞ "a2b2c3"

compress(["a"]) ➞ "a"

compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) ➞ "ab12"

compress(["a", "a", "a", "b", "b", "a", "a"]) ➞ "a3b2a2"
"""
def compress(chars):
    if not chars:
        return ""

    compressed = ""
    current_char = chars[0]
    count = 1

    for i in range(1, len(chars)):
        if chars[i] == current_char:
            count += 1
        else:
            compressed += current_char
            if count > 1:
                compressed += str(count)
            current_char = chars[i]
            count = 1

    compressed += current_char
    if count > 1:
        compressed += str(count)

    return compressed


# def compress(chars):
#
#     temp = {}
#     total = ""
#
#     for i in chars:
#         if i in temp:
#             temp[i] += 1
#         else:
#             temp[i] = 1
#             key = next(iter(temp))
#             if i == key:
#                 continue
#             else:
#                 value = temp[key]
#                 total += str(key)
#                 if value != 1:
#                     total += str(value)
#                 temp.pop(key)
#
#     key = next(iter(temp))
#     value = temp[key]
#     total += str(key)
#     if value != 1:
#         total += str(value)
#
#     return total

print(compress(["a", "a", "b", "b", "c", "c", "c"]))
print(compress(["a"]))
print(compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
print(compress(["a", "a", "a", "b", "b", "a", "a"]))
