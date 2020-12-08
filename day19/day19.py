inp = open('input.txt').readlines()

pos = (0, 0)
d = (0, 1)

for i, c in enumerate(inp[0]):
    if c == '|':
        pos = (i, 0)

sol1 = ''
sol2 = 0
while True:
    sol2 += 1
    pos = (pos[0] + d[0], pos[1] + d[1])
    c = inp[pos[1]][pos[0]]
    if c == ' ':
        break
    elif c not in '|-+':
        sol1 += c
    elif c == '+':
        if d[0] == 0:
            if pos[0] != 0 and inp[pos[1]][pos[0]-1] != ' ':
                d = (-1, 0)
            else:
                d = (1, 0)
        elif pos[1] != 0 and inp[pos[1]-1][pos[0]] != ' ':
            d = (0, -1)
        else:
            d = (0, 1)

print(sol1)
print(sol2)
