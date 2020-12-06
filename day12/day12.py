inp = open('input.txt').read().splitlines()

d = {}
for l in inp:
    p, c = l.split(' <-> ')
    p = int(p)
    c = [int(x) for x in c.split(',')]
    d[p] = c

def sol(p):
    s = set()
    visit = []
    while True:
        s.add(p)
        if p in d:
            c = d[p]
            del d[p]
        for i in c:
            if i not in s:
                visit.append(i)
        if not visit:
            break
        p = visit.pop()
    return len(s)

print(sol(0))
groups = 1
while d:
    p = list(d.keys())[0]
    sol(p)
    groups += 1
print(groups)
