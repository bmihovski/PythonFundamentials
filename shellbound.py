from collections import defaultdict
from math import ceil

"""
Vladi is a crab. Crabs are scared of almost anything, which is why they usually hide in their shells.
Vladi is a rich crab though. He has acquired many outer shells, in different regions,
in which he can hide - each with a different size.
However, it is really annoying to look after all your shells when they are so spread out.
That is why Vladi decided to merge all shells in each region, so that he has one big shell for every region.
He needs your help to do that.
You will be given several input lines containing a string and an integer, separated by a space.
The string will represent the region's name, and the integer - the shell in the given region, size.
You must store all shells in their corresponding regions.
If the region already exists, add the new shell to it. Make sure you have NO duplicate shells (shells with same size).
Vladi doesn't like shells to have the same size.
When you receive the command "Aggregate", you must stop reading input lines, and you must print every region,
all of the shells in that region, and the size of the giant shell after you've merged them in the following format:
{regionName} -> {shell 1, shell 2…, shell n…} ({giantShell})
The giant shell size is calculated when you subtract the average of the shells from the sum of the shells.
Or in other words: (sum of shells) - ((sum of shells) / (count of shells)).
Constraints
    All numeric data will be represented with integer variables in range [0…1.000.000.000].

Input

Sofia 50
Sofia 20
Sofia 30
Varna 10
Varna 20
Aggregate

Output
Sofia -> 50, 20, 30 (67)
Varna -> 10, 20 (15)
"""
vladi_shells = defaultdict(list)
input_shells = list()


def _print_shell_results(place):
    """
    Prints shell location, area and combined area of final shell
    :param place: (Str) Shell location
    :return: None
    """
    print(f'{place} -> ', end='')
    print(*vladi_shells[place], sep=', ', end=' ')
    print(f'({ceil(sum(vladi_shells[place]) - (sum(vladi_shells[place]) / len(vladi_shells[place])))})')


while True:
    input_shells = input().split()
    if 'Aggregate' in input_shells:
        break
    elif input_shells[0] in vladi_shells:
        if int(input_shells[1]) not in vladi_shells[input_shells[0]]:
            vladi_shells[input_shells[0]].append(int(input_shells[1]))
    else:
        vladi_shells[input_shells[0]].append(int(input_shells[1]))

{_print_shell_results(key) for key in vladi_shells.keys()}
