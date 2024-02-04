"""
Gaderypoluki Cipher
Create a function that takes an encryption key (a string with an even number of characters) and a message to encrypt. Group the letters of the key by two:

"gaderypoluki" -> "ga de ry po lu ki"
Now take the message for encryption. If the message character appears in the key, replace it with an adjacent character in the grouped version of the key. If the message character does not appear in the key, leave it as is. If the letter in the key occurs more than once, the first result is used. For example: use the above key, if the letter "a" appeared in the message, it would be replaced with "g" since "g" in the adjacent letter.

Return the encrypted message.

Examples
encrypt("ab c", "abc ab") ➞ "ba cba"

encrypt("otorhinolaryngological", "My name is Paul") ➞ "Mr olme hs Plua"

encrypt("gaderypoluki", "This is an encrypted message") ➞ "Thks ks gn dncyrotde mdssgad"

"""

def encrypt(key, message):
    d = dict()
    for i, c in enumerate(key):
        if c not in d:
            if i % 2:
                d[c] = key[i - 1]
            else:
                d[c] = key[i + 1]
    print(d)
    return "".join(d[c] if c in d else c for c in message)

# def encrypt(key, message):
#
#     nested_key = []
#     for i in range(0, len(key), 2):
#         nested_key.append([key[i:i+2]])
#
#     message_index = 0
#     # print(message[2])
#     result = ""
#
#     while message_index < len(message):
#
#         character_to_find = message[message_index]
#         flag = False
#
#         for sublist in nested_key:
#             if character_to_find in sublist[0]:
#                 index = sublist[0].index(character_to_find)
#                 if index > 0:
#                     result += sublist[0][index - 1]
#                     message_index += 1
#                     flag = True
#                 elif index < len(sublist[0]) - 1:
#                     result += sublist[0][index + 1]
#                     message_index += 1
#                     flag = True
#             if character_to_find == " ":
#                 result += " "
#                 message_index += 1
#                 flag = True
#                 break
#
#         if not flag:
#             result += character_to_find
#             message_index += 1
#
#     return result

print(encrypt("ab c", "abc ab"))
print(encrypt("otorhinolaryngological", "My name is Paul"))
print(encrypt("gaderypoluki", "This is an encrypted message"))