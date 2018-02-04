"""
A supermarket has products which have quantities. Your task is to stock the shop before Exam Sunday.
Until you receive the command "shopping time", add the various products to the shop's inventory,
keeping track of their quantity (for inventory purposes).
When you receive the aforementioned command, the students start pouring in before the exam and buy various products.
The format for stocking a product is: "stock {product} {quantity}".
The format for buying a product is: "buy {product} {quantity}".
If a student tries to buy a product, which doesn't exist, print "{product} doesn't exist".
If it does exist, but it's out of stock, print "{product} out of stock".
If a student tries buying more than the quantity of that product,
sell them all the quantity of the product (the product is left out of stock, don't print anything).
When you receive the command "exam time",
your task is to print the remaining inventory in the following format: "{product} -> {quantity}".
If a product is out of stock, do not print it.
Input	             Output
stock Boca_Cola 10   Boca_Cola -> 15
stock Boca_Cola 10
stock Kay's 3
stock Kay's 2
shopping time
buy Boca_Cola 5
buy Kay's 5
exam time

"""
inputs_stdin = list()
inventory = dict()


def _add_to_inventory(supplies):
    """
    Update the inventory with new supplies
    :param supplies: (List) Name and qty of item
    :return: None
    """
    if supplies[1] in inventory:
        inventory.update({supplies[1]: (inventory[supplies[1]] + int(supplies[2]))})
    else:
        inventory.update({supplies[1]: int(supplies[2])})


def _add_to_cart(items):
    """
    Add to items cart and inform out stock
    :param items: (List) Name and qty of item to buy
    :return:
    """
    if items[1] not in inventory:
        print(items[1] + " doesn't exist")
    elif inventory[items[1]] == 0:
        print(items[1] + ' out of stock')
    elif (inventory[items[1]] - int(items[2])) < 0:
        inventory.update({items[1]: 0})
    else:
        inventory.update({items[1]: (inventory[items[1]] - int(items[2]))})


while 'exam' not in inputs_stdin:
    inputs_stdin = input().split(' ')

    if 'exam' in inputs_stdin:
        continue
    elif 'stock' in inputs_stdin:
        _add_to_inventory(inputs_stdin)
    elif 'buy' in inputs_stdin:
        _add_to_cart(inputs_stdin)

{print(f'{item} -> {inventory[item]}') for item in inventory.keys() if inventory[item] > 0}
