import string

with open("input.txt") as file:
    lines = file.readlines()

def find_repeated_character(line):
    first_set = set(line[:len(line)//2])
    for l in line[len(line)//2:]:
        if l in first_set:
            return l

repeated_chars = [find_repeated_character(l) for l in lines]
print(repeated_chars[:10])

def index(s):
    return string.ascii_lowercase.index(s.lower())
int_items = [index(r) for r in repeated_chars]

print(sum(int_items))
