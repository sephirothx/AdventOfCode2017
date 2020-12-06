inp = open('input.txt').read()

s = 0
sol1 = 0
sol2 = 0
garb = False
esc = False
for c in inp:
    if esc:
        esc = False
        continue
    if garb and c not in '>!':
        sol2 += 1
    if not garb and c == '{':
        s += 1
    elif not garb and c == '}':
        sol1 += s
        s -= 1
    elif not garb and c == '<':
        garb = True
    elif c == '>':
        garb = False
    elif c == '!':
        esc = True
print(sol1)
print(sol2)
