"""
Strings can be hard to manipulate because of their immutable nature.
As a master of strings, you have to write a program, which will help the less experienced manipulate them.
On the first line, you will receive the string, which you have to manipulate.
On the next input lines, until you receive the command "end",
you' will receive a series of commands in one of the following formats:
"	"Left {count} times" - this command moves all elements left count times.
On each roll, the first element is placed at the end of the string.
"	"Right {count} times" - this command moves all elements left count times.
On each roll, the last element is placed at the beginning of the string.
"	"Insert {index} {string}" - insert the given string at the index.
"	"Delete {startIndex} {endIndex}" - delete the element from the startIndex (inclusive) to the endIndex (inclusive)
At the end, print the string after all modifications.

Input
"	The first input line will hold the string, which we have to manipulate.
"	The next lines will hold commands in the described formats.
"	The input ends with the keyword "end".
Output
"	After receiving the "end" command, print the string after all manipulations.
Constraints
"	All commands, indices and counts will be in the correct format and inside the string.
You do not have to check them explicitly.

Input
The Lone Ranger
Delete 0 7
Insert 0 Power
Insert 12 s
end

ReverseItAll
Left 20
Right 83
Delete 0 2
end

Output
Power Rangers
ReverseIt
"""
final_string = None
while True:
    input_strings = input()
    if 'end' in input_strings:
        break
    elif 'Delete' in input_strings:
        indexes_to_delete = input_strings.split()
        final_string = final_string.replace(final_string[int(indexes_to_delete[1]):int(indexes_to_delete[-1]) + 1], '')
    elif 'Insert' in input_strings:
        index_txt_to_insert = input_strings.split()
        final_string = (final_string[:int(index_txt_to_insert[1])] + index_txt_to_insert[2] +
                        final_string[int(index_txt_to_insert[1]):])
    elif 'Left' in input_strings:
        left_reverse = input_strings.split()
        for count in range(int(left_reverse[1])):
            final_string = final_string[1:] + final_string[0]
    elif 'Right' in input_strings:
        right_reverse = input_strings.split()
        for count in range(int(left_reverse[1])):
            final_string = final_string[-1] + final_string[:-1]
    else:
        final_string = input_strings

print(final_string)
