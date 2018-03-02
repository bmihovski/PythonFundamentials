"""
You will be given groups of 2 strings, each on a new line. There will ALWAYS be at least 2 input lines,
and there will NEVER be a case when there are less than 2 input strings, for a given element of the input.
Now to the main logic - the elements of the input. You can refer to the elements of the input as states.
Each state also has a fiction - the collapsing factor. Your task is to collapse each state, by its given fiction.
The collapsing is done by removing all occurrences of the fiction in the state, and after that -
removing the first and last element of the fiction. You must then repeat the process,
until the fiction's length becomes 0.
When you finish the process, you must print what is left from the state.
If the state is also empty, you should print "(void)". NOTE: Border spaces should be removed.
Both the state and the fiction are strings, and will be given each on a separate line.
You must read sequences of DOUBLE lines, and print the result from the collapsing,
until you receive the command "collapse".

Examples

Input
astalavista baby
aaa
aaaa
aa
this will be funny rhight
this
collapse

bow chicka mow wow
mow
ahaia
hai
collapse

Output
stlvist bby
(void)

will be funny rght
bw chicka  ww
(void)
"""
while True:
    str_to_filter = input()
    if 'collapse' in str_to_filter:
        break
    fiction = input()

    if fiction in str_to_filter:
        str_to_filter = str_to_filter.replace(fiction, '')

    for _ in range(len(fiction), 2, -1):
        fiction = fiction[1:-1]
        str_to_filter = str_to_filter.replace(fiction, '')

    if str_to_filter == '':
        print(f'(void)')
    else:
        print(str_to_filter)
