from collections import defaultdict

inp = open('input.txt').read().splitlines()

d = {
    '<': lambda x,y: x<y,
    '>': lambda x,y: x>y,
    '==': lambda x,y: x==y,
    '>=': lambda x,y: x>=y,
    '<=': lambda x,y: x<=y,
    '!=': lambda x,y: x!=y,
}

reg = defaultdict(int)
sol1 = 0
sol2 = 0
for l in inp:
    r1,op1,v1,_,r2,op2,v2 = l.split()
    v1,v2 = int(v1),int(v2)
    cond = d[op2](reg[r2], v2)
    if cond:
        reg[r1] += v1 if op1 == 'inc' else -v1
        sol2 = max(sol2, reg[r1])

for r in reg:
    sol1 = max(sol1, reg[r])

print(sol1)
print(sol2)
