inp = open('input.txt').read().splitlines()

layer = {}
sol1 = 0
for line in inp:
    l, r = [int(x) for x in line.split(':')]
    layer[l] = r
    if l % (2*r - 2) == 0:
        sol1 += l*r
print(sol1)

sol2 = 0
done = False
while not done:
    for l in layer:
        r = layer[l]
        if (sol2 + l) % (2*r - 2) == 0:
            sol2 += 1
            break
    else:
        done = True
print(sol2)
