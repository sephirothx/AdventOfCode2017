from collections import defaultdict
inp = open('input.txt').read().split(',')

d = defaultdict(int)
dist1 = dist2 = 0
for i in inp:
    d[i] += 1
    n = abs(d['n'] - d['s'])
    nw = abs(d['nw'] - d['se'])
    ne = abs(d['ne'] - d['sw'])
    dist1 = n + nw + ne - min(n, nw, ne)
    dist2 = max(dist2, dist1)

print(dist1)
print(dist2)
