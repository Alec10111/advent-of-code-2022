import string

def index(s):
    return string.ascii_lowercase.index(s.lower()) % 22

def parse_round(round):
    return [index(w) for w in round]

with open("input.txt") as file:
    rounds = [s.split(' ') for s in file.read().split("\n")]

print(rounds[:10])
numeric_rounds = [parse_round(r) for r in rounds]

def play(x,y):
    if x == y:
        return 0
    elif x > y:
        return 6
    else:
        return 3
    
print(numeric_rounds[:10])
result = [(res[1] + play(*res)) for res in numeric_rounds]
print(result)





