"""
Roman Numerals
Create a function that takes in a Roman numeral as a string and converts it to an integer, returning the result. The function should work for all Roman numerals representing positive integers less than 4000.

The following table shows how digits will be represented in Roman numeral notation:

Place value	1	2	3	4	5	6	7	8	9
Ones	I	II	III	IV	V	VI	VII	VIII	IX
Tens	X	XX	XXX	XL	L	LX	LXX	LXXX	XC
Hundreds	C	CC	CCC	CD	D	DC	DCC	DCCC	CM
Thousands	M	MM	MMM	-	-	-	-	-	-
Examples
parse_roman_numeral("VII") ➞ 7

parse_roman_numeral("DCLXXIX") ➞ 679

parse_roman_numeral("MMMCMV") ➞ 3905
Notes
All letters will be in uppercase.
Assume all inputs will be well-formed Roman numerals.
While you could probably solve this by separately checking for each of these sequences inside the string, there is a smarter way. Think about the numerical value each individual letter has, and how the letter immmediately following it can affect that letter's numerical value.
"""
def parse_roman_numeral(num):

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(num):
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total



# roman_numerals = {
#     "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9,
#     "X": 10, "XX": 20, "XXX": 30, "XL": 40, "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90,
#     "C": 100, "CC": 200, "CCC": 300, "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800, "CM": 900,
#     "M": 1000, "MM": 2000, "MMM": 3000
# }
#
# def parse_roman_numeral(num):
#
#     thousands = ""
#     hundreds = ""
#     tens = ""
#     ones = ""
#
#     for i in num:
#         if i == 'M':
#             if not hundreds:
#                 thousands += i
#             else:
#                 hundreds += i
#         elif i in ["C","D"]:
#             if not tens:
#                 hundreds += i
#             else:
#                 tens += i
#         elif i in ["L", "X"]:
#             if not ones:
#                 tens += i
#             else:
#                 ones += i
#         elif i in ["V", "I"]:
#             ones += i
#
#     result = [thousands, hundreds, tens, ones]
#     return sum([roman_numerals[i] for i in result if i not in ''])

print(parse_roman_numeral("I"))
print(parse_roman_numeral("VIII"))
print(parse_roman_numeral("XXIX"))
print(parse_roman_numeral("LIV"))
print(parse_roman_numeral("CCV"))
print(parse_roman_numeral("CDXLIV"))
print(parse_roman_numeral("CMXCIX"))
print(parse_roman_numeral("M"))
print(parse_roman_numeral("MMMDCCCLXXXVIII"))
print(parse_roman_numeral("MMMCMX"))

