"""
Write a program to read a list of integers, an integer p, multiply each item by p and print the resulting list.
Hints
"	Read the list
"	Loop through the list, multiplying each item by p
"	Finally, print the resulting list, using a for loop
"""
nums_to_multiply = input().split(' ')
mult_num = int(input())
print(*[int(item) * mult_num for item in nums_to_multiply], sep=' ')
