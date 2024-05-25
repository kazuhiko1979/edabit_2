"""
Rectangle or Not?
Create a function that determines whether four coordinates properly create a rectangle. A rectangle has 4 sides and has 90 degrees for each angle. Coordinates are given as strings containing an x- and a y- coordinate: "(x, y)".

For this problem, assume none of the rectangles are tilted.

is_rectangle(["(0, 0)", "(0, 1)", "(1, 0)", "(1, 1)"]) ➞ True
Examples
is_rectangle(["(-4, 3)", "(4, 3)", "(4, -3)", "(-4, -3)"]) ➞ True

is_rectangle(["(0, 0)", "(0, 1)"]) ➞ False
# A line is not a rectangle!

is_rectangle(["(0, 0)", "(0, 1)", "(1, 0)"]) ➞ False
# Neither is a triangle!

is_rectangle(["(0, 0)", "(9, 0)", "(7, 5)", "(16, 5)"]) ➞ False
# A parallelogram, but not a rectangle!
Notes
A square is also a rectangle!
A parallelogram is NOT necessarily a rectangle (the rectangle is a special case of a parallelogram).
If the input is fewer than or greater than 4 coordinates, return False.
"""
import itertools

def is_rectangle(coordinates):

    points = []
    for point in coordinates:
        point = point.strip("()")
        x,y = map(int, point.split(','))
        points.append((x,y))
    if len(points) != 4:
        return False

    def is_parallel_sides(p1, p2, p3, p4):
        if (p2[0] - p1[0]) * (p4[1] - p3[1]) == (p2[1] - p1[1]) * (p4[0] - p3[0]):
            return True
        return False

    def distance(p1, p2):
        return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2

    for perm in itertools.permutations(points):
        A, B, C, D = perm
        if is_parallel_sides(A, B, C, D) and is_parallel_sides(A, D, B, C) and distance(A, B) == distance(C, D) and distance(A, D) == distance(B, C):
            return True
        return False


print(is_rectangle(["(-4, 3)", "(4, 3)", "(4, -3)", "(-4, -3)"]))
print(is_rectangle(["(0, 0)", "(0, 1)"]))
print(is_rectangle(["(0, 0)", "(0, 1)", "(1,0)"]))
print(is_rectangle(["(0, 0)", "(9, 0)", "(7,5)", "(16, 5)"]))
print(is_rectangle(["(0, 0)", "(1, 0)", "(0, 1)", "(0, 0)"]))
print(is_rectangle(["(1, 0)", "(1, 2)", "(2, 1)", "(2, 3)", "(3, 3)"]))
print(is_rectangle(["(-2, 2)", "(-2, -1)", "(5, -1)", "(5, 2)"]))