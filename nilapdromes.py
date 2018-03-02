"""
Nilapdromes are similar to palindromes, but are quite different.
Nilapdromes are words which have 1 substring of random characters in the middle, called - the core,
and 2 identical substrings, surrounding it, called - the borders.
Examples of nilapdromes are: "aba", "asdthisasd", "baumyaubau". . .
Examples of INCORRECT nilapdromes are: "abbc", "SDSD", "_,#$x$#,_y".
For example, the nilapdrome "baumyaubau" - the core is "myau" and the borders are "bau".
You will be receiving input lines, containing exactly one nilapdrome, each, until you receive the command "end".
Your task is to make, from each nilapdrome - a new nilapdrome,
with borders - equal to the core (middle substring) of the given one, and core - equal to the borders of the given one.
For example, the nilapdrome "baumyaubau" should result in "myaubaumyau".
You should print each result nilapdrome, after you've created it, BEFORE reading the next one.
INCORRECT nilapdromes, should be IGNORED.

Examples

Input
aba
asdthisasd
baumyaubau
end

everythingnothingeverything
invalid
donenodedonee
abbc
sdsd
ssdd
dssd
end

Output
bab
thisasdthis
myaubaumyau

nothingeverythingnothing
ssdss

"""
input_word = None

while True:
    input_word = input()
    if input_word == 'end':
        break
    word_length = len(input_word)
    devided_word = word_length // 2
    if word_length % 2 == 0:
        left_slice = input_word[devided_word:]
        right_slice = input_word[:devided_word]
        if left_slice == right_slice:
            continue
    else:
        left_slice = input_word[devided_word + 1:]
        right_slice = input_word[:devided_word]
    while left_slice:
        if left_slice == right_slice:
            slice_len = len(right_slice)
            core_part = input_word[slice_len:-slice_len]
            print(core_part + left_slice + core_part)
            break
        else:
            left_slice = left_slice[1:]
            right_slice = right_slice[:-1]
