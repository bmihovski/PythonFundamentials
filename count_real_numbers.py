"""
Read a list of real numbers and print them in ascending order along with their number of occurrences.
Hints
    Use dictionary (key=nums, value=count) named counts.
    Pass through each input number num and increase counts[num] (when num exists in the dictionary) or assign counts[num] = 1 (when num does not exist in the dictionary).
    Pass through all numbers num in the dictionary (counts.keys()) and print the number num and its count of occurrences counts[num].
"""
nums_stdin = map(float, input().split(' '))
counts = dict()

for num in nums_stdin:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

{print(f'-> {value} times'): print(f'{key}', end=' ') for key, value in sorted(counts.items())}
