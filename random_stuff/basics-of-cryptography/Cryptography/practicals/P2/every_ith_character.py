import re

INPUT_PATH = "ciphertext.txt"

WHITESPACE_PATTERN = re.compile(r'\s+')

def read_input(path):
    '''Reads the contents of a file as a string, removes all whitespace
    and returns the contents as a string.'''
    with open(path, "r") as file:
        string = file.read().rstrip()
    return re.sub(WHITESPACE_PATTERN, "", string)

def unshift_char(char, unshift):
    orig =  ord(char) - unshift
    if (orig < ord('A')):
        return chr(orig + 26)
    else:
        return chr(orig)

input_ = read_input(INPUT_PATH)

shifts = [0, 0, 0]

for i in range(len(shifts)):
    output = ""
    for j in range(i, len(input_), len(shifts)):
        output += unshift_char(input_[j], shifts[i])
    print(output)
