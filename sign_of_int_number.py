"""
Create a function that prints the sign of an integer number n.
"""

number_stdin = int(input())

def check_int_type(int_to_check):
    """
    Check the type of input integer and notify the user
    :param int_to_check: Int
    :return: message_to_user: Str
    """
    if int_to_check > 0:
        msg_to_user = f'The number {int_to_check} is positive.'
    elif int_to_check < 0:
        msg_to_user = f'The number {int_to_check} is negative.'
    else:
        msg_to_user = f'The number {int_to_check} is zero.'

    return msg_to_user

print(check_int_type(number_stdin))
