"""
On the first line of the input, you will receive n -  the number of lines of clothes,
which came prepackaged for the wardrobe.
On the next n lines, you will receive the clothes for each color in the format:
"	"{color} -> {item1},{item2},{item3}…"
If a color is added a second time, add all items from it and count the duplicates.
Finally, you will receive the color and item of the clothing, that you need to look for.
Output
Go through all the colors of the clothes and print them in the following format:
{color} clothes:
* {item1} - {count}
* {item2} - {count}
* {item3} - {count}
…
* {itemN} - {count}
If the color lines up with the clothing item, print "(found!)" alongside the item.
See the examples to better understand the output.

Input
4
Blue -> dress,jeans,hat
Gold -> dress,t-shirt,boxers
White -> briefs,tanktop
Blue -> gloves
Blue dress

Output
Blue clothes:
* dress - 1 (found!)
* jeans - 1
* hat - 1
* gloves - 1
Gold clothes:
* dress - 1
* t-shirt - 1
* boxers - 1
White clothes:
* briefs - 1
* tanktop - 1
"""
wardrobe = dict()
input_clothes = list()
input_checkouts = list()
items_wardrobe = int(input())
printed = []


def _items_wardrobe(color, cloth):
    """
    Prints the content of wardrobe by color and matches
    :param color: (Str) The color of clothes
    :param cloth: (Str) The kind of cloth
    :return: None
    """
    print(f'{color} clothes:')
    for cloth in wardrobe[color]:
        if cloth in printed:
            continue
        print(f'* {cloth} - {wardrobe[color].count(cloth)}', end='')
        if color == input_checkouts[0] and cloth == input_checkouts[1]:
            print(f' (found!)', end='')
        print()
        printed.append(cloth)


for item in range(items_wardrobe):
    input_clothes = input().split(' -> ')
    clothes = input_clothes[1].split(',')
    if input_clothes[0] in wardrobe:
        wardrobe[input_clothes[0]].extend(clothes)
    else:
        wardrobe.update({input_clothes[0]: clothes})


input_checkouts = input().split()
{_items_wardrobe(key, input_checkouts[1]) for key in wardrobe.keys()}
