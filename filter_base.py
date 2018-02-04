"""
You have been tasked to sort out a database full of information about employees.
You will be given several input lines containing information in one of the following formats:
    {name} -> {age}
    {name} -> {salary}
    {name} -> {position}
As you see you have 2 parameters. There can be only 3 cases of input:
If the second parameter is an integer, you must store it as name and age.
If the second parameter is a floating-point number, you must store it as name and salary.
If the second parameter is a string, you must store it as name and position.
You must read input lines, then parse and store the information from them, until you receive the command
"filter base". When you receive that command, the input sequence of employee information should end.
On the last line of input you will receive a string, which can either be "Age", "Salary" or "Position".
Depending on the case, you must print all entries which have been stored as name and age,
name and salary, or name and position.
In case, the given last line is "Age", you must print every employee, stored with its age in the following format:
Name: {name1}
Age: {age1}
====================
Name: {name2}
. . .
In case, the given last line is "Salary", you must print every employee, stored with its salary in the following format:
Name: {name1}
Salary: {salary1}
====================
Name: {name2}
. . .
In case, the given last line is "Position", you must print every employee,
stored with its position in the following format:
Name: {name1}
Position: {position1}
====================
Name: {name2}
. . .
NOTE: Every entry is separated with the other, with a string of 20 character '='.
There is NO particular order of printing - the data must be printed in order of input.

Input

Isacc -> 34
Peter -> CEO
Isacc -> 4500.054321
George -> Cleaner
John -> Security
Nina -> Secretary
filter base
Position

Ivan -> Chistach
Pesho -> Ohrana
Pesho -> 1323.0456
Ivan -> 732.404
Georgi -> 21
Georgi -> 21.02
filter base
Salary

Output

Name: Peter
Position: CEO
====================
Name: George
Position: Cleaner
====================
Name: John
Position: Security
====================
Name: Nina
Position: Secretary
====================

Name: Pesho
Salary: 1323.0456
====================
Name: Ivan
Salary: 732.404
====================
Name: Georgi
Salary: 21.02
====================

"""
input_employees = list()
employees = dict()
filter_type = None


def _print_employee(name, criteria):
    """
    Prints employee record base on criteria
    :param name: (Str) Employee name
    :param criteria: (Str) Record type based on Age, Salary and Position
    :return:
    """
    if criteria == 'Age':
        print('Name: ' + name)
        print(f'{criteria}: {employees[name]}')
        print('====================')
    elif criteria == 'Salary':
        print('Name: ' + name)
        print(f'{criteria}: {employees[name]}')
        print('====================')
    else:
        print('Name: ' + name)
        print(f'{criteria}: {employees[name]}')
        print('====================')


while True:
    input_employees = input().split(' -> ')
    if 'Age' in input_employees or 'Salary' in input_employees or 'Position' in input_employees:
        filter_type = input_employees[0]
        break
    elif 'filter base' in input_employees:
        continue
    elif input_employees[1].isdecimal():
        if input_employees[0] in employees:
            employees.pop(input_employees[0])
            employees.update({input_employees[0]: int(input_employees[1])})
        else:
            employees.update({input_employees[0]: int(input_employees[1])})
    else:
        try:
            employees.update({input_employees[0]: float(input_employees[1])})
            if input_employees[0] in employees:
                employees.pop(input_employees[0])
                employees.update({input_employees[0]: float(input_employees[1])})
            else:
                employees.update({input_employees[0]: float(input_employees[1])})
        except ValueError:
            if input_employees[0] in employees:
                employees.pop(input_employees[0])
                employees.update({input_employees[0]: input_employees[1]})
            else:
                employees.update({input_employees[0]: input_employees[1]})


if filter_type == 'Age':
    [_print_employee(key, filter_type) for key in employees.keys() if type(employees[key]) is int]
elif filter_type == 'Salary':
    [_print_employee(key, filter_type) for key in employees.keys() if type(employees[key]) is float]
else:
    [_print_employee(key, filter_type) for key in employees.keys() if type(employees[key]) is str]
