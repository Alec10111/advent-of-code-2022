### Part One ###
################

with open('input.txt') as file:
    lines = file.readlines()
max_sum = 0
current_sum = 0
for l in lines:
    if l == '\n':
        if current_sum > max_sum:
            max_sum = current_sum
        current_sum = 0
        continue
    current_sum += int(l)
print(max_sum)


### Part Two ###
################

def split_lines(l):
    return l.split("\n\n")

def split_lists(ls):
    return [l.split("\n") for l in ls]

def int_list(xs):
    return [map(int,x) for x in xs]

with open("input.txt") as file:
    lines = file.read()

lines = int_list(split_lists(split_lines(lines)))
lines = sorted(map(sum,lines))
print(sum(lines[-3:]))
