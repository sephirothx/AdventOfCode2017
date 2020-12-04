import itertools
inp = open('input.txt').read().splitlines()

sol = 0
for l in inp:
    for a,b in itertools.combinations(l.split(), 2):
        if a == b or sorted(a) == sorted(b):
            break
    else:
        sol += 1
print(sol)
