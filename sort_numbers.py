"""
Read a list of integers and sort them in ascending order. Print the output as shown in the examples below.
Hints
    Use the built-in method list.sort().
"""
nums_to_sort = list(map(int, input().split(' ')))
nums_to_sort.sort()
[print(item, end=' <= ') for item in nums_to_sort[:-1]]
print(nums_to_sort[-1])
