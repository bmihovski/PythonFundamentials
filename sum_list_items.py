"""
Write a program, which reads a list of integers, calculates its sum and prints it.
The input consists of a number n (the number of items) + n integers, each as a separate line.
Hints
"	First, read the number n.
"	Read the integers in a for-loop.
"""
sum_items = list()
number_to_enter = int(input())

for item in range(number_to_enter):
    value = int(input())
    sum_items.append(value)

print(sum(sum_items))
