"""
You are given two values of the same type as input. The values can be of type int, char of string.
Create a function that returns the greater of the two values:
Hints
1.	For this function you need to create three functions with the same name and different signatures
2.	Create a function which will compare integers.
3.	Lastly you need to create a function to compare the other types.
4.	The last step is to read the input, use appropriate variables and call the function you’ve just written.
"""

value_type = input()
first_value = input()
second_value = input()


def compare_two_values(type_comp, first_val, second_val):
    """
    Compares values from different types
    :param type_comp: Str Type of the values
    :param first_val: Str First value to compare
    :param second_val: Str Second value to compare
    :return: Str The winning value from the comparision
    """
    winning_value = None
    if type_comp == 'int':
        if int(first_val) > int(second_val):
            winning_value = first_val
        else:
            winning_value = second_val
    else:
        if first_val > second_val:
            winning_value = first_val
        else:
            winning_value = second_val

    return winning_value


print(compare_two_values(value_type, first_value, second_value))
