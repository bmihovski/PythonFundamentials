"""
Create a function for printing triangles as shown below:
Hits:
1.	After you read the input.
2.	Start by creating a function for printing a single line from a given start to a given end. Choose a meaningful name
    for it, describing its purpose.
3.	Think how you can use it to solve the problem.
4.	After you spent some time thinking, you should have come to the conclusion that you will need two loops
5.	In the first loop you can print the first half of the triangle without the middle line.
6.	Next, print the middle line.
7.	Lastly, print the rest of the triangle.
"""
triangle_value = int(input())


def print_the_triangle(stop_value):
    """
    Print single line from given values
    :param stop_value: Int last value to be printed
    :return: None
    """
    values_to_be_printed = list()
    for i in range(1, stop_value + 1):
        values_to_be_printed.append(i)
        print(*values_to_be_printed)
    for i in range(stop_value - 1, 0, -1):
        print(*values_to_be_printed[:i])


print_the_triangle(triangle_value)
