"""
Write a program to read n points and find the closest two of them.
Input
The input holds the number of points n and n lines, each holding a point {X and Y coordinate}.
Output
    The output holds the shortest distance and the closest two points.
    If several pairs of points are equally close, print the first of them (from top to bottom).
Hints
    Use the class Point you created in the previous task.
    Create an array  points that will keep all points.
    Create a method find_closest_points(points) that will check distance between every two pairs from the array of points and returns the two closest points in a new array.
    Print the closest distance and the coordinates of the two closest points.

Input

4
3 4
6 8
2 5
-1 3

Output

1.414
(3, 4)
(2, 5)
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y