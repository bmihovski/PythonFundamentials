"""
Create a class Box, which will represent a rectangular box.
The Box should have UpperLeft (Point), UpperRight (Point), BottomLeft (Point), BottomRight (Point).
Create, or use from the Lab, the class Point which has X (int) and Y (int) - coordinates in 2D space.
Move the CalculateDistance() method in the Point class, exactly as it is.
Then use "Point.CalculateDistance(point1, point2)" signature, to use the method.
Create 2 methods in the Box class:
CalculatePerimeter(width, height)
CalculateArea(width, height).
Make them return integers, representing the perimeter and area of the box.
The formulas are respectively - (2 * Width + 2 * Height) and (Width * Height).
The Width is the distance between the UpperLeft and the UpperRight Points,
and ALSO - the Bottomleft and the BottomRight Points.
The Height is the distance between the UpperLeft and the BottomLeft Points,
and ALSO - the UpperRight and the BottomRight Points.
You will receive several input lines in the following format:
{X1}:{Y1} | {X2}:{Y2} | {X3}:{Y3} | {X4}:{Y4}
Those will be the coordinates to UpperLeft, UpperRight, BottomLeft and BottomRight (IN THE SAME ORDER).
When you receive the command "end". You must print all Boxes in the following format:
"Box: {width}, {height}
 Perimeter: {perimeter}
 Area: {area}"

Examples

Input
0:2 | 2:2 | 0:0 | 2:0
-3:0 | 0:0 | -3:-3 | 0:-3
-2:2 | 2:2 | -2:-2 | 2:-2
end

Output
Box: 2, 2
Perimeter: 8
Area: 4
Box: 3, 3
Perimeter: 12
Area: 9
Box: 4, 4
Perimeter: 16
Area: 16
"""