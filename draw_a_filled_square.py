"""
Draw at the console a filled square of size n like in the example:
1.	Read the input
2.	Create a function which will print the top and the bottom rows (they are the same). Don’t forget to give it a descriptive name and to give it as a parameter some length
3.	Create the function which will print the middle rows.
4.	Use the functions that you've just created to draw a square.
"""
square_length = int(input())


def print_top_or_bottom_rows(length):
    """
    Prints top or bottom line of the square
    :param lenght: Int square length which will be multiplied by 2
    :return: None
    """
    print('-' * (length * 2))


def print_middle_rows(length):
    """
    Prints middle rows of the square
    :param length: Int square length
    :return:
    """
    doubled_length = length * 2
    for z in range(0, length - 2):
        for i in range(1, doubled_length + 1):
            if i == 1 or i == length * 2:
                print('-', end='')
            elif (i % 2) == 0:
                print('\\', end='')
            else:
                print('/', end='')
        print()


print_top_or_bottom_rows(square_length)
print_middle_rows(square_length)
print_top_or_bottom_rows(square_length)