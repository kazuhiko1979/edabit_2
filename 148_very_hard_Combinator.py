"""
Combinator
Create a function that, given a list of string lists, returns an list of all combinations as concatenated strings.

The function is called with a list of lists containing strings.
The task is to combine each string of each array with each string of each other list.
If one of the string lists is empty, the function will return an empty list.
The function will accept an optional second string parameter. This parameter, if specified, is to be used to combine two strings.

Examples
combinator([["a", "b"], ["c", "d"]]) ➞ ["ac", "ad", "bc", "bd"]

combinator([["a"], ["a", "b"], "abc"]) ➞ ["aaa", "aab", "aac", "aba", "abb", "abc"]

combinator([["foo", "bar"], ["baz", "bamboo"]], " ") ➞ ["foo baz", "foo bamboo", "bar baz", "bar bamboo"]

combinator([[]]) ➞ []
Notes
The order of the given strings must be retained in the combinations.
You can assume that:
The function is always called with a list of string lists and lists can be empty.
"""
import itertools

def combinator(lst,separator=''):

    # temp = [list(i) if not isinstance(i, list) else i for i in lst]
    temp = [list(i) if not isinstance(i, list) else [j for j in i if j != ' '] for i in lst]
    combinations = list(itertools.product(*temp))
    result = [''.join(pair) if all(len(item) <= 2 for item in pair) else ' '.join(pair) for pair in combinations]
    return result

print(combinator([['a']]))
print(combinator([['ab'], ['ba']]))
print(combinator([['a', 'b']]))
print(combinator([["a", "b"], ["c", "d"]]))
print(combinator([["a"], ["a", "b"], "abc"]))
print(combinator([["foo", "bar"], ["baz", "bamboo"]],' '))
print(combinator(['abcd', 'efgh', 'ijkl']))
print(combinator([[]]))
print(combinator([['a', 'b'], [], ['e', 'f']]))
print(combinator([[], ['e', 'f']]))