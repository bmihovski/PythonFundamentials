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
FIRST_TYPE = "Domestics"
SECOND_TYPE = "Electronics"
THIRD_TYPE = "Food"
prod = dict()
lines_input = list()


class Product:
    def __init__(self, prod_type, price, quantity):
        """
        Constructs product object
        :param prod_type: (Str) Product type
        :param price: (Float) Product price
        :param quantity: (Int) Product quantity
        """
        self.prod_type = str(prod_type)
        self.price = float(price)
        self.quantity = int(quantity)


while True:
    lines_input = input().split()
    try:
        with open(STOCK_FILE, 'rb') as stock_db:
            prod = load(stock_db)
    except FileNotFoundError:
        pass
    if 'exit' in lines_input[0]:
        break
    elif 'stock' in lines_input[0]:
        with open(STOCK_FILE, 'wb') as stock_db:
            dump(prod, stock_db)
    elif 'analyze' in lines_input[0]:
        {print(f'{props.prod_type}, Product: {name} Price: ${props.price:.2f}, Amount Left: '
               f'{props.quantity}')
         if props.prod_type == FIRST_TYPE or props.prod_type == SECOND_TYPE
            or props.prod_type == THIRD_TYPE else print('No products stocked') for name, props in
         sorted(prod.items(), reverse=True)}
    elif 'sales' in lines_input[0]:
        incomes_dom = 0
        incomes_elec = 0
        incomes_food = 0
        for index, product in enumerate(prod.values()):
            if product.prod_type == FIRST_TYPE:
                incomes_dom += (product.price * product.quantity)
            if product.prod_type == SECOND_TYPE:
                incomes_elec += (product.price * product.quantity)
            if product.prod_type == THIRD_TYPE:
                incomes_food += (product.price * product.quantity)
        if incomes_dom > 0:
            print(f'{FIRST_TYPE}: ${incomes_dom}')
        if incomes_elec > 0:
            print(f'{SECOND_TYPE}: ${incomes_elec}')
        if incomes_food > 0:
            print(f'{THIRD_TYPE}: ${incomes_food}')
    elif lines_input[0] in prod.keys():
        product_type = prod[lines_input[0]].prod_type
        prod.update({lines_input[0]: Product(prod_type=product_type,
                                             price=lines_input[2], quantity=lines_input[3])})
    else:
        prod.update({lines_input[0]: Product(prod_type=lines_input[1],
                                             price=lines_input[2], quantity=lines_input[3])})
