from collections import defaultdict
import re
inp = open('input.txt').read().splitlines()

reg = defaultdict(int)
ip = 0
sol1 = 0
while True:
    if ip >= len(inp):
        break
    op, v = inp[ip].split(' ', maxsplit=1)
    if op == 'snd':
        snd = reg[v]
    elif op == 'set':
        x, y = v.split()
        reg[x] = int(y) if re.match(r'-?\d+', y) else reg[y]
    elif op == 'sub':
        x, y = v.split()
        reg[x] -= int(y) if re.match(r'-?\d+', y) else reg[y]
    elif op == 'mul':
        sol1 += 1
        x, y = v.split()
        reg[x] *= int(y) if re.match(r'-?\d+', y) else reg[y]
    elif op == 'jnz':
        x, y = v.split()
        x = int(x) if re.match(r'-?\d+', x) else reg[x]
        if x != 0:
            ip += (int(y) if re.match(r'-?\d+', y) else reg[y]) - 1
    ip += 1

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

sol2 = 0
for n in range(109900, 126901, 17):
    if not is_prime(n):
        sol2 += 1

print(sol1)
print(sol2)
