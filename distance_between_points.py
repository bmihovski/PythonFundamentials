from math import sqrt

"""
Write a method to calculate the distance between two points p1 {x1, y1} and p2 {x2, y2}.
Write a program to read two points (given as two integers) and print the Euclidean distance between them.
Hints
    Create a class Point holding properties X and Y.
    Write a method CalcDistance(p1, p2) that returns the distance between the given points - a number.
    Use this formula to calculate the distance between two points. How it works?
    Let's have two points p1 {x1, y1} and p2 {x2, y2}
    Draw a right-angled triangle
    Side a = |x1 - x2|
    Side b = |y1 - y2|
    Distance == side c (hypotenuse)
    c2 = a2 + b2 (Pythagorean theorem)
Distance = c = √(a^2+b^2 )
    You can use math.sqrt(number) method for calculating a square root.
    Print the distance formatted to the 3rd decimal point.

Input
3 4
6 8

Output
5.000
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def calc_distance(p1, p2):
    """
    Calculates distance between two points
    :param p1: (Obj) Point coordinates
    :param p2: (Obj) Point coordinates
    :return: (Float) Distance between points
    """
    delta_x = p2.x - p1.x
    delta_y = p2.y - p1.y
    return sqrt(delta_x ** 2 + delta_y ** 2)


def read_point_coordinates():
    """
    Take point coordinates from stdin
    :return: (Obj) Point coordinates int type
    """
    line = map(int, input().split())
    x, y = line
    point = Point(x, y)
    return point


point1 = read_point_coordinates()
point2 = read_point_coordinates()

print(f'{calc_distance(point1, point2):.3f}')
