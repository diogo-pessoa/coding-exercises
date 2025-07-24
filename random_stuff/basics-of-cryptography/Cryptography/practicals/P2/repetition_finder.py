import re

INPUT_PATH = "ciphertext.txt"

WHITESPACE_PATTERN = re.compile(r'\s+')

def read_input(path):
    '''Reads the contents of a file as a string, removes all whitespace
    and returns the contents as a string.'''
    with open(path, "r") as file:
        string = file.read().rstrip()
    return re.sub(WHITESPACE_PATTERN, "", string)

def find_repetitions(string, slen):
    '''Finds all repeated substrings of a given length in a string and
    returns a dict from substrings to counts.'''
    cnts = {}
    for i in range(len(string) - slen + 1):
        subs = string[i : i + slen]
        cnt = string.count(subs)
        if cnt > 1:
            if subs in cnts.keys():
                pass
            else:
                cnts[subs] = cnt
    return cnts

input_ = read_input(INPUT_PATH)

for i in reversed(range(2, len(input_) // 2)):
    cnts = find_repetitions(input_, i)
    if len(cnts) > 0:
        print(str(i) + ": " + str(cnts))
