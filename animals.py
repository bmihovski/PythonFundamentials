from operator import attrgetter
from  collections import defaultdict

"""
You have been given the task to create classes for several sophisticated animals.
Create a class Dog which has a name (string), age (int) and number_of_legs (int).
Create a class Cat which has a name (string), age (int) and intelligence_quotient (int).
Create a class Snake which has a name (string), age(int) and cruelty_coefficient (int).
Create a method in each class which is called produce_sound().
The method should print on the console a string depending on the class:
    If it's a Dog, you should print "I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."
    It it's a Cat, you should print "I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."
    If it's a Snake, you should print "I'm a Sophistisnake, and I will now produce a sophisticated sound!
        Honey, I'm home."
Now for the real deal. You will receive several input commands, which will register animals or make them produce sounds,
until you receive the command "I'm your Huckleberry".
The commands will be in the following format:
{class} {name} {age} {parameter}
The class will be either "Dog", "Cat" or "Snake". The name will be a simple string,
which can contain any ASCII character BUT space. The age will be an integer. The parameter, will be an integer.
Depending on the class it would either be number of legs, IQ, or cruelty coefficient.
Register each animal, and keep them in collections, by your choice, so that you can ACCESS THEM BY NAME.
You will most likely need 3 collections, to store the different animals inside them.
Between the register commands you might receive a command in the following format:
talk {name}
You must then make the animal with the given name, produce a sound.

When you receive the ending command, you should print every animal in the following format:
    If it's a Dog, you should print "Dog: {name}, Age: {age}, Number Of Legs: {numberOfLegs}"
    It it's a Cat, you should print "Cat: {name}, Age: {age}, IQ: {intelligenceQuotient}"
    If it's a Snake, you should print "Snake: {name}, Age: {age}, Cruelty: {crueltyCoefficient}"
Print first the Dogs, then the Cats, and lastly - The Snakes.

Constraints
    You can assume that there will be no duplicate names (even in different animals).
    All input data will be valid. There will be no invalid input lines.
    The name in the talk command, will always be existent.

Examples

Input

Dog Sharo 3 4
Cat Garfield 5 200
Snake Alex 25 1000
talk Sharo
talk Garfield
talk Alex
I'm your Huckleberry

Output
I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.
I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.
I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.
Dog: Sharo, Age: 3, Number Of Legs: 4
Cat: Garfield, Age: 5, IQ: 200
Snake: Alex, Age: 25, Cruelty: 1000
"""


class Dog:
    def __init__(self, name, age, number_of_legs, class_name):
        self.name = name
        self.age = int(age)
        self.number_of_legs = int(number_of_legs)
        self.class_name = class_name

    def produce_sound(self):
        print("I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")

    def __str__(self):
        dog_bio = f'Dog: {self.name}, Age: {self.age}, Number Of Legs: {self.number_of_legs}'
        return dog_bio


class Cat:
    def __init__(self, name, age, iq, class_name):
        self.name = name
        self.age = int(age)
        self.iq = int(iq)
        self.class_name = class_name

    def produce_sound(self):
        print("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")

    def __str__(self):
        cat_bio = f'Cat: {self.name}, Age: {self.age}, IQ: {self.iq}'
        return cat_bio


class Snake:
    def __init__(self, name, age, cruelty, class_name):
        self.name = name
        self.age = int(age)
        self.cruelty = int(cruelty)
        self.class_name = class_name

    def produce_sound(self):
        print("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")

    def __str__(self):
        snake_bio = f'Snake: {self.name}, Age: {self.age}, Cruelty: {self.cruelty}'
        return snake_bio


animals = list()
talks = list()
line_inputs = list()

while True:
    line_inputs = input().split()
    if 'Dog' in line_inputs:
        animals.append(Dog(name=line_inputs[1], age=line_inputs[2],
                           number_of_legs=line_inputs[3], class_name='Dog'))
    elif 'Cat' in line_inputs:
        animals.append(Cat(name=line_inputs[1], age=line_inputs[2],
                           iq=line_inputs[3], class_name='Cat'))
    elif 'Snake' in line_inputs:
        animals.append(Snake(name=line_inputs[1], age=line_inputs[2],
                             cruelty=line_inputs[3], class_name='Snake'))
    elif "I'm" in line_inputs:
        break
    else:
        [animal.produce_sound() for animal in animals if line_inputs[1] == animal.name]

[print(animal) for animal in animals if animal.class_name == 'Dog']
[print(animal) for animal in animals if animal.class_name == 'Cat']
[print(animal) for animal in animals if animal.class_name == 'Snake']
