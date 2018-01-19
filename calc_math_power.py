"""
Create a function that calculates and returns the value of a number raised to a given power:
1.	As usual, read the input
2.	Create a function which will have two parameters - the number and the power, and will return a result
3.	Print the result
"""
number = float(input())
power = float(input())


def calculate_math_power(num, pow):
    """
    Calculates math power by given number and power values
    :param num: Float Number to be calculated
    :param pow: Float Power value to be calculated
    :return: Float Output
    """
    number_to_power = num ** pow

    return number_to_power


print(calculate_math_power(number, power))
