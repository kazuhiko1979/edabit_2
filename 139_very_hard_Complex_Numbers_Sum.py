"""
Complex Numbers Sum
Mubashir needs your help in his maths homework.

Create a function which takes a list of Complex Numbers and returns the sum as a string.

Examples
sum_complex(["2+3i", "3-i"]) ➞ "5+2i"

sum_complex(["1", "1"]) ➞ "2"

sum_complex(["i", "2i", "3i"]) ➞ "6i"
"""





def sum_complex(lst):
    if not lst:
        return "0"

    real, imag = 0, 0

    for s in lst:
        num = complex(s.replace('i', 'j'))
        real += num.real
        imag += num.imag

    real = int(real)
    imag_str = str(int(imag)) + "i" if int(imag) != 0 else ""

    if imag_str == "1i":
        imag_str = "i"
    elif imag_str == "-1i":
        imag_str = "-i"
    elif imag_str == "0i":
        imag_str = ""

    if real == 0:
        real = ""

    if real and imag_str:
        return "{}+{}".format(real, imag_str) if imag_str[0] != "-" \
            else "{}{}".format(real, imag_str)
    elif real:
        return str(real)
    elif imag_str:
        return imag_str
    else:
        return "0"

# Test cases
print(sum_complex([]))  # "0"
print(sum_complex(["3+4i"]))  # "3+4i"
print(sum_complex(["123+456i"]))  # "123+456i"
print(sum_complex(["0"]))  # "0"
print(sum_complex(["-i"]))  # "-i"
print(sum_complex(["1", "1"]))  # "2"
print(sum_complex(["-5", "5"]))  # "0"
print(sum_complex(["1", "10", "100", "1000"]))  # "1111"
print(sum_complex(["2+3i","3-i"]))  # "5+2i"
print(sum_complex(["5+4i", "11+3i"]))  # "16+7i"
print(sum_complex(["-2-4i", "-8+6i"]))  # "-10+2i"
print(sum_complex(["-1-i", "7+10i"]))  # "6+9i"
print(sum_complex(["1","-3+i"]))  # "-2+i"
print(sum_complex(["1","-3-i"]))  # "-2-i"
print(sum_complex(["3+4i", "3-4i"]))  # "6"
print(sum_complex(["10+i", "10-i", "9"]))  # "29"
print(sum_complex(["2+3i", "0", "0"]))  # "2+3i"
print(sum_complex(["2+i", "3+2i", "-5-2i"]))  # "i"
print(sum_complex(["2+i", "3+2i", "-5-4i"]))  # "-i"
print(sum_complex(["10+5i", "1-i", "-i"]))  # "11+3i"
print(sum_complex(["i", "2i", "3i"]))  # "6i"
print(sum_complex(["-i", "-3i", "1+i"]))  # "1-3i"
print(sum_complex(["-1000i", "1000i", "1234"]))  # "1234"
print(sum_complex(["-i", "123", "4-i"]))  # "127-2i"



# def sum_complex(lst):
#
#     if not lst:
#         return "0"
#
#     real = 0
#     imag = 0
#
#     for s in lst:
#         if "i" in s:
#             s = s.replace(s[s.index("i")], "j")
#             num = complex(s)
#             real += num.real
#             imag += num.imag
#         else:
#             real += int(s)
#
#     real = int(real)
#     imag = str(int(imag)) + "i"
#
#     if imag[:-1] == "1":
#         imag = "i"
#     if imag[:-1] == "-1":
#         imag = "-i"
#     if imag[:-1] == "0":
#         imag = ""
#
#     # print(real, imag)
#     if real == 0:
#         real = ""
#     if imag == 0:
#         imag == ""
#
#     # print(imag[0])
#     if real and imag:
#         if imag[0] != "-":
#             return "{}+{}".format(real,imag)
#         else:
#             return "{}{}".format(real, imag)
#     elif real:
#         return str(real)
#     elif imag:
#         return imag
#     else:
#         return "0"






# def sum_complex(lst):
#
#     r = []
#     im = []
#
#     if lst == []:
#         return 0
#
#     for s in lst:
#
#         if "i" in s:
#             s = s.replace(s[s.index("i")], "j")
#             r.append(complex(s).real)
#             im.append(complex(s).imag)
#         else:
#             return sum([int(i) for i in lst])
#
#     return "{}j".format(int(sum(im))) if sum(r) == 0 \
#         else "{}+{}j".format(int(sum(r)), int(sum(im)))

# print(sum_complex([]))
# print(sum_complex(["2+3i", "3-i"]))
# print(sum_complex(["123+456i"]))
# print(sum_complex(["0"]))
# print(sum_complex(["1", "1"]))
# print(sum_complex(["i", "2i", "3i"]))

