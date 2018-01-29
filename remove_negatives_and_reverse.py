"""
Read a list of integers, remove all negative numbers from it and print the remaining items in reversed order.
In case of no items left in the list, print "empty".
Hints
    Read the list
    Create a new empty list for the results.
    Scan the input list from the end to the beginning.
    Check each item and append all non-negative items to the result list.
    Finally, print the results list (at a single line holding space-separated numbers).
"""
nums_to_check = list(map(int, input().split(' ')))
nums_to_print = list()
[nums_to_print.append(item) for item in reversed(nums_to_check) if item > 0]
if nums_to_print:
    [print(item, end=' ') for item in nums_to_print]
else:
    print('empty')
