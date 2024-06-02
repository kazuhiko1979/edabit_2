"""
Bracket Logic
Brackets and parentheses in mathematical expressions have to conform to certain logical rules. Every opening bracket must have a closing mate somewhere further down the line. Although brackets can be nested, different types cannot overlap:

([<x+y>+3]-1) makes sense because each set of brackets contains or is contained by another set.
([<x+y>+3)-1] makes no sense because the parentheses and the square brackets overlap.
Given a string expression that can contain four types of brackets: () <> [] {}, create a function that returns True if the bracket logic is valid and False if it is not.

Examples
bracket_logic("[<>()]") ➞ True

bracket_logic("[<(>)]") ➞ False

bracket_logic("[(a*b+<7-c>+9]") ➞ False
# Opening parenthesis has no mate.

bracket_logic("[{(h*i+3)-12]/4*x+2}") ➞ False
# Square and curly brackets overlap.

bracket_logic("[ab(c/d<e-f+(7*6)>)+2]") ➞ True
Notes
Any characters other than the brackets can be ignored.
"""

def bracket_logic(xp):
    stack = []
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    for char in xp:
        if char in pairs.keys():
            stack.append(char)
        elif char in pairs.values():
            if not stack:
                return False
            open_char = stack.pop()
            if pairs[open_char] != char:
                return False
    return len(stack) == 0

print(bracket_logic("{b}{y}{ }[x][{{(t)-}{}](t<w(^)>)-b}<[g](x{u[ ]})y>"))
print(bracket_logic("{f}[t[[]]<[+](w)t>u(h)(%){f}[d{e}]{c(/)}<w>][v]"))
print(bracket_logic("[(t)d]</{h}><<a <( )e>[*]{e{e}}<w{x[^]}>>"))
print(bracket_logic("{g}((-) ^>b)[^]{{*<->}(w)(u)(%)}({/}c)(%)[g{b}]<z({<< >w>c}d)[b]>"))
print(bracket_logic("(y)(c)(){[[ ]z] [{+}z[*]]{+}}([d]<y<e>>c)[b][b]"))
print(bracket_logic("((^(b))e>(<d<w>>(({a}/(g)){t</)}b(d)){[v]u})"))
print(bracket_logic("{([%]</>u)<{<y{v}>{<c>h}{y}f}[y]{<*>e}[^]v><[h]d>}[d]"))
print(bracket_logic("{a}{<(^)(b)%>[z]<->e}[{z}%]{<^>g}<[h] ({ }y[*]<v>)>{x[+]<^>}<v>[]"))