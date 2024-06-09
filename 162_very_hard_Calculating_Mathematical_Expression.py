"""
Calculating Mathematical Expression
Create a function that takes a mathematical expression as a string, list of numbers on which the mathematical expression is to be calculated and return the result as a list of string.

Examples
mathematical("f(y)=y+1",[1,2]) ➞ ["f(1)=2","f(2)=3"]

mathematical("f(y)=y^2",[1,2,3]) ➞ ["f(1)=1","f(2)=4","f(3)=9"]

mathematical("f(y)=yx3",[1,2,3]) ➞ ["f(1)=3","f(2)=6","f(3)=9"]
Notes
List of numbers are positive integers.
In the algebraic expression x = *
"""

def mathematical(exp, numbers):

    expression = exp.split('=')[1].replace('^', '**').replace('x', '*')
    total = []
    for y in numbers:
        result = eval(expression)
        total.append("f({})={}".format(y, int(result)))
    return total

    # total = []
    # for y in numbers:
    #     if '^' in exp:
    #         result = eval(exp.split('=')[1].replace('^', '**'))
    #         total.append("f({})={}".format(y, result))
    #     elif 'x' in exp:
    #         result = eval(exp.split('=')[1].replace('x', '*'))
    #         total.append("f({})={}".format(y, result))
    #     else:
    #         result = eval(exp.split('=')[1])
    #         total.append("f({})={}".format(y, result))
    #
    # return total

print(mathematical("f(y)=y+1",[1,2]))
print(mathematical("f(y)=y^2",[1,2,3]))
print(mathematical("f(y)=yx3",[1,2,3]))
print(mathematical("f(y)=y-2",[1,2,3]))
print(mathematical("f(y)=y/3",[3, 6, 9]))