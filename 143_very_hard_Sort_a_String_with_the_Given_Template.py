"""
Sort a String with the Given Template
The function is given two strings t - template, s - to be sorted. Sort the characters in s such that if the character is present in t then it is sorted according to the order in t and other characters are sorted alphabetically after the ones found in t.

Examples
custom_sort("edc", "abcdefzyx") ➞ "edcabfxyz"

custom_sort("fby", "abcdefzyx") ➞ "fbyacdexz"

custom_sort("", "abcdefzyx") ➞ "abcdefxyz"

custom_sort("", "") ➞ ""
Notes
The characters in t and s are all lower-case.
"""

def custom_sort(t, s):

    order = "".join([i for i in s if i in t])
    origin = "".join([i for i in s if i not in t])

    priority = {char: i for i, char in enumerate(t)}

    def get_sort_key(x):
        return priority.get(x, -1)

    sorted_s = ''.join(sorted(order, key=get_sort_key))
    return sorted_s + ''.join(sorted(origin))

print(custom_sort("edc", "abcdefzyx"))
print(custom_sort("fby", "abcdefzyx"))
print(custom_sort("", "abcdefzyx"))
print(custom_sort('cteqh', 'xnjanztmhg'))
print(custom_sort('jv', 'cxkafinfiuhnnaracsztbrcwaifwattzavwohoqskauififucq'))