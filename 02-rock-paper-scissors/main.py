import string

def next(n):
    return (n+1)% 3

def prev(n):
    return (n-1) % 3

def index(s):
    return string.ascii_lowercase.index(s.lower()) % 23

def parse_round(round):
    return [index(w) for w in round]

with open("input.txt") as file:
    rounds = [s.split(' ') for s in file.read().split("\n")]

print("parsed_rounds",rounds[:10])
numeric_rounds = [parse_round(r) for r in rounds]

def play(x,y):
    if x == y:
        return 3 + y + 1
    elif y == next(x):
        return 6 + y + 1
    else:
        return y + 1
    
def choose_play(x,y):
    if y == 0:
        return [x, prev(x)]
    if y == 1:
        return [x,x]
    return [x, next(x)]

print("numeric_rounds", numeric_rounds[:10])
chosen_plays = [choose_play(*p) for p in numeric_rounds]

result = [play(*res) for res in numeric_rounds]
result2 = [play(*res) for res in chosen_plays]

print(sum(result))
print(sum(result2))
