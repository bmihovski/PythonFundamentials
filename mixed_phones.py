"""
You will be given several phone entries, in the form of strings in format:
{firstElement} : {secondElement}
The first element is usually the person's name, and the second one - his phone number.
The phone number consists ONLY of digits, while the person's name can consist of any ASCII characters.
Sometimes the phone operator gets distracted by the Minesweeper she plays all day, and gives you first the phone,
and then the name. e.g. : 0888888888 : Pesho. You must store them correctly, even in those cases.
When you receive the command "Over", you are to print all names you've stored with their phones.
The names must be printed in alphabetical order.
"""
inputs_stdin = list()
phonebook = dict()

while 'Over' not in inputs_stdin:
    inputs_stdin = input().split(' : ')
    if 'Over' in inputs_stdin:
        continue
    if inputs_stdin[1].isdigit():
        phonebook.update({inputs_stdin[0]: inputs_stdin[1]})
    else:
        phonebook.update({inputs_stdin[1]: inputs_stdin[0]})

{print(f'{name} -> {phonebook[name]}') for name in sorted(phonebook.keys())}
