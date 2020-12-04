inp = [int(x) for x in open('input.txt').read().splitlines()]

sol = 0
pos = 0
while pos < len(inp):
    sol += 1
    j = inp[pos]
    inp[pos] += (1 if j < 3 else -1)
    pos += j
print(sol)
