"""
Create a program that reads an integer number and multiplies the sum of all its
even digits by the sum of all its odd digits:
Hints
1.	Create a function with a name describing its purpose.
    The function should have a single parameter and will return value.
    Also the function will call two other functions.
2.	Create two other functions each of which will sum either even or odd digits.
3.	Implement the logic for summing odd digits.
4.	Do the same for the function that will sum even digits.
5.	As you test your solution you may notice that it doesn't work for negative numbers.
    Following the program execution line by line, find and fix the bug.
"""
input_number = input()


def get_integers_from_str(str_int):
    """
    Produce a list from str integers
    :param str_int: Str Numeric value from stdin
    :return: List: List of separated values in Str type
    """
    list_of_ints = [int(s) for s in str_int if s.isdigit()]

    return list_of_ints


def get_multiple_of_events_and_odds(even_num, odd_num):
    """
    Calculates a multiple of even and odd numbers
    :param even_num: Int Even number
    :param odd_num: Int Odd number
    :return:
    """
    multiple_of_even_odd = even_num * odd_num

    return multiple_of_even_odd


def get_sum_of_even_digits(list_of_ints):
    """
    Calculates a sum of even numbers from a list of numbers
    :param list_of_ints: List of numbers
    :return: Int Sum of the even digits
    """
    even_sum = 0
    for n in list_of_ints:
        if (n % 2) == 0:
            even_sum += n
        else:
            continue

    return even_sum


def get_sum_of_odd_digits(list_of_ints):
    """
    Calculates a sum of odd numbers from a list of numbers
    :param list_of_ints: List of numbers
    :return:
    """
    odd_sum = 0
    for n in list_of_ints:
        if (n % 2) != 0:
            odd_sum += n
        else:
            continue

    return odd_sum


even_odd_numbers = get_integers_from_str(input_number)
sum_of_even = get_sum_of_even_digits(even_odd_numbers)
sum_of_odd = get_sum_of_odd_digits(even_odd_numbers)
print(get_multiple_of_events_and_odds(sum_of_even, sum_of_odd))
