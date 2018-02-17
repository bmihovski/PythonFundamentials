from pickle import dump, load

"""
You have been tasked to create a File Database for several stocked products at a universal shop.
A product has a Type (string), Name (string), Price (decimal) and Quantity (integer).
The type of the product can be - "Food", "Electronics", "Domestics".
The name of the product may consist of any ASCII character, except space.
The price of the product will be a floating-point number with up to 20 digits after the decimal point.
The quantity of the product will be an integer in range [0, 1000].
The software program you must build should be a Console interface.
You will receive several input lines, containing information about products, in the following format:
{name} {type} {price} {quantity}

You should store every product, with its respective properties.
If you receive a product NAME, which already exists AND has the SAME TYPE, you should REPLACE its price and quantity,
with the given ones.
The products are stored virtually, in your program's memory - they are called ACTIVE products.
When you receive the command "stock", in the input, you must stock all products, you have, in a file.
When you receive the command "analyze", in the input, you must print all STOCKED products, in alphabetical order,
by their TYPE, each printed in the following format:
"{type}, Product: {name}
Price: ${price}, Amount Left: {quantity}"
In case there are NO products print "No products stocked".
When you receive the command "sales", in the input, you must print all types of ACTIVE products, and the income, earned
if all products and their quantities from that TYPE are sold. In other words, you need to calculate for every product
from the respective type, its quantity * price. You must then sum all sums, from the products - that's the INCOME.
The output should be formatted like this:
"{firstType}: ${income}
{secondType}: ${income}
{thirdType}: ${income}"
The types must be ordered in descending order, by their total income. If one of the types, has NO products,
DO NOT PRINT IT.
ALL PRICES, must be FORMATTED to the second digit, after the decimal point.
The input ends when you receive the command "exit". You do NOT print anything, you do NOT store anything on files. . .
You just exit the program.
Note
You only STOCK products in the external FILE, when you receive the command "stock".
Do NOT stock products at the end of the program execution.
When you start the program, you should check if you have any stocked products, and if you do,
you should load them into your database.

Examples

Input
SamsungSmartTV Electronics 4000.50 10
Banana Food 1.50 10000
IPhone7 Electronics 1000 100
Apple Food 1 100000
Microwave Electronics 149.99 2500
Toster Electronics 20.00 15730
analyze
sales
Mopper Domestics 10.05 10000
ToiletPaper Domestics 5.50 100000
sales
analyze
sales
stock
exit

Output
Electronics: $829580.00
Food: $115000.00
No products stocked
Electronics: $829580.00
Domestics: $650500.00
Food: $115000.00
"""
STOCK_FILE = "stock.p"
food = dict()
electronics = dict()
domestics = dict()
lines_input = list()


class Product:
    def __init__(self, price, quantity):
        self.price = float(price)
        self.quantity = int(quantity)


def add_update_product(prod_type, prod_name, price, qty):
    if prod_type == 'Food':
        food.update({prod_name: Product(price, qty)})
    elif prod_type == 'Electronics':
        electronics.update({prod_name: Product(price, qty)})
    else:
        domestics.update({prod_name: Product(price, qty)})


while True:
    lines_input = input().split()
    try:
        with open(STOCK_FILE, 'rb') as stock_db:
            food, electronics, domestics = load(stock_db)
    except FileNotFoundError:
        pass
    if 'exit' in lines_input[0]:
        break
    elif 'sales' in lines_input[0]:
        with open(STOCK_FILE, 'wb') as stock_db:
            dump((food, electronics, domestics), stock_db)
    elif 'analyze' in lines_input[0]:
        if not domestics.keys():
            print('No products stocked')
        else:
            {print(f'Domestics, Product: {product} Price: ${domestics[product].price:.2f}, Amount Left: '
                   f'{domestics[product].quantity}') for product in sorted(domestics.keys())}
        if not electronics.keys():
            print('No products stocked')
        else:
            {print(f'Electronics, Product: {product} Price: ${electronics[product].price:.2f}, Amount Left: '
                   f'{electronics[product].quantity}') for product in sorted(electronics.keys())}
        if not food.keys():
            print('No products stocked')
        else:
            {print(f'Food, Product: {product} Price: ${food[product].price:.2f}, Amount Left: '
                   f'{food[product].quantity}') for product in sorted(food.keys())}
    elif 'sales' in lines_input[0]:
        electronics_sales = map(lambda x: electronics[x].price * electronics[x].quantity, electronics.keys())
        print(*electronics_sales)
        #"{firstType}: ${income} {secondType}: ${income}  {thirdType}: ${income}"
    elif lines_input[0] in food.keys() or lines_input[0] in electronics.keys() or lines_input[0] in domestics.keys():
        if lines_input[1] == 'Food':
            add_update_product(prod_name=lines_input[0], prod_type=lines_input[1],
                               price=lines_input[2], qty=lines_input[3])
        elif lines_input[1] == 'Electronics':
            add_update_product(prod_name=lines_input[0], prod_type=lines_input[1],
                               price=lines_input[2], qty=lines_input[3])
        else:
            add_update_product(prod_name=lines_input[0], prod_type=lines_input[1],
                               price=lines_input[2], qty=lines_input[3])
    else:
        if lines_input[1] == 'Food':
            add_update_product(prod_name=lines_input[0], prod_type=lines_input[1],
                               price=lines_input[2], qty=lines_input[3])
        elif lines_input[1] == 'Electronics':
            add_update_product(prod_name=lines_input[0], prod_type=lines_input[1],
                               price=lines_input[2], qty=lines_input[3])
        else:
            add_update_product(prod_name=lines_input[0], prod_type=lines_input[1],
                               price=lines_input[2], qty=lines_input[3])
