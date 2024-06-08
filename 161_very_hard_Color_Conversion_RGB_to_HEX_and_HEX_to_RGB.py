"""
[Color Conversion] RGB to HEX and HEX to RGB
Create a function that converts RGB to HEX and vice versa.

color_conversion("#ff09d3") converts the string param from HEX to RGB. color_conversion({"r": 235, "g": 64, "b": 52}) converts the dict param from RGB to HEX.

Examples
color_conversion("#ffffff") ➞ {"r": 255, "g": 255, "b": 255}

color_conversion("#ff0025") ➞ {"r": 255, "g": 0, "b": 37}

color_conversion({"r": 40, "g": 200, "b": 125}) ➞ "#28c87d"

color_conversion({"r": -1, "g": 0, "b": 256}) ➞ "Invalid input!"

color_conversion("c9bade") ➞ {"r": 201, "g": 186, "b": 222}
Notes
The RGB value must be between 0 and 255.
Hex value input can be prefixed with a hash (#) or without (see example #5).
"""
import re
def color_conversion(h):
    if type(h) is dict:
        result = []
        for i in h.values():
            if 0 <= i <= 255:
                result.append(hex(i)[2:].zfill(2))
            else:
                return 'Invalid input!'
        hex_string = ''.join(result)
        return '#' + hex_string

    pattern = re.compile(r'^#?[0-9a-fA-F]{6}$')
    if bool(pattern.match(h)):
        if h.startswith('#'):
            h = h[1:]
        r = int(h[0:2], 16)
        g = int(h[2:4], 16)
        b = int(h[4:6], 16)
        return {'r': r, 'g': g, 'b': b}

        # return result
    else:
        return 'Invalid input!'

print(color_conversion('#4f69c9'))
print(color_conversion("ffffff"))
print(color_conversion('#000000'))
print(color_conversion("#ff0025"))
print(color_conversion('#050106'))
print(color_conversion({'r': 126, 'g': 214, 'b': 131}))
print(color_conversion({'r': 255, 'g': 255, 'b': 255}))
print(color_conversion({'r': 0, 'g': 0, 'b': 0}))
print(color_conversion({'r': 3, 'g': 1, 'b': 200}))
print(color_conversion({'r': 201, 'g': 186, 'b': 222}))
print(color_conversion({'r': 256, 'g': 0, 'b': 0}))
print(color_conversion({'r': 0, 'g': 0, 'b': 256}))
print(color_conversion({'r': 0, 'g': -1, 'b': 0}))
print(color_conversion({'r': 0, 'g': 255, 'b': -10}))
print(color_conversion('f9ffef0'))
