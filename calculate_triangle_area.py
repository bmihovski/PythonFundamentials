"""
Create a function that calculates and returns the area of a triangle by given base and height.
Use a general formatting with 12 digits after the decimal point (e.g. {area:.12g})
Hints
1.	After reading the input
2.	Create a function that calculates the area.
3.	Invoke the function in the main and save the return value in a new variable.
"""
triangle_base = float(input())
triangle_height = float(input())


def triangle_area(base, height):
    """
    Calculates triangle area by given base and height
    :param base: Float triangle base distance
    :param height: Float triangle height distance
    :return: Float Calculated triangle area
    """
    calc_triangle_area = (base * height) / 2

    return calc_triangle_area


if __name__ == '__main__':
    calculated_area = triangle_area(triangle_base, triangle_height)
    print(f'{calculated_area:.12g}')

