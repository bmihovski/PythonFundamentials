"""
Read a list of integers and extract all square numbers from it and print them in descending order.
A square number is an integer which is the square of any integer. For example, 1, 4, 9, 16 are square numbers.
Hints
    To find out whether an integer is "square number", check whether its square root is integer number
    (has no fractional part):
        if (√num == (int)√num) …
    To order the results list in descending order use sorting with reverse
"""
nums_to_check = list(map(int, input().split()))
nums_to_check.sort()
nums_to_check.reverse()
[print(item, end=' ') for item in nums_to_check if item**0.5 == int(item**0.5)]
