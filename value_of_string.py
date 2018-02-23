from string import ascii_lowercase, ascii_uppercase

"""
Write a program which finds the sum of the ASCII codes of the letters in a given string.
Your tasks will be a bit harder, because you will have to find the sum of either the lowercase or the uppercase letters.
On the first line, you will receive the string.
On the second line, you will receive one of two possible inputs:
If you receive "UPPERCASE"  find the sum of all uppercase English letters in the previously received string
 If you receive "LOWERCASE"  find the sum of all lowercase English letters in the previously received string
You should not sum the ASCII codes of any characters, which is not letters.
At the end print the sum in the following format:
The total sum is: {sum}

Input
HelloFromMyAwesomePROGRAM
LOWERCASE
AC/DC
UPPERCASE

Output
The total sum is: 1539
The total sum is: 267
"""
letters_sum = 0
input_letters = input()
case_to_check = input()

letters = filter(lambda x: x in ascii_lowercase if case_to_check == 'LOWERCASE' else x in ascii_uppercase, input_letters)
for letter in letters:
    letters_sum += ord(letter)

print(f'The total sum is: {letters_sum}')
